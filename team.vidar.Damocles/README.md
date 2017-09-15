###  目录结构

*  本目录存放released插件native部分（发布时按此目录结构复制到插件根目录下）



```
.
├── team.vidar.Damocles					# Plugin dir
│   ├── CQGroupMemberInfo.py
│   ├── CQGroupMemberListInfo.py
│   ├── CQHandler.py					# Python layer plugin implement
│   ├── CQPack.py
│   ├── CQSDK.py						# Python layer SDK wrapper
│   ├── CQStrangerInfo.py
│   ├── Python27						# Stand-alone python runtime
│   │   ├── DLLs
│   │   │   ├── _bsddb.pyd
│   │   │   ├── bz2.pyd
│   │   │   ├── _ctypes.pyd
│   │   │   ├── _ctypes_test.pyd
│   │   │   ├── _elementtree.pyd
│   │   │   ├── _hashlib.pyd
│   │   │   ├── _msi.pyd
│   │   │   ├── _multiprocessing.pyd
│   │   │   ├── pyexpat.pyd
│   │   │   ├── select.pyd
│   │   │   ├── _socket.pyd
│   │   │   ├── sqlite3.dll
│   │   │   ├── _sqlite3.pyd
│   │   │   ├── _ssl.pyd
│   │   │   ├── tcl85.dll
│   │   │   ├── tclpip85.dll
│   │   │   ├── _testcapi.pyd
│   │   │   ├── tk85.dll
│   │   │   ├── _tkinter.pyd
│   │   │   ├── unicodedata.pyd
│   │   │   └── winsound.pyd
│   │   ├── Microsoft.VC90.CRT.manifest
│   │   ├── msvcr90.dll
│   │   ├── python27.dll
│   │   └── python27.zip
│   └── README.md
├── team.vidar.Damocles.dll				# Native layer dll
└── team.vidar.Damocles.json			# Plugin json
```

