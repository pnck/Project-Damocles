#!/usr/bin/env python3
# coding:utf8
import os
import sys
import inspect
import traceback
import socketserver
import ssl
import xmlrpc.server
import re
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

NO_ONE_GROUP = ()
OWNER_GROUP = (407508177,)
ADMIN_GROUP = OWNER_GROUP + (578168406, 387210935, 85645231)


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


class CommandParserBase:
    _routes = {}
    _route_group = {}

    @property
    def result(self):
        ret = self._result
        self._result = ''
        return ret

    @staticmethod
    def escape_cqcode(s):
        return s.replace('&', '&amp;').replace('[', '&#91;').replace(']', '&#93;')

    def get_args(self,s):
        s = str(s)
        args = []
        while s:
            s = s.strip()
            #print('s=>\t\t', s)
            n1 = s.find("'")
            n2 = s.find('"')
            if n1 == 0 and n1 < n2:  # leading '
                t1 = re.search(r'''    '.+?'    '''.strip(), s)
                l = list(s)
                args.append(t1)
                del l[t1.start():t1.end()]
                s = ''.join(l)
                #print('AFTER-t1>\t', s)
                continue

            if n2 == 0 and n2 < n1:  # leading "
                t2 = re.search(r'''    ".+?"    '''.strip(), s)
                l = list(s)
                args.append(t2)
                del l[t2.start():t2.end()]
                s = ''.join(l)
                #print('AFTER-t2>\t', s)
                continue

            else:
                t3 = re.search(r'''   \S+    '''.strip(), s)
                l = list(s)
                args.append(t3)
                del l[t3.start():t3.end()]
                s = ''.join(l)
                #print('AFTER-t3>\t', s)
        stripped = [s.group().strip('"\'').replace('"',r'\"').replace("'",r"\'") for s in args]
        return stripped

    def default_action(self):
        pass

    def not_implemented_action(self, *a, **kw):
        self._result = '{} not implemented'.format(self._route_to)
        return True

    def __init__(self):
        self._ret_actions = ''
        self._result = ''
        self._routes.update({'default': self.default_action})
        self._route_to = 'default'
        self._route_group.update({self.default_action: None})


class CommandParser(CommandParserBase):
    def get_actions(self):
        try:
            if self._ret_actions:
                if type(self._ret_actions) is type('str'):
                    return (self._ret_actions,)
                else:
                    return tuple(self._ret_actions)
            else:
                ret = self.result
                print('RET:=> ', ret)
                if ret:
                    sendmsg = '[CQ:at,qq=%d] %s' % (self.__fromQQ, ret)
                    s = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
                    return (s,)
            return None
        finally:
            self._ret_actions = ''
            self._result = ''

    def __init__(self):
        super().__init__()

    # decorator
    def handle(cmd, avaliable_group=OWNER_GROUP):
        print('decorator: adding cmd=' + str(cmd))

        def wrapped(f):
            if type(f) is type(CommandParserBase.default_action) and type(cmd) is type('str'):
                def run_or_not(self, s):
                    gp = self._route_group[f]
                    if gp is None or self.__fromQQ in gp:
                        return f(self, s)
                    else:
                        self._result = '你没权限执行这个命令'
                        return None

                CommandParserBase._route_group.update(
                    {run_or_not: avaliable_group, f: avaliable_group})
                CommandParserBase._routes.update({cmd: run_or_not})
                return run_or_not
            else:
                return CommandParserBase.default_action
        return wrapped

    # decorator
    def not_implemented(f):
        return CommandParserBase.not_implemented_action

    def parse(self, fromQQ, msg, subtype=0, sendTime=None, fromGroup=None, fromDiscuss=None, fromAnonymous=None):
        msg = msg.strip()
        print('parsing:=> ' + msg)
        self._route_to = 'default'
        for k in self._routes:
            if k == 'default':
                continue
            if msg.find(k) == 0:  # msg => /xxxx
                # self._route_to => /aaaxxxxx, k => /aaa
                if self._route_to.find(k) == 0:
                    continue
                self._route_to = k
        if self._route_to == 'default':  # still default,just return
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

        # print('msg:[{0}]|self_route_to => {1} |||| routes{{{2}}}'.format(msg,self._route_to,self._routes))

        # call action
        fcalling = self._routes[self._route_to]
        ret = None
        if inspect.isfunction(fcalling):
            ret = fcalling(self, '' + msg[len(self._route_to):])
        elif inspect.ismethod(fcalling):
            ret = fcalling('' + msg[len(self._route_to):])
        else:
            return False

        if ret or ret is None:
            return True
        else:
            return False

    @handle('/help', None)
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
                    a1, repr(self._route_group[self._routes[a1]])).replace(',)', ')').replace('None', 'All').replace('()','None')

    @handle('/cmd', OWNER_GROUP)
    def on_cmd(self, s):
        fromQQ = int(self.__fromQQ)
        self._result = 'accepted,args[{}]'.format(','.join(self.get_args(s)))

    @handle('/setname', ADMIN_GROUP)
    def on_setname(self, s):
        try:
            who, newname = self.get_args(s)[:2]
            a1 = 'CQSDK.SetGroupCard(fromGroup,{0},"{1}")'.format(
                who, newname)

            sendmsg = '[CQ:at,qq={0}] 你的群名片改了'.format(who)
            a2 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)

            self._ret_actions = (a1, a2)

        except:
            traceback.print_exc()
            return False

    @handle('/rejectme', NO_ONE_GROUP)
    def on_test1(self, s):
        print('but...why exec?')

    @handle('/ban', ADMIN_GROUP)
    def on_ban(self, s):
        who, duration = self.get_args(s)[:2]
        duration = int(duration)
        who = str(who)
        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', who)
        if t:
            who = t[0]

        if int(duration) >= 1:
            a1 = 'CQSDK.SetGroupBan(fromGroup,{0},{1})'.format(
                who, duration * 60)
            sendmsg = '[CQ:at,qq={0}] 休息一会次根香蕉压压惊，别辣么浮躁'.format(who)
            a2 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
            self._ret_actions = (a1, a2)

    @handle('/unban', ADMIN_GROUP)
    def on_unban(self, s):
        qq = self.get_args(s)[0]
        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', qq)
        if t:
            qq = t[0]
        a1 = 'CQSDK.SetGroupBan(fromGroup,{0},{1})'.format(qq, '0')
        self._ret_actions = (a1,)

    @handle('/learn', None)
    def on_learn(self, s):
        self._result = '现在这个命令还没实现好，先只告诉你们一条：进协会唯一的要求就是打开门，走进去。'
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

    @handle('/whereareyou')
    @not_implemented
    def on_where(self, s):
        pass

    @handle('/law', None)
    def on_law(self, s):
        qq = self.get_args(s)[0]

        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', qq)
        if t:
            qq = t[0]

        sendmsg = '国家刑法第二百八十六条规定，\\n关于恶意利用计算机犯罪相关条文对于违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。\\n违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行删除、修改、增加的操作，后果严重的，依照前款的规定处罚。'
        sendmsg = '[CQ:at,qq={0}] {1}'.format(qq, sendmsg)
        a1 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
        self._ret_actions = (a1,)


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
