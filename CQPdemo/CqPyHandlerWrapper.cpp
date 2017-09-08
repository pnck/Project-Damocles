//
// Created by pcnk on 9/8/17.
//

#include "CqPyHandlerWrapper.h"


std::string PyString_AsString_Ex(PyObject *s) {
    std::string ret;
    if (PyString_Check(s)) {
        ret = std::string(PyString_AsString(s));
    }
    return ret;
}

int PyTuple_SetItem(PyObject *tuple, Py_ssize_t index, int32_t v) {
    return PyTuple_SetItem(tuple, index, PyLong_FromLong(v));
}

int PyTuple_SetItem(PyObject *tuple, Py_ssize_t index, int64_t v) {
    return PyTuple_SetItem(tuple, index, PyLong_FromLongLong(v));
}

int PyTuple_SetItem(PyObject *tuple, Py_ssize_t index, const char *v) {
    return PyTuple_SetItem(tuple, index, PyString_FromString(v));
}

PyObject *PyObject_GetAttrString_Ex(PyObject *o, const char *name) {
    if (o) {
        return PyObject_GetAttrString(o, name);
    }
    return NULL;
}
//////////////////////////////////////////////////////////////////////////



#pragma region CQSDK Functions


static PyObject *CQSDK_MessageBox(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    CQ_MessageBox(
            PyString_AsString_Ex(arg0).c_str(),
            PyString_AsString_Ex(arg1).c_str()
    );

    return Py_BuildValue("");
}

static PyObject *CQSDK_GetAppID(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    const char *ret = CQ_GetAppID();

    return PyString_FromString(ret);
}

static PyObject *CQSDK_SendPrivateMsg(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SendPrivateMsg(
            PyLong_AsLongLong(arg0),
            PyString_AsString_Ex(arg1).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SendGroupMsg(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SendGroupMsg(
            PyLong_AsLongLong(arg0),
            PyString_AsString_Ex(arg1).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SendDiscussMsg(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SendDiscussMsg(
            PyLong_AsLongLong(arg0),
            PyString_AsString_Ex(arg1).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SendLike(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);

    int32_t ret = CQ_SendLike(
            PyLong_AsLongLong(arg0)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupKick(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetGroupKick(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyLong_AsLong(arg2)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupBan(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetGroupBan(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyLong_AsLongLong(arg2)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupAdmin(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetGroupAdmin(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyLong_AsLong(arg2)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupWholeBan(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SetGroupWholeBan(
            PyLong_AsLongLong(arg0),
            PyLong_AsLong(arg1)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupAnonymousBan(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetGroupAnonymousBan(
            PyLong_AsLongLong(arg0),
            PyString_AsString_Ex(arg1).c_str(),
            PyLong_AsLongLong(arg2)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupAnonymous(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SetGroupAnonymous(
            PyLong_AsLongLong(arg0),
            PyLong_AsLong(arg1)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupCard(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetGroupCard(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyString_AsString_Ex(arg2).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupLeave(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    int32_t ret = CQ_SetGroupLeave(
            PyLong_AsLongLong(arg0),
            PyLong_AsLong(arg1)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupSpecialTitle(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);
    PyObject *arg3 = PyTuple_GetItem(args, 3);

    int32_t ret = CQ_SetGroupSpecialTitle(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyString_AsString_Ex(arg2).c_str(),
            PyLong_AsLongLong(arg3)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetDiscussLeave(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);

    int32_t ret = CQ_SetDiscussLeave(
            PyLong_AsLongLong(arg0)
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetFriendAddRequest(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_SetFriendAddRequest(
            PyString_AsString_Ex(arg0).c_str(),
            PyLong_AsLong(arg1),
            PyString_AsString_Ex(arg2).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_SetGroupAddRequestV2(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);
    PyObject *arg3 = PyTuple_GetItem(args, 3);

    int32_t ret = CQ_SetGroupAddRequestV2(
            PyString_AsString_Ex(arg0).c_str(),
            PyLong_AsLong(arg1),
            PyLong_AsLong(arg2),
            PyString_AsString_Ex(arg3).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_GetGroupMemberInfoV2(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    const char *ret = CQ_GetGroupMemberInfoV2(
            PyLong_AsLongLong(arg0),
            PyLong_AsLongLong(arg1),
            PyLong_AsLong(arg2)
    );

    return Py_BuildValue("s", ret);
}

static PyObject *CQSDK_GetGroupMemberList(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);

    const char *ret = CQ_GetGroupMemberList(
            PyLong_AsLongLong(arg0)
    );

    return Py_BuildValue("s", ret);
}

static PyObject *CQSDK_GetStrangerInfo(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);

    const char *ret = CQ_GetStrangerInfo(
            PyLong_AsLongLong(arg0),
            PyLong_AsLong(arg1)
    );

    return Py_BuildValue("s", ret);
}

static PyObject *CQSDK_AddLog(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);
    PyObject *arg1 = PyTuple_GetItem(args, 1);
    PyObject *arg2 = PyTuple_GetItem(args, 2);

    int32_t ret = CQ_AddLog(
            PyLong_AsLong(arg0),
            PyString_AsString_Ex(arg1).c_str(),
            PyString_AsString_Ex(arg2).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_GetCookies(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    const char *ret = CQ_GetCookies();

    return Py_BuildValue("s", ret);
}

static PyObject *CQSDK_GetCsrfToken(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    int32_t ret = CQ_GetCsrfToken();

    return Py_BuildValue("i", ret);
}

static PyObject *CQSDK_GetLoginQQ(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    int64_t ret = CQ_GetLoginQQ();

    return Py_BuildValue("L", ret);
}

static PyObject *CQSDK_GetLoginNick(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    const char *ret = CQ_GetLoginNick();

    return Py_BuildValue("s", ret);
}

static PyObject *CQSDK_GetAppDirectory(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    const char *ret = CQ_GetAppDirectory();

    return PyString_FromString(ret);
}

static PyObject *CQSDK_SetFatal(PyObject *self, PyObject *args) {
    SDKCALL_EXCLUSIVE;

    PyObject *arg0 = PyTuple_GetItem(args, 0);

    int32_t ret = CQ_SetFatal(
            PyString_AsString_Ex(arg0).c_str()
    );

    return Py_BuildValue("i", ret);
}

static PyMethodDef CQSDK_funcs[] =
        {
                {"MessageBox",           (PyCFunction) CQSDK_MessageBox,           METH_VARARGS, NULL},
                {"GetAppID",             (PyCFunction) CQSDK_GetAppID,             METH_VARARGS, NULL},
                {"SendPrivateMsg",       (PyCFunction) CQSDK_SendPrivateMsg,       METH_VARARGS, NULL},
                {"SendGroupMsg",         (PyCFunction) CQSDK_SendGroupMsg,         METH_VARARGS, NULL},
                {"SendDiscussMsg",       (PyCFunction) CQSDK_SendDiscussMsg,       METH_VARARGS, NULL},
                {"SendLike",             (PyCFunction) CQSDK_SendLike,             METH_VARARGS, NULL},
                {"SetGroupKick",         (PyCFunction) CQSDK_SetGroupKick,         METH_VARARGS, NULL},
                {"SetGroupBan",          (PyCFunction) CQSDK_SetGroupBan,          METH_VARARGS, NULL},
                {"SetGroupAdmin",        (PyCFunction) CQSDK_SetGroupAdmin,        METH_VARARGS, NULL},
                {"SetGroupWholeBan",     (PyCFunction) CQSDK_SetGroupWholeBan,     METH_VARARGS, NULL},
                {"SetGroupAnonymousBan", (PyCFunction) CQSDK_SetGroupAnonymousBan, METH_VARARGS, NULL},
                {"SetGroupAnonymous",    (PyCFunction) CQSDK_SetGroupAnonymous,    METH_VARARGS, NULL},
                {"SetGroupCard",         (PyCFunction) CQSDK_SetGroupCard,         METH_VARARGS, NULL},
                {"SetGroupLeave",        (PyCFunction) CQSDK_SetGroupLeave,        METH_VARARGS, NULL},
                {"SetGroupSpecialTitle", (PyCFunction) CQSDK_SetGroupSpecialTitle, METH_VARARGS, NULL},
                {"SetDiscussLeave",      (PyCFunction) CQSDK_SetDiscussLeave,      METH_VARARGS, NULL},
                {"SetFriendAddRequest",  (PyCFunction) CQSDK_SetFriendAddRequest,  METH_VARARGS, NULL},
                {"SetGroupAddRequestV2", (PyCFunction) CQSDK_SetGroupAddRequestV2, METH_VARARGS, NULL},
                {"GetGroupMemberInfoV2", (PyCFunction) CQSDK_GetGroupMemberInfoV2, METH_VARARGS, NULL},
                {"GetGroupMemberList",   (PyCFunction) CQSDK_GetGroupMemberList,   METH_VARARGS, NULL},
                {"GetStrangerInfo",      (PyCFunction) CQSDK_GetStrangerInfo,      METH_VARARGS, NULL},
                {"AddLog",               (PyCFunction) CQSDK_AddLog,               METH_VARARGS, NULL},
                {"GetCookies",           (PyCFunction) CQSDK_GetCookies,           METH_VARARGS, NULL},
                {"GetCsrfToken",         (PyCFunction) CQSDK_GetCsrfToken,         METH_VARARGS, NULL},
                {"GetLoginQQ",           (PyCFunction) CQSDK_GetLoginQQ,           METH_VARARGS, NULL},
                {"GetLoginNick",         (PyCFunction) CQSDK_GetLoginNick,         METH_VARARGS, NULL},
                {"GetAppDirectory",      (PyCFunction) CQSDK_GetAppDirectory,      METH_VARARGS, NULL},
                {"SetFatal",             (PyCFunction) CQSDK_SetFatal,             METH_VARARGS, NULL},
                {NULL, NULL, 0,                                                                  NULL}
        };

#pragma endregion


bool Python27Mixin::initialize() {
#if 0
    os_delpuv("PYTHONDEBUG");
    os_delpuv("PYTHONHOME");
    os_delpuv("PYTHONOPTIMIZE");
    os_delpuv("PYTHONPATH");
    os_delpuv("PYTHONVERBOSE");

    std::string app_home = CQ_GetAppDirectory();
    std::string app_python_home = path_join(str_list(app_home, "Python27"));

    std::vector<std::string> sys_path_list;
    sys_path_list.push_back(app_python_home);
    sys_path_list.push_back(path_join(str_list(app_python_home, "DLLs")));
    sys_path_list.push_back(os_getenv("PATH"));
    os_putenv("PATH", str_join(";", sys_path_list));

    std::vector<std::string> python_path_list;

    std::string cqhandler_home = str_strip(os_getenv("CQHANDLER_HOME"));
    if (!cqhandler_home.empty()) {
        python_path_list.push_back(cqhandler_home);
    }

    python_path_list.push_back(app_home);
    python_path_list.push_back(path_join(str_list(app_home, "CQHandler.zip")));
    python_path_list.push_back(path_join(str_list(app_python_home, "python27.zip")));
    python_path_list.push_back(path_join(str_list(app_python_home, "Lib")));
    python_path_list.push_back(path_join(str_list(app_python_home, "DLLs")));
    python_path_list.push_back(app_python_home);

    os_putenv("PYTHONHOME", app_python_home);
    os_putenv("PYTHONPATH", str_join(";", python_path_list));

    if (FAILED(__HrLoadAllImportsForDll("python27.dll"))) {
        ::MessageBoxA(NULL, "__HrLoadAllImportsForDll Failed", "", MB_OK);
        return false;
    }
#else
    Py_SetPythonHome("C:\\python27");
#endif
    Py_Initialize();
    Py_InitModule3("_CQSDK", CQSDK_funcs, NULL);
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:\\modules')");

    int32_t ret = 0;

    do {
#define BREAK_IF_NULL(var, msg) if (NULL == (var)) { ::MessageBox(NULL, msg, "error", MB_OK); return false; }


        PyObject *m = PyImport_ImportModule("CQHandler");
        BREAK_IF_NULL(m, "Import CQHandler Module Failed")

        PyObject *d = PyModule_GetDict(m);

        PyObject *c = PyDict_GetItemString(d, "CQHandler");
        BREAK_IF_NULL(c, "Load CQHandler Class Failed")

        m_PyHandler = PyObject_CallObject(c, NULL);
        BREAK_IF_NULL(m_PyHandler, "Create CQHandler Instance Failed")

        Py_XDECREF(c);
        Py_XDECREF(d);
        Py_XDECREF(m);
    } while (false);

    return true;
}

void Python27Mixin::finalize() {
    Py_XDECREF(m_PyHandler);
    m_PyHandler = NULL;
    Py_Finalize();
    //__FUnloadDelayLoadedDLL2("python27.dll");
}

int32_t CqHandler_Python27::OnEvent_Startup() {
    EVENT_EXCLUSIVE;
    return 0;
}

int32_t CqHandler_Python27::OnEvent_Exit() {
    EVENT_EXCLUSIVE;
    return 0;
}

int32_t CqHandler_Python27::OnEvent_Enable() {
    m_enabled = true;
    int32_t ret = 0;

    if (this->initialize()) {
        PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_Enable");
        if (f) {
            PyObject *r = PyObject_CallObject(f, NULL);
            ret = PyLong_AsLong(r);
            Py_XDECREF(r);
            Py_XDECREF(f);
        }
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_Disable() {
    EVENT_EXCLUSIVE;
    int32_t ret = 0;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_Disable");
    if (f) {
        PyObject *r = PyObject_CallObject(f, NULL);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    this->finalize();
    this->m_enabled = false;
    return ret;
}

int32_t CqHandler_Python27::OnEvent_PrivateMsg(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, int32_t font) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_PrivateMsg");
    if (f) {
        PyObject *args = PyTuple_New(5);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromQQ);
        PyTuple_SetItem(args, 3, msg);
        PyTuple_SetItem(args, 4, font);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }

    return ret;

}

int32_t CqHandler_Python27::OnEvent_GroupMsg(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *fromAnonymous, const char *msg, int32_t font) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_GroupMsg");
    if (f) {
        PyObject *args = PyTuple_New(7);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromGroup);
        PyTuple_SetItem(args, 3, fromQQ);
        PyTuple_SetItem(args, 4, fromAnonymous);
        PyTuple_SetItem(args, 5, msg);
        PyTuple_SetItem(args, 6, font);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }

    return ret;
}

int32_t CqHandler_Python27::OnEvent_DiscussMsg(int32_t subType, int32_t sendTime, int64_t fromDiscuss, int64_t fromQQ, const char *msg, int32_t font) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_DiscussMsg");
    if (f) {
        PyObject *args = PyTuple_New(6);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromDiscuss);
        PyTuple_SetItem(args, 3, fromQQ);
        PyTuple_SetItem(args, 4, msg);
        PyTuple_SetItem(args, 5, font);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }

    return ret;
}

int32_t CqHandler_Python27::OnEvent_System_GroupAdmin(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t beingOperateQQ) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_System_GroupAdmin");
    if (f) {
        PyObject *args = PyTuple_New(4);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromGroup);
        PyTuple_SetItem(args, 3, beingOperateQQ);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }

    return ret;
}

int32_t CqHandler_Python27::OnEvent_System_GroupMemberDecrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) {
    EVENT_EXCLUSIVE;

    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_System_GroupMemberDecrease");
    if (f) {
        PyObject *args = PyTuple_New(5);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromGroup);
        PyTuple_SetItem(args, 3, fromQQ);
        PyTuple_SetItem(args, 4, beingOperateQQ);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_System_GroupMemberIncrease(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, int64_t beingOperateQQ) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_System_GroupMemberIncrease");
    if (f) {
        PyObject *args = PyTuple_New(5);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromGroup);
        PyTuple_SetItem(args, 3, fromQQ);
        PyTuple_SetItem(args, 4, beingOperateQQ);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_Friend_Add(int32_t subType, int32_t sendTime, int64_t fromQQ) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_Friend_Add");
    if (f) {
        PyObject *args = PyTuple_New(3);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromQQ);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_Request_AddFriend(int32_t subType, int32_t sendTime, int64_t fromQQ, const char *msg, const char *responseFlag) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_Request_AddFriend");
    if (f) {
        PyObject *args = PyTuple_New(5);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromQQ);
        PyTuple_SetItem(args, 3, msg);
        PyTuple_SetItem(args, 4, responseFlag);

        PyObject *r = PyObject_CallObject(f, NULL);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_Request_AddGroup(int32_t subType, int32_t sendTime, int64_t fromGroup, int64_t fromQQ, const char *msg, const char *responseFlag) {
    EVENT_EXCLUSIVE;
    int32_t ret = EVENT_IGNORE;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, "OnEvent_Request_AddGroup");
    if (f) {
        PyObject *args = PyTuple_New(6);
        PyTuple_SetItem(args, 0, subType);
        PyTuple_SetItem(args, 1, sendTime);
        PyTuple_SetItem(args, 2, fromGroup);
        PyTuple_SetItem(args, 3, fromQQ);
        PyTuple_SetItem(args, 4, msg);
        PyTuple_SetItem(args, 5, responseFlag);

        PyObject *r = PyObject_CallObject(f, args);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

int32_t CqHandler_Python27::OnEvent_Menu(const char *index) {
    EVENT_EXCLUSIVE;
    int32_t ret = 0;
    PyObject *f = PyObject_GetAttrString_Ex(m_PyHandler, str_join(str_list("OnEvent_Menu", index)).c_str());
    if (f) {
        PyObject *r = PyObject_CallObject(f, NULL);
        ret = PyLong_AsLong(r);
        Py_XDECREF(r);
        Py_XDECREF(f);
    }
    return ret;
}

bool CqHandler_Python27::OnEvent_ReInit() {
    SDKCALL_EXCLUSIVE;
    EVENT_EXCLUSIVE;
    bool ret = false;
    finalize();
    ret = initialize();
    return ret;
}

static std::shared_ptr<ICqHandler> CqHandler_Python27::g_instance = nullptr;//唯一实例

std::shared_ptr<ICqHandler> CqHandler_Python27::GetPython27Handler(int32_t authCode) {
    EVENT_EXCLUSIVE;
    SDKCALL_EXCLUSIVE;
    if (!g_instance) {
        struct __CqHandlerExposeConstructor final : public CqHandler_Python27 { };
        g_instance = std::make_shared<__CqHandlerExposeConstructor>(authCode);
    }
    return g_instance;
}
