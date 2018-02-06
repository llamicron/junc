import unittest
import os
import sys
import json

from terminaltables import AsciiTable
from docopt import docopt

from .. import Junc
from ..storage import Storage

class TestJunc(unittest.TestCase):
    def setUp(self):
        self.test_file = os.path.join(os.path.expanduser('~'), '.junc.json.test')
        open(self.test_file, 'w')
        self.junc = Junc(jsonfile=self.test_file)

    def tearDown(self):
        os.truncate(self.test_file, 0)

    def seed_server_list(self):
        servers = [
            {
                "username": "pi",
                "ip": "192.168.0.134",
                "name": "sween",
                "location": "Dining Room"
            },
            {
                "username": "pi",
                "ip": "192.168.0.169",
                "name": "brewpi-prod",
                "location": "Brew Rig"
            }
        ]
        with open(self.test_file, 'w'):
            file.write(json.dumps(servers))

    def test_it_has_a_file_with_a_default(self):
        default = os.path.join(os.path.expanduser('~'), '.junc.json')
        new = os.path.join(os.path.expanduser('~'), '.junc.json.test')
        junc = Junc()
        assert junc.jsonfile == default

        junc = Junc(jsonfile=new)
        assert junc.jsonfile == new

    def test_get_server_list(self):
        # File is empty right now
        assert self.junc.get_servers() == []
