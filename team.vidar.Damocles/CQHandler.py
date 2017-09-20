#!/usr/bin/env python2
# -*- coding:gbk -*-
# this file will be run on windows, please save as gbk encoding

import os
import sys
from random import seed, random
from time import time
import time
import functools
from commandparser import *

reload(sys)
sys.setdefaultencoding('gbk')

import HTMLParser
import xmlrpclib
import traceback
import ssl
import CQSDK
from keywordchain import KeywordChain
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'CQHanlder.log'),
    filemode='a+'
)

welcome_addional = ['Just hack for fun.', 'As we do, as you know', '���ǵ���;���ǳ���', '��������Ex��ɶ��Ӧ����զ���°�����զ������*������᲻�ᰡ��',
                    'dalao����Ex���ٶȰ����ٶ��£��ٶ�ȥ��*�ٶ��㶼�����𣿣�', 'C����������ֻ��C Primer Plus', '��ӭ��������ɳ��', '�ϳ���̹�˳���ak��ak����']


htmlparser = HTMLParser.HTMLParser()


def escape(s):
    return s.replace('&', '&amp;').replace('[', '&#91;').replace(']', '&#93;')


server = xmlrpclib.ServerProxy('https://116.196.104.11:1337',
                               context=ssl.SSLContext(ssl.PROTOCOL_TLSv1), allow_none=True)
try:
    if not server.echo('try echo') == 'try echo':
        raise xmlrpclib.Fault(-1, 'Try echo method failed, server invalid.')
        print('Available methods:' + str(server.system.listMethods()))

except xmlrpclib.Fault, e:
    traceback.print_exc()
    print('__________________')
    print(e.faultString)
    # sys.exit()
except Exception:
    traceback.print_exc()
    print('-------------NOT GOOD----------')
    # sys.exit()


def log_except(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, e:
            CQSDK.AddLog(CQSDK.CQLOG_WARNING, 'EXCEPTION', escape(str(e)))
    return wrapped


class NativeCommandParser(CommandParser):
    def __init__(self):
        super().__init__()

    @CommandParser.handle('/help', None)
    def on_help(self, s):
        s = s.strip()
        if not s:
            cmds = self._routes.copy()
            del cmds['default']
            self._result = '��������: ' + \
                '\\n'.join(repr(list(cmds.keys())).split(',')[1:-1])
            self._result += '\\n\\n����help������: admin | owner | /xxxx(i.e. /��ͷ�ľ�������)'
            self._result += '\\n\\nҪ�鿴Զ�����������֧�ֵ����������� [server]/help '
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
            a1 = 'CQSDK.SetGroupCard(fromGroup,{0},"{1}")'.format(
                who, newname)

            sendmsg = '[CQ:at,qq={0}] ���Ⱥ��Ƭ����'.format(who)
            a2 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)

            self._ret_actions = (a1, a2)

        except:
            traceback.print_exc()
            return False

    @CommandParser.handle('/rejectme', NO_ONE_GROUP)
    def on_test1(self, s):
        print('but...why exec?')

    @CommandParser.handle('/ban', ADMIN_GROUP)
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
            sendmsg = '[CQ:at,qq={0}] ��Ϣһ��θ��㽶ѹѹ��������ô����'.format(
                who)
            a2 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
            self._ret_actions = (a1, a2)

    @CommandParser.handle('/unban', ADMIN_GROUP)
    def on_unban(self, s):
        qq = self.get_args(s)[0]
        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', qq)
        if t:
            qq = t[0]
        a1 = 'CQSDK.SetGroupBan(fromGroup,{0},{1})'.format(qq, '0')
        self._ret_actions = (a1,)

    @CommandParser.handle('/law', None)
    def on_law(self, s):
        qq = self.get_args(s)[0]
        t = re.findall('(?<=\[CQ:at,qq=)\d+(?=\])', qq)
        if t:
            qq = t[0]
        sendmsg = '�����̷��ڶ��ٰ�ʮ�����涨��\\n���ڶ������ü��������������Ķ���Υ�����ҹ涨���Լ������Ϣϵͳ���ܽ���ɾ�����޸ġ����ӡ����ţ���ɼ������Ϣϵͳ�����������У�������صģ���������������ͽ�̻��߾��ۣ�����ر����صģ���������������ͽ�̡�\\nΥ�����ҹ涨���Լ������Ϣϵͳ�д洢��������ߴ�������ݺ�Ӧ�ó������ɾ�����޸ġ����ӵĲ�����������صģ�����ǰ��Ĺ涨������'
        sendmsg = '[CQ:at,qq={0}] {1}'.format(qq, sendmsg)
        a1 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
        self._ret_actions = (a1,)

    @CommandParser.handle('/learn', None)
    def on_learn(self, s):
        self._result = '����������ûʵ�ֺã���ֻ��������һ������Э��Ψһ��Ҫ����Ǵ��ţ��߽�ȥ��'
        pass

    @CommandParser.handle('/learn_c')
    @CommandParser.not_implemented
    def on_learn_c(self, s):
        pass


class CQHandler(object):
    def __init__(self):
        logging.info('__init__')

    def __del__(self):
        logging.info('__del__')

    def OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    @log_except
    def OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(
            subType, sendTime, fromQQ, msg, font))
        if fromQQ == 407508177:
            s = htmlparser.unescape(msg)
            if s[:8] == '[findkw]':
                s = s[8:]
                tracer = KeywordChain('learn')
                CQSDK.SendPrivateMsg(407508177, escape(
                    '[ack]' + repr(tracer.check(s))))
            if s[:5] == '[syn]':
                s = s[5:]
                CQSDK.SendPrivateMsg(407508177, escape('[ack]' + s))
            if s[:9] == '[forward]':
                CQSDK.SendGroupMsg(
                    650591057, '&#91;forward from [CQ:at,qq=%d]&#93; %s' % (fromQQ, escape(s[9:])))
        return False

    @log_except
    def OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(
            subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))
        s = htmlparser.unescape(msg)
        if s[:5] == '[syn]':
            s = s[5:]
            CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq=%d]  %s' % (
                fromQQ, escape('[ack]' + s)))
        elif s[:8] in ('[server]', '[SERVER]'):
            s = s[8:]
            actions = server.handle_OnEvent_GroupMsg(subType, sendTime, u'%s' % (
                fromGroup,), u'%s' % (fromQQ,), u'%s' % (fromAnonymous,), s.decode('gbk'), font)
            logging.warn('GOT %s ' % (actions,))
            if type(actions) in (type(tuple()), type(list())):
                for action in actions:
                    if type(action) is type(u'unicode'):
                        action = action.encode('gbk')
                    if type(action) is type('string'):
                        logging.warn('attempt to exec[%s]' % (action,))
                        exec(action.lstrip())
            return True
        else:
            while True:
                sendmsg = '[CQ:at,qq=%d] ' % (fromQQ,)
                if KeywordChain('learn').check(s):
                    sendmsg += "��������ŵĻ�������Ҫ��c����Ϊ������\n����ѧϰc��������Ч�Ļ��ǿ�C primer plus��http://t.cn/RCP5AgV \nPS: ��ò�Ҫ��̷��ǿ��XX�쾫ͨ�����Ǵ����ŵ���ͨϵ�� [CQ:face,id=21]"
                elif KeywordChain('hack').check(s):
                    sendmsg += "�����̷��ڶ��ٰ�ʮ�����涨��\n���ڶ������ü��������������Ķ���Υ�����ҹ涨���Լ������Ϣϵͳ���ܽ���ɾ�����޸ġ����ӡ����ţ���ɼ������Ϣϵͳ�����������У�������صģ���������������ͽ�̻��߾��ۣ�����ر����صģ���������������ͽ�̡�\nΥ�����ҹ涨���Լ������Ϣϵͳ�д洢��������ߴ�������ݺ�Ӧ�ó������ɾ�����޸ġ����ӵĲ�����������صģ�����ǰ��Ĺ涨������"
                elif KeywordChain('isa').check(s):
                    sendmsg += " �������������Ϣ��ȫЭ���ַ�Ļ�������һ�̣�����¥��111������һ����¥��һ�����ȹ��������пƼ���613��\n��ӭ��ʱ����[CQ:face,id=21]"
                elif KeywordChain('reg').check(s):
                    sendmsg += "���ϵı�����ַ: http://reg.vidar.club/ ��ֽ�������Ե�ʱ���������\n�Ƽ����ϱ���o(*^��^*)��[CQ:face,id=21]"
                elif KeywordChain('dress').check(s):
                    sendmsg += "�Ҹ���10����ȥ׼�������Ůװ"
                    CQSDK.SetGroupBan(fromGroup, fromQQ, 10 * 60)
                elif KeywordChain('duty').check(s):
                    hour = time.localtime(time.time())
                    if hour <= 6:
                        sendmsg += "��ô�����ûʲô������"
                    elif hour in range(7, 10):
                        sendmsg += "��Ŷ���˯���ɣ���֪��������û��������"
                    elif hour in range(10, 12):
                        sendmsg += "���Ӧ�����˿�����"
                    elif hour == 12:
                        sendmsg += "�������û�м���ȥ���緹�Ļ�Ӧ������"
                    elif hour in range(13, 17):
                        sendmsg += "����һ�㶼�����ڵ�"
                    elif hour in range(17, 19):
                        sendmsg += "�������û�м���ȥ�����Ļ�Ӧ������"
                    elif hour in range(19, 21):
                        sendmsg += "��Ӧ�ö�û��ȥ��"
                    elif hour in range(22, 24):
                        sendmsg += "��ô���ˣ���������ͨ������ȻӦ��û����,��ѧУ�ǲ���ͨ����"
                    else:
                        sendmsg += "����ֵ�����ʲôʱ��㣿����"
                else:
                    break
                CQSDK.SendGroupMsg(fromGroup, sendmsg)
                return True
        return False

    def OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(
            subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(
            subType, sendTime, fromGroup, beingOperateQQ))

    def OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(
            subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    @log_except
    def OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(
            subType, sendTime, fromGroup, fromQQ, beingOperateQQ))
        seed(time())
        i = int(random() * 1000) % len(welcome_addional)
        sendmsg = '[CQ:at,qq=%d]' % (beingOperateQQ,)
        sendmsg += "��ӭ����Vidar-Team2017������Ⱥ\n�����Ķ��������\n1��Э�����: https://vidar.club \nwiki��https://wiki.vidar.club/doku.php \ndrops��https://drops.vidar.club/ \n2��Ϊ���ô�Ҹ��õ��໥�˽⣬���ȸ���һ��Ⱥ��Ƭ��\n��ע��ʽΪ17-רҵ-����\n3�������κ����ʣ�����Ⱥ�ﰬ�ع���Ա���� \n PS:"
        sendmsg += welcome_addional[i]
        CQSDK.SendGroupMsg(fromGroup, sendmsg)

    def OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(
            subType, sendTime, fromQQ))

    def OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(
            subType, sendTime, fromQQ, msg, responseFlag))

    def OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(
            subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')
