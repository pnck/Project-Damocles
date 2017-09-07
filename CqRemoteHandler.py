#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import sys
import xmlrpclib
import traceback
import ssl

server = xmlrpclib.ServerProxy('https://116.196.104.11:1337',context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))
try:
    if not server.echo('try echo') == 'try echo':
        raise xmlrpclib.Fault(-1,'Try echo method failed, server invalid.')
except xmlrpclib.Fault,e:
    traceback.print_exc()
    print('__________________')
    print(e.faultString)
    sys.exit()
except Exception:
    traceback.print_exc()
    print('-------------NOT GOOD----------')
    sys.exit()

print('Available methods:'+str(server.system.listMethods()))