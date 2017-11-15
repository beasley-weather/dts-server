import zmq


_context = zmq.Context()


class IPC_Client:
    ACK = bytes.fromhex('06')

    def __init__(self, sock_addr):
        self._sock_addr = sock_addr
        self._sock = _context.socket(zmq.REQ)

    def __enter__(self):
        self._sock.connect(self._sock_addr)

    def __exit__(self, *args):
        self._sock.disconnect(self._sock_addr)

    def transfer(self, data):
        '''
        :param data: Data to transfer
        :type data: bytes
        '''
        self._sock.send(data)
        resp = self._sock.recv()
        if (resp != self.ACK):
            # todo error handling, perhaps cache data temporarily, or throw exception
            pass
