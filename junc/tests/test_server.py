import unittest

from ..server import _Server

class TestServer(unittest.TestCase):
    def test_serialize_server_to_another(self):
        ser1 = _Server({
            'name': 'sween',
            'username': 'pi',
            'ip': '192.168.0.134',
            'location': 'Dining Room'
        })
        print(ser1)
        assert type(ser1) is _Server
        ser2 = _Server(ser1.__dict__)
        assert type(ser2) is _Server
