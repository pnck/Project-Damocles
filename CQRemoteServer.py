#!/usr/bin/env python3
#coding:utf8
import sys
import socketserver
import ssl
import xmlrpc.server
try:
    import fcntl
except ImportError:
    fcntl = None

import logging
logging.basicConfig(
    level       = logging.INFO,
    format      = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S',
    filename    = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Server_CQHanlder.log'),
    filemode    = 'w+'
)


CERTFILE = 'cert.pem'
KEYFILE = 'key.pem'

class SecureXMLRPCServer(socketserver.ThreadingTCPServer,xmlrpc.server.SimpleXMLRPCDispatcher):
    allow_reuse_address = True
    def __init__(self, addr, certfile, keyfile=None,
            requestHandler=xmlrpc.server.SimpleXMLRPCRequestHandler,
            logRequests=True, allow_none=False, encoding=None, 
            bind_and_activate=True, ssl_version=ssl.PROTOCOL_TLSv1):
        self.logRequests = logRequests

        # create an SSL context
        self.context = ssl.SSLContext(ssl_version)
        self.context.load_cert_chain(certfile=certfile, keyfile=keyfile)

        xmlrpc.server.SimpleXMLRPCDispatcher.__init__(self, allow_none, 
                encoding)
        # call TCPServer constructor
        socketserver.TCPServer.__init__(self, addr, requestHandler, bind_and_activate)

        if fcntl is not None and hasattr(fcntl, 'FD_CLOEXEC'):
            flags = fcntl.fcntl(self.fileno(), fcntl.F_GETFD)
            flags |= fcntl.FD_CLOEXEC
            fcntl.fcntl(self.fileno(), fcntl.F_SETFD, flags)

    def get_request(self):
        newsocket, fromaddr = self.socket.accept()
        # create an server-side SSL socket
        sslsocket = self.context.wrap_socket(newsocket, server_side=True)
        return sslsocket, fromaddr

class CQRemoteHandlerImplement:
    def echo(self,s):
        return s

    def handle_OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def handle_OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def handle_OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(subType, sendTime, fromQQ, msg, font))

    def handle_OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))
        if msg.find('[SERVER]') >= 0:
            return ''' CQSDK.SendGroupMsg(fromGroup,'[CQ:at,qq=%d] action from server') '''


    def handle_OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def handle_OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(subType, sendTime, fromGroup, beingOperateQQ))

    def handle_OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def handle_OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def handle_OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(subType, sendTime, fromQQ))

    def handle_OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(subType, sendTime, fromQQ, msg, responseFlag))

    def handle_OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def handle_OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def handle_OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def handle_OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')


if __name__ == '__main__':
    cqServer = SecureXMLRPCServer(('0.0.0.0',1337),certfile=CERTFILE,keyfile=KEYFILE)
    cqServer.register_introspection_functions()
    cqServer.register_instance(CQRemoteHandlerImplement(),allow_dotted_names=True)
    cqServer.register_multicall_functions()
    print('__Server started__')
    try:
        cqServer.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
