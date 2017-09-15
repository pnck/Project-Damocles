# -*- coding:utf-8 -*-

import _CQSDK

EVENT_IGNORE        = 0     # 事件_忽略
EVENT_BLOCK         = 1     # 事件_拦截

REQUEST_ALLOW       = 1     # 请求_通过
REQUEST_DENY        = 2     # 请求_拒绝

REQUEST_GROUPADD    = 1     # 请求_群添加
REQUEST_GROUPINVITE = 2     # 请求_群邀请

CQLOG_DEBUG         = 0     # 调试 灰色
CQLOG_INFO          = 10    # 信息 黑色
CQLOG_INFOSUCCESS   = 11    # 信息(成功) 紫色
CQLOG_INFORECV      = 12    # 信息(接收) 蓝色
CQLOG_INFOSEND      = 13    # 信息(发送) 绿色
CQLOG_WARNING       = 20    # 警告 橙色
CQLOG_ERROR         = 30    # 错误 红色
CQLOG_FATAL         = 40    # 致命错误 深红


def i_hate_unicode_with_windows(f):
    def wrapper(*args):
        newargs = []
        for arg in args:
            if type(arg) is type(u'unicode'):
                arg = arg.encode('gbk')
            newargs.append(arg)    
        return f(*newargs)
    return wrapper
            

@i_hate_unicode_with_windows
def MessageBox(msg, title):
    return _CQSDK.MessageBox(msg, title)

@i_hate_unicode_with_windows
def GetAppID():
    return _CQSDK.GetAppID()

@i_hate_unicode_with_windows
def SendPrivateMsg(QQID, msg):
    return _CQSDK.SendPrivateMsg(QQID, msg)

@i_hate_unicode_with_windows
def SendGroupMsg(groupid, msg):
    return _CQSDK.SendGroupMsg(groupid, msg)

@i_hate_unicode_with_windows
def SendDiscussMsg(discussid, msg):
    return _CQSDK.SendDiscussMsg(discussid, msg)

@i_hate_unicode_with_windows
def SendLike(QQID):
    return _CQSDK.SendLike(QQID)

@i_hate_unicode_with_windows
def SetGroupKick(groupid, QQID, rejectaddrequest):
    return _CQSDK.SetGroupKick(groupid, QQID, rejectaddrequest)

@i_hate_unicode_with_windows
def SetGroupBan(groupid, QQID, duration):
    return _CQSDK.SetGroupBan(groupid, QQID, duration)

@i_hate_unicode_with_windows
def SetGroupAdmin(groupid, QQID, setadmin):
    return _CQSDK.SetGroupAdmin(groupid, QQID, setadmin)

@i_hate_unicode_with_windows
def SetGroupWholeBan(groupid, enableban):
    return _CQSDK.SetGroupWholeBan(groupid, enableban)

@i_hate_unicode_with_windows
def SetGroupAnonymousBan(groupid, anomymous, duration):
    return _CQSDK.SetGroupAnonymousBan(groupid, anomymous, duration)

@i_hate_unicode_with_windows
def SetGroupAnonymous(groupid, enableanomymous):
    return _CQSDK.SetGroupAnonymous(groupid, enableanomymous)

@i_hate_unicode_with_windows
def SetGroupCard(groupid, QQID, newcard):
    return _CQSDK.SetGroupCard(groupid, QQID, newcard)

@i_hate_unicode_with_windows
def SetGroupLeave(groupid, isdismiss):
    return _CQSDK.SetGroupLeave(groupid, isdismiss)

@i_hate_unicode_with_windows
def SetGroupSpecialTitle(groupid, QQID, newspecialtitle, duration):
    return _CQSDK.SetGroupSpecialTitle(groupid, QQID, newspecialtitle, duration)

@i_hate_unicode_with_windows
def SetDiscussLeave(discussid):
    return _CQSDK.SetDiscussLeave(discussid)

@i_hate_unicode_with_windows
def SetFriendAddRequest(responseflag, responseoperation, remark):
    return _CQSDK.SetFriendAddRequest(responseflag, responseoperation, remark)

@i_hate_unicode_with_windows
def SetGroupAddRequestV2(responseflag, requesttype, responseoperation, reason):
    return _CQSDK.SetGroupAddRequestV2(responseflag, requesttype, responseoperation, reason)

@i_hate_unicode_with_windows
def GetGroupMemberInfoV2(groupid, QQID, nocache = False):
    return _CQSDK.GetGroupMemberInfoV2(groupid, QQID, nocache)

@i_hate_unicode_with_windows
def GetGroupMemberList(groupid):
    return _CQSDK.GetGroupMemberList(groupid)
    
@i_hate_unicode_with_windows
def GetStrangerInfo(QQID, nocache = False):
    return _CQSDK.GetStrangerInfo(QQID, nocache)

@i_hate_unicode_with_windows
def AddLog(priority, category, content):
    return _CQSDK.AddLog(priority, category, content)

def GetCookies():
    return _CQSDK.GetCookies()

def GetCsrfToken():
    return _CQSDK.GetCsrfToken()

def GetLoginQQ():
    return _CQSDK.GetLoginQQ()

def GetLoginNick():
    return _CQSDK.GetLoginNick()

def GetAppDirectory():
    return _CQSDK.GetAppDirectory()

def SetFatal(errorinfo):
    return _CQSDK.SetFatal(errorinfo)
