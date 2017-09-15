# -*- coding:gbk -*-

import base64
from CQPack import CQUnpack
from CQGroupMemberInfo import CQGroupMemberInfo

def GetGroupMemberListInfo(data):
    memList = []
    
    data = base64.decodestring(data)
    info = CQUnpack(data)
    count = info.GetInt()
    while count:
        if info.Len() <= 0:
            break
        retData = info.GetLenStr()
        memInfo = CQGroupMemberInfo(retData,False)
        memList.append(memInfo)
    
    return memList        
        

'''
EXAMPLE:

from CQGroupMemberInfo import CQGroupMemberInfo
info = CQGroupMemberInfo(CQSDK.GetGroupMemberInfoV2(fromGroup, fromQQ))
'''