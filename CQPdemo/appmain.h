#define CQAPPID "pw.libc.Damocles" //请修改AppID
#define CQAPPINFO CQAPIVERTEXT "," CQAPPID

#include "CqPyHandlerWrapper.h"

#define DEVELOPER_QQ (407508177)

extern int32_t g_authCode;
extern std::shared_ptr<ICqHandler> g_CqHandler;