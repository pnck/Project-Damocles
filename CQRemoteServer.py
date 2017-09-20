#!/usr/bin/env python3
# coding:utf8
import os
import sys
import traceback
import socketserver
import ssl
import xmlrpc.server
import re
from commandparser import *
import rollbattle
try:
    import fcntl
except ImportError:
    fcntl = None

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'Server_CQHanlder.log'),
    filemode='w+'
)


CERTFILE = 'cert.pem'
KEYFILE = 'key.pem'


class SecureXMLRPCServer(socketserver.ThreadingTCPServer, xmlrpc.server.SimpleXMLRPCDispatcher):
    allow_reuse_address = True

    def __init__(self, addr, certfile, keyfile=None,
                 requestHandler=xmlrpc.server.SimpleXMLRPCRequestHandler,
                 logRequests=True, allow_none=False, encoding=None,
                 bind_and_activate=True, ssl_version=ssl.PROTOCOL_TLSv1):
        self.logRequests = logRequests

        # create an SSL context
        self.context = ssl.SSLContext(ssl_version)
        self.context.load_cert_chain(certfile=certfile, keyfile=keyfile)

        xmlrpc.server.SimpleXMLRPCDispatcher.__init__(self, allow_none,
                                                      encoding)
        # call TCPServer constructor
        socketserver.TCPServer.__init__(
            self, addr, requestHandler, bind_and_activate)

        if fcntl is not None and hasattr(fcntl, 'FD_CLOEXEC'):
            flags = fcntl.fcntl(self.fileno(), fcntl.F_GETFD)
            flags |= fcntl.FD_CLOEXEC
            fcntl.fcntl(self.fileno(), fcntl.F_SETFD, flags)

    def get_request(self):
        newsocket, fromaddr = self.socket.accept()
        # create an server-side SSL socket
        sslsocket = self.context.wrap_socket(newsocket, server_side=True)
        return sslsocket, fromaddr


class ServerCommandParser(CommandParser):
    def __init__(self):
        super().__init__()

    @CommandParser.handle('/help', None)
    def on_help(self, s):
        s = s.strip()
        if not s:
            cmds = self._routes.copy()
            del cmds['default']
            self._result = 'Available commands: ' + repr(list(cmds.keys()))
            self._result += '\\n\\nAvaliable help contexts: admin | owner | /xxxx(i.e. concrete command begins with slash)'
        else:
            args = self.get_args(s)
            a1 = args[0].lower()
            if a1 == 'admin':
                self._result = 'Admins: ' + repr(list(ADMIN_GROUP))
            elif a1 == 'owner':
                self._result = 'Owner: ' + repr(list(OWNER_GROUP))
            elif a1 in self._routes.keys():
                self._result = 'Available user group of {0} : {1}'.format(
                    a1, repr(self._route_group[self._routes[a1]])).replace(',)', ')').replace('None', 'All').replace('()', 'None')

    @CommandParser.handle('/setname', ADMIN_GROUP)
    def on_setname(self, s):
        try:
            who, newname = self.get_args(s)[:2]
            who = str(who)
            t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', who)
            if t:
                who = t[0]
            a1 = 'CQSDK.SetGroupCard(fromGroup,{0},{1})'.format(
                who, "'''" + newname + "'''")

            sendmsg = '[CQ:at,qq={0}] 你的群名片改了'.format(who)
            a2 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
            self._ret_actions = (a1, a2)
            print(a1, a2)
        except:
            traceback.print_exc()
            return False

    @CommandParser.handle('/cmd', OWNER_GROUP)
    def on_cmd(self, s):
        fromQQ = int(self._fromQQ)
        #self._result = 'accepted,args[{}]'.format(','.join(self.get_args(s)))
        self._result = repr(os.popen(s).read())[1:-1]

    @CommandParser.handle('/createfile')
    @CommandParser.not_implemented
    def on_createfile(self, s):
        pass

    @CommandParser.handle('/build')
    @CommandParser.not_implemented
    def on_build(self, s):
        pass

    @CommandParser.handle('/roll')
    def on_where(self, s):
        challenger = int(self._fromQQ)
        against,request_time = self.get_args(s)[:2]
        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', against)
        if t:
            against = t[0]
        against = int(against)
        request_time = int(request_time)
        result = rollbattle.roll(challenger,against,request_time)
        print('R=>',result)

class CQRemoteHandlerImplement:
    def __init__(self):
        self.__parser = ServerCommandParser()

    def echo(self, s):
        return s

    def handle_OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def handle_OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def handle_OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(
            subType, sendTime, fromQQ, msg, font))

    def handle_OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(
            subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))

        try:
            if self.__parser.parse(fromQQ, msg, subType, sendTime, fromGroup, fromAnonymous=fromAnonymous):
                return self.__parser.get_actions()

            else:
                # return ("CQSDK.SendGroupMsg(fromGroup,'[CQ:at,qq=%d] action from server'%(fromQQ,))",)
                pass
        except:
            traceback.print_exc()
            return None

    def handle_OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(
            subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def handle_OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(
            subType, sendTime, fromGroup, beingOperateQQ))

    def handle_OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(
            subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def handle_OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(
            subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def handle_OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(
            subType, sendTime, fromQQ))

    def handle_OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(
            subType, sendTime, fromQQ, msg, responseFlag))

    def handle_OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(
            subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def handle_OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def handle_OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def handle_OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')


if __name__ == '__main__':
    cqServer = SecureXMLRPCServer(
        ('0.0.0.0', 1337), certfile=CERTFILE, keyfile=KEYFILE, allow_none=True)
    cqServer.register_introspection_functions()
    cqServer.register_instance(
        CQRemoteHandlerImplement(), allow_dotted_names=True)
    cqServer.register_multicall_functions()
    print('__Server started__')
    try:
        cqServer.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
