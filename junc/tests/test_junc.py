import unittest
import sys

from terminaltables import AsciiTable
from docopt import docopt

from .. import junc
from ..storage import Storage

class TestJunc(unittest.TestCase):
    def setUp(self):
        self.sv_list = [
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
        self.st = Storage()

    def test_list_tables(self):
        table = junc.list_tables(self.sv_list, self.st)
        assert type(table) is AsciiTable

        raw_list = junc.list_tables(self.sv_list, self.st, json_format = True)
        assert type(raw_list) is list


