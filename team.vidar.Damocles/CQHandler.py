#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding('gbk')

import HTMLParser
import xmlrpclib
import traceback
import ssl
import CQSDK
import logging
logging.basicConfig(
    level       = logging.INFO,
    format      = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S',
    filename    = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CQHanlder.log'),
    filemode    = 'a+'
)

htmlparser = HTMLParser.HTMLParser()
def escape(s):
    return s.replace('&','&amp;').replace('[','&#91;').replace(']','&#93;')

server = xmlrpclib.ServerProxy('https://116.196.104.11:1337',context=ssl.SSLContext(ssl.PROTOCOL_TLSv1),allow_none=True)
try:
    if not server.echo('try echo') == 'try echo':
        raise xmlrpclib.Fault(-1,'Try echo method failed, server invalid.')
	print('Available methods:'+str(server.system.listMethods()))
	
except xmlrpclib.Fault,e:
    traceback.print_exc()
    print('__________________')
    print(e.faultString)
    #sys.exit()
except Exception:
    traceback.print_exc()
    print('-------------NOT GOOD----------')
    #sys.exit()


class CQHandler:
    def __init__(self):
        logging.info('__init__')

    def __del__(self):
        logging.info('__del__')

    def OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(subType, sendTime, fromQQ, msg, font))
        if fromQQ == 407508177:
            s = htmlparser.unescape(msg)
            if s[:5] == '[syn]':
                s = s[5:]
                CQSDK.SendPrivateMsg(407508177,escape('[ack]'+s))
            if s[:9] == '[forward]':
                CQSDK.SendGroupMsg(650591057,'&#91;forward from [CQ:at,qq=%d]&#93; %s' % (fromQQ,escape(s[9:])))
        
    def OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))
        s = htmlparser.unescape(msg)
        if s[:5] == '[syn]':
            s = s[5:]
            CQSDK.SendGroupMsg(fromGroup,'[CQ:at,qq=%d]  %s' % (fromQQ,escape('[ack]'+s)))
        if s[:8] in ('[server]','[SERVER]'):
            s = s[8:]
            try:
                actions = server.handle_OnEvent_GroupMsg(subType, sendTime, fromGroup, fromQQ, fromAnonymous, s, font)
                logging.warn('GOT %s ' % (actions,))
                if type(actions) in ( type(tuple()) , type(list()) ):
                    for action in actions:
                        if type(action) is type(u'unicode'):
                            action = action.encode('gbk')
                        if type(action) is type('string'):
                            logging.warn('attempt to exec[%s]' % (action,))
                            exec(action.lstrip())
            except Exception,e:
                CQSDK.AddLog(CQSDK.CQLOG_WARNING,'RPCFAILED',escape(str(e)))



    def OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(subType, sendTime, fromGroup, beingOperateQQ))

    def OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(subType, sendTime, fromQQ))

    def OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(subType, sendTime, fromQQ, msg, responseFlag))

    def OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')
