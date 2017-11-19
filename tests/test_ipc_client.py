import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from dts_server.ipc_client import IPC_Client


class TEST_IPC_CLIENT(unittest.TestCase):
    def setUp(self):
        def connect_mock(address):
            self.assertEqual(address, self.expected_address)
        self.connect_mock = connect_mock

        def disconnect_mock(address):
            self.assertEqual(address, self.expected_address)
        self.disconnect_mock = disconnect_mock

        def send_mock(data):
            self.assertEqual(data, self.expected_data)
        self.send_mock = send_mock

        def recv_mock():
            return bytes.fromhex('06')
        self.recv_mock = recv_mock

        def recv_fail_mock():
            return bytes()
        self.recv_fail_mock = recv_fail_mock

        self.expected_address = 'tcp://127.0.0.1:44444'
        self.expected_data = b'hello world'

        self.setUp_IPC_Client()

    # new field is required to ensure no additional arg is passed to method
    @patch('dts_server.ipc_client._context', new=MagicMock())
    def setUp_IPC_Client(self):
        self.ipc_client = IPC_Client(self.expected_address)
        self.ipc_client._sock = MagicMock()
        self.ipc_client._sock.connect.side_effect = self.connect_mock
        self.ipc_client._sock.disconnect.side_effect = self.disconnect_mock
        self.ipc_client._sock.send.side_effect = self.send_mock
        self.ipc_client._sock.recv.side_effect = self.recv_mock

    def test___enter___and___exit__(self):
        '''
        Ensure connect and disconnect are called on zmq socket
        '''
        with self.ipc_client:
            pass

    def test_transfer(self):
        with self.ipc_client:
            self.ipc_client.transfer(self.expected_data)

    def test_transfer_fail(self):
        self.ipc_client._sock.recv.side_effect = self.recv_fail_mock
        with self.ipc_client:
            self.assertRaises(Exception, self.ipc_client.transfer, self.expected_data)
