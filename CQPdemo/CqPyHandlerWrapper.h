//
// Created by pnck on 9/8/17.
//

#ifndef PROJECT_DAMOCLES_CQPYHANDLERWRAPPER_H
#define PROJECT_DAMOCLES_CQPYHANDLERWRAPPER_H

//#include "C:\\Python27\include\Python.h"
#include <python2.7/Python.h>
#include <bits/shared_ptr.h>
#include "stdafx.h"
#include "cqp.h
#include "utils.h"
#include "appmain.h"

#define CQAPPID (__CQ_APPID__.c_str())
#define CQAPPINFO (__CQ_APPINFO__.c_str())

inline void CQ_MessageBox(const char *msg, const char *title) {
    ::MessageBox(NULL, msg, title, MB_OK);
}

inline const char *CQ_GetAppID() {
    return CQAPPID;
}

inline int32_t CQ_SendPrivateMsg(int64_t QQID, const char *msg) {
    return CQ_sendPrivateMsg(g_authCode, QQID, msg);
}

inline int32_t CQ_SendGroupMsg(int64_t groupid, const char *msg) {
    return CQ_sendGroupMsg(g_authCode, groupid, msg);
}

inline int32_t CQ_SendDiscussMsg(int64_t discussid, const char *msg) {
    return CQ_sendDiscussMsg(g_authCode, discussid, msg);
}

inline int32_t CQ_SendLike(int64_t QQID) {
    return CQ_sendLike(g_authCode, QQID);
}

inline int32_t CQ_SetGroupKick(int64_t groupid, int64_t QQID, CQBOOL rejectaddrequest) {
    return CQ_setGroupKick(g_authCode, groupid, QQID, rejectaddrequest);
}

inline int32_t CQ_SetGroupBan(int64_t groupid, int64_t QQID, int64_t duration) {
    return CQ_setGroupBan(g_authCode, groupid, QQID, duration);
}

inline int32_t CQ_SetGroupAdmin(int64_t groupid, int64_t QQID, CQBOOL setadmin) {
    return CQ_setGroupAdmin(g_authCode, groupid, QQID, setadmin);
}

inline int32_t CQ_SetGroupWholeBan(int64_t groupid, CQBOOL enableban) {
    return CQ_setGroupWholeBan(g_authCode, groupid, enableban);
}

inline int32_t CQ_SetGroupAnonymousBan(int64_t groupid, const char *anomymous, int64_t duration) {
    return CQ_setGroupAnonymousBan(g_authCode, groupid, anomymous, duration);
}

inline int32_t CQ_SetGroupAnonymous(int64_t groupid, CQBOOL enableanomymous) {
    return CQ_setGroupAnonymous(g_authCode, groupid, enableanomymous);
}

inline int32_t CQ_SetGroupCard(int64_t groupid, int64_t QQID, const char *newcard) {
    return CQ_setGroupCard(g_authCode, groupid, QQID, newcard);
}

inline int32_t CQ_SetGroupLeave(int64_t groupid, CQBOOL isdismiss) {
    return CQ_setGroupLeave(g_authCode, groupid, isdismiss);
}

inline int32_t CQ_SetGroupSpecialTitle(int64_t groupid, int64_t QQID, const char *newspecialtitle, int64_t duration) {
    return CQ_setGroupSpecialTitle(g_authCode, groupid, QQID, newspecialtitle, duration);
}

inline int32_t CQ_SetDiscussLeave(int64_t discussid) {
    return CQ_setDiscussLeave(g_authCode, discussid);
}

inline int32_t CQ_SetFriendAddRequest(const char *responseflag, int32_t responseoperation, const char *remark) {
    return CQ_setFriendAddRequest(g_authCode, responseflag, responseoperation, remark);
}

inline int32_t CQ_SetGroupAddRequestV2(const char *responseflag, int32_t requesttype, int32_t responseoperation, const char *reason) {
    return CQ_setGroupAddRequestV2(g_authCode, responseflag, requesttype, responseoperation, reason);
}

inline const char *CQ_GetGroupMemberInfoV2(int64_t groupid, int64_t QQID, CQBOOL nocache) {
    return CQ_getGroupMemberInfoV2(g_authCode, groupid, QQID, nocache);
}

inline const char *CQ_GetGroupMemberList(int64_t groupid) {
    return CQ_getGroupMemberList(g_authCode, groupid);
}

inline const char *CQ_GetStrangerInfo(int64_t QQID, CQBOOL nocache) {
    return CQ_getStrangerInfo(g_authCode, QQID, nocache);
}

inline int32_t CQ_AddLog(int32_t priority, const char *category, const char *content) {
    return CQ_addLog(g_authCode, priority, category, content);
}

inline const char *CQ_GetCookies() {
    return CQ_getCookies(g_authCode);
}

inline int32_t CQ_GetCsrfToken() {
    return CQ_getCsrfToken(g_authCode);
}

inline int64_t CQ_GetLoginQQ() {
    return CQ_getLoginQQ(g_authCode);
}

inline const char *CQ_GetLoginNick() {
    return CQ_getLoginNick(g_authCode);
}

inline const char *CQ_GetAppDirectory() {
    return CQ_getAppDirectory(g_authCode);
}

inline int32_t CQ_SetFatal(const char *errorinfo) {
    return CQ_setFatal(g_authCode, errorinfo);
}

inline const char *CQ_GetRecord(const char *file, const char *outformat) {
    return CQ_getRecord(g_authCode, file, outformat);
}


class CQMutex
{
    HANDLE m_hMutex;
public:
    inline CQMutex(LPCTSTR lpName) {
        m_hMutex = ::CreateMutex(NULL, FALSE, lpName);
    }

    inline ~CQMutex() {
        ::CloseHandle(this->m_hMutex);
    }

    inline void Lock() {
        ::WaitForSingleObject(this->m_hMutex, INFINITE);
    }

    inline void UnLock() {
        ::ReleaseMutex(this->m_hMutex);
    }
};

class CQMutex_SDK
{
    CQMutex m_Mutex;
public:
    inline CQMutex_SDK() : m_Mutex(__SDK_MUTEX_NAME__.c_str()) {
        m_Mutex.Lock();
    }

    inline ~CQMutex_SDK() {
        m_Mutex.UnLock();
    }
};

class CQMutex_Event
{
    CQMutex m_Mutex;
public:
    inline CQMutex_Event() : m_Mutex(__EVT_MUTEX_NAME__.c_str()) {
        m_Mutex.Lock();
    }

    inline ~CQMutex_Event() {
        m_Mutex.UnLock();
    }
};

#define EVENT_EXCLUSIVE CQMutex_Event __evt_lock__
#define SDKCALL_EXCLUSIVE CQMutex_SDK __sdk_lock__


struct ICqHandler
{
    virtual int32_t OnEvent_Startup() = 0;
    virtual int32_t OnEvent_Exit() = 0;
    virtual int32_t OnEvent_Enable() = 0;
    virtual int32_t OnEvent_Disable() = 0;
    virtual int32_t OnEvent_PrivateMsg(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, int32_t font) = 0;
    virtual int32_t OnEvent_GroupMsg(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *fromAnonymous, const char *msg, int32_t font) = 0;
    virtual int32_t OnEvent_DiscussMsg(int32_t subType, int32_t sendTime, int64_t fromDiscuss, int64_t fromQQ, const char *msg, int32_t font) = 0;
    virtual int32_t OnEvent_System_GroupAdmin(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t beingOperateQQ) = 0;
    virtual int32_t OnEvent_System_GroupMemberDecrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) = 0;
    virtual int32_t OnEvent_System_GroupMemberIncrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) = 0;
    virtual int32_t OnEvent_Friend_Add(int32_t subType, int32_t sendTime, int64_t fromQQ) = 0;
    virtual int32_t OnEvent_Request_AddFriend(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, const char *responseFlag) = 0;
    virtual int32_t OnEvent_Request_AddGroup(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *msg, const char *responseFlag) = 0;
    virtual int32_t OnEvent_Menu(const char *index) = 0;
    virtual bool OnEvent_ReInit() = 0;
protected:
    int32_t m_authCode;
};


class Python27Mixin
{
protected:
    PyObject *m_PyHandler;

    Python27Mixin() : m_PyHandler(nullptr) { }

    virtual  ~Python27Mixin() { }

    bool initialize();
    void finalize();
};

class CqHandler_Python27 : public ICqHandler, public Python27Mixin
{
protected:
    bool m_enabled;
    static std::shared_ptr<ICqHandler> g_instance;//唯一实例
protected://私有化构造函数以便单例化本类
    CqHandler_Python27() : m_enabled(false), m_authCode(0) { }

    CqHandler_Python27(int32_t authCode) : CqHandler_Python27(), m_authCode(authCode) { }

public:
    ~CqHandler_Python27() override = default;
public:
    static std::shared_ptr<ICqHandler> GetPython27Handler(int32_t authCode);
public:
    int32_t OnEvent_Startup() override;
    int32_t OnEvent_Exit() override;
    int32_t OnEvent_Enable() override;
    int32_t OnEvent_Disable() override;
    int32_t OnEvent_PrivateMsg(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, int32_t font) override;
    int32_t OnEvent_GroupMsg(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *fromAnonymous, const char *msg, int32_t font) override;
    int32_t OnEvent_DiscussMsg(int32_t subType, int32_t sendTime, int64_t fromDiscuss, int64_t fromQQ, const char *msg, int32_t font) override;
    int32_t OnEvent_System_GroupAdmin(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t beingOperateQQ) override;
    int32_t OnEvent_System_GroupMemberDecrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) override;
    int32_t OnEvent_System_GroupMemberIncrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) override;
    int32_t OnEvent_Friend_Add(int32_t subType, int32_t sendTime, int64_t fromQQ) override;
    int32_t OnEvent_Request_AddFriend(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, const char *responseFlag) override;
    int32_t OnEvent_Request_AddGroup(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *msg, const char *responseFlag) override;
    int32_t OnEvent_Menu(const char *index = "") override;
    bool OnEvent_ReInit() override;

    void SetAuthCode(int32_t authCode) { m_authCode = authCode; }
};

#endif //PROJECT_DAMOCLES_CQPYHANDLERWRAPPER_H
