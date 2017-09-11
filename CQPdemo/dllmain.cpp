// dllmain.cpp : Defines the entry point for the DLL application.
#include "stdafx.h"
#include "utils.h"
#include "cqp.h"


std::string __CQ_APPID__;
std::string __CQ_APPINFO__;
std::string __EVT_MUTEX_NAME__;
std::string __SDK_MUTEX_NAME__;


BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
					 )
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		__CQ_APPID__ = path_splitext(path_basename(os_getmodulefilename(hModule)))[0];
        __CQ_APPINFO__ = str_join(str_list(CQAPIVERTEXT, ",", __CQ_APPID__));
        __EVT_MUTEX_NAME__ = str_join(str_list("CQHandler.Mutex.EVT", "@", __CQ_APPID__));
        __SDK_MUTEX_NAME__ = str_join(str_list("CQHandler.Mutex.SDK", "@", __CQ_APPID__));
	case DLL_THREAD_ATTACH:
	case DLL_THREAD_DETACH:
	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}

