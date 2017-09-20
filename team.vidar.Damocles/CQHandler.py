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

welcome_addional = ['Just hack for fun.', 'As we do, as you know', '我们的征途是星辰大海', '萌新三连Ex：啥玩应啊？咋回事啊？那咋整啊？*大佬你会不会啊！',
                    'dalao三连Ex：百度啊，百度呗，百度去，*百度你都不会吗？！', 'C语言入门我只服C Primer Plus', '欢迎来到炽热沙城', '上车吗？坦克车，ak带ak带队']


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
            self._result = '可用命令: ' + \
                '\\n'.join(repr(list(cmds.keys())).split(',')[1:-1])
            self._result += '\\n\\n可用help上下文: admin | owner | /xxxx(i.e. /开头的具体命令)'
            self._result += '\\n\\n要查看远程命令服务器支持的命令请输入 [server]/help '
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

            sendmsg = '[CQ:at,qq={0}] 你的群名片改了'.format(who)
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
            sendmsg = '[CQ:at,qq={0}] 休息一会次根香蕉压压惊，别辣么浮躁'.format(
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
        sendmsg = '国家刑法第二百八十六条规定，\\n关于恶意利用计算机犯罪相关条文对于违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。\\n违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行删除、修改、增加的操作，后果严重的，依照前款的规定处罚。'
        sendmsg = '[CQ:at,qq={0}] {1}'.format(qq, sendmsg)
        a1 = 'CQSDK.SendGroupMsg(fromGroup,"{}")'.format(sendmsg)
        self._ret_actions = (a1,)

    @CommandParser.handle('/learn', None)
    def on_learn(self, s):
        self._result = '现在这个命令还没实现好，先只告诉你们一条：进协会唯一的要求就是打开门，走进去。'
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
                    sendmsg += "如果想入门的话，还是要以c语言为基础。\n至于学习c语言最有效的还是看C primer plus。http://t.cn/RCP5AgV \nPS: 最好不要看谭浩强，XX天精通或者是从入门到精通系列 [CQ:face,id=21]"
                elif KeywordChain('hack').check(s):
                    sendmsg += "国家刑法第二百八十六条规定，\n关于恶意利用计算机犯罪相关条文对于违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。\n违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行删除、修改、增加的操作，后果严重的，依照前款的规定处罚。"
                elif KeywordChain('isa').check(s):
                    sendmsg += " 如果你是想问信息安全协会地址的话。是在一教（信仁楼）111，或者一教三楼“一教卖热狗”，还有科技馆613。\n欢迎随时过来[CQ:face,id=21]"
                elif KeywordChain('reg').check(s):
                    sendmsg += "线上的报名地址: http://reg.vidar.club/ ，纸质在面试的时候带过来。\n推荐线上报名o(*^▽^*)┛[CQ:face,id=21]"
                elif KeywordChain('dress').check(s):
                    sendmsg += "我给你10分钟去准备好你的女装"
                    CQSDK.SetGroupBan(fromGroup, fromQQ, 10 * 60)
                elif KeywordChain('duty').check(s):
                    hour = time.localtime(time.time())
                    if hour <= 6:
                        sendmsg += "这么早估计没什么人起来"
                    elif hour in range(7, 10):
                        sendmsg += "大概都在睡觉吧，不知道今天有没有人早起"
                    elif hour in range(10, 12):
                        sendmsg += "这点应该有人开门了"
                    elif hour == 12:
                        sendmsg += "不清楚，没有集体去吃午饭的话应该有人"
                    elif hour in range(13, 17):
                        sendmsg += "下午一般都有人在的"
                    elif hour in range(17, 19):
                        sendmsg += "不清楚，没有集体去吃晚饭的话应该有人"
                    elif hour in range(19, 21):
                        sendmsg += "人应该都没回去呢"
                    elif hour in range(22, 24):
                        sendmsg += "这么晚了，除非有人通宵，不然应该没人了,但学校是不给通宵的"
                    else:
                        sendmsg += "你出现的这是什么时间点？？？"
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
        sendmsg += "欢迎加入Vidar-Team2017届新生群\n请先阅读以下事项：\n1、协会官网: https://vidar.club \nwiki：https://wiki.vidar.club/doku.php \ndrops：https://drops.vidar.club/ \n2、为了让大家更好的相互了解，请先更改一下群名片。\n备注格式为17-专业-姓名\n3、如有任何疑问，请在群里艾特管理员提问 \n PS:"
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
