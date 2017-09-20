#!/usr/bin/env python3
# coding:utf8
import inspect
import functools
import re

NO_ONE_GROUP = ()
OWNER_GROUP = (407508177,)
ADMIN_GROUP = OWNER_GROUP + (578168406, 387210935, 85645231)


class CommandParserBase(object):
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

    @staticmethod
    def get_args(s):
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
        stripped = [s.group().strip('"\'').replace(
            '"', r'\"').replace("'", r"\'") for s in args]
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
                    sendmsg = '[CQ:at,qq=%s] %s' % (self.__fromQQ, ret)
                    s = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
                    return (s,)
            return None
        finally:
            self._ret_actions = ''
            self._result = ''

    def __init__(self):
        super(CommandParser,self).__init__()

    # decorator
    @staticmethod
    def handle(cmd, avaliable_group=OWNER_GROUP):
        print('decorator: adding cmd=' + str(cmd))

        def wrapped(f):
            if type(cmd) is type('str'):
                @functools.wraps(f)
                def run_or_not(self, s):
                    gp = self._route_group[f]
                    fromQQ = int(self.__fromQQ)
                    if gp is None or fromQQ in gp:
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
    @staticmethod
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
