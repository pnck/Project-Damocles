#!/usr/bin/env python3
# coding:utf8
import os
import sys
import socketserver
import ssl
import xmlrpc.server
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


class CQRemoteHandlerImplement:
    def __init__(self):
        self.__parser = CommandParser()

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

        if self.__parser.parse(fromQQ, msg, subType, sendTime, fromGroup, fromAnonymous=fromAnonymous):
            sendmsg = '[CQ:at,qq=%d] %s' % (fromQQ,self.__parser.result)
            s = "CQSDK.SendGroupMsg(fromGroup,'{}'".format(sendmsg)
        else:
            return "CQSDK.SendGroupMsg(fromGroup,'[CQ:at,qq=%d] action from server'%(fromQQ,))"

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


class CommandParser:
    @staticmethod
    def escape_cqcode(s):
        return s.replace('&', '&amp;').replace('[', '&#91;').replace(']', '&#93;')

    @property
    def result(self):
        return self.__result

    def __init__(self):
        self.__route = {'default': self.default_action}

    def default_action(self):
        pass

    def not_implemented_action(self):
        return '''CQSDK.SendGroupMsg(fromGroup,'[CQ:at,qq=%d] not implemented'%(fromQQ,))'''

    # decorator
    def handle(cmd):
        #print('cmd=',cmd)
        def classdeco(self):
            #print('self=',self)
            def wrapped(f):
                #print('wrapped called',self.__route)
                if type(f) is type(self.default_route) and type(cmd) is type('str'):
                    if cmd != 'default':
                        self.__route[cmd] = f
                return f
            return wrapped
        return classdeco

    # decorator
    def not_implemented(self):
        print('NOT===>self=',self)
        def wrapped(f):
            print('      [f]=',f)
            return self.not_implemented_action
        return wrapped

    def parse(self, fromQQ, msg, subtype=0, sendTime=None, fromGroup=None, fromDiscuss=None, fromAnonymous=None):
        msg = msg.strip()
        route_to = 'default'
        for k in self.__route:
            if k == 'default':
                continue
            if msg.find(k) == 0:  # msg => /xxxx
                if route_to.find(k) == 0:  # route_to => /aaaxxxxx, k => /aaa
                    continue
        else:  # still default,just return
            return False

        self.__subtype = subtype
        self.__sendTime = sendTime
        self.__fromGroup = fromGroup
        self.__fromDiscuss = fromDiscuss
        self.__fromAnonymous = fromAnonymous
        self.__fromQQ = fromQQ

        if fromGroup is not None:  # from group
            pass
        elif fromDiscuss is not None:  # from discuss
            pass
        else:  # from private
            pass

        # call action
        ret = self.__route[route_to](msg[len(route_to):])
        if ret or ret is None:
            return True
        else:
            return False

    @handle('/help')
    def on_help(self, s):
        cmds = self.__route
        del cmds['default']
        self.__result = 'Available commands: ' + repr(cmds)

    @handle('/cmd')
    def on_cmd(self, s):
        try:
            fromQQ = int(fromQQ)
            if fromQQ == 407508177:
                pass
        except:
            pass

    @handle('/learn')
    @not_implemented
    def on_learn(self, s):
        pass

    @handle('/learn_c')
    @not_implemented
    def on_learn_c(self, s):
        pass

    @handle('/createfile')
    @not_implemented
    def on_createfile(self, s):
        pass

    @handle('/build')
    @not_implemented
    def on_build(self, s):
        pass


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
