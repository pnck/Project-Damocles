// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#define WIN32_LEAN_AND_MEAN             // Exclude rarely-used stuff from Windows headers
// Windows Header Files:
#include <windows.h>

#include <string>

#include <delayimp.h>
#pragma comment(lib, "Delayimp.lib")

extern std::string __CQ_APPID__;
extern std::string __CQ_APPINFO__;
extern std::string __EVT_MUTEX_NAME__;
extern std::string __SDK_MUTEX_NAME__;


// TODO: reference additional headers your program requires here
#include "stdint.h"
#include "string"