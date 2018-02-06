import unittest

from docopt import docopt
from terminaltables import AsciiTable

from .. import Junc, __doc__ as doc

class TestJunc(unittest.TestCase):
    def setUp(self):
        self.junc = Junc(testing = True)

    def test_list_servers(self):
        args = docopt(doc, ['list'])
        results = self.junc.what_to_do_with(args)

        assert type(results) is AsciiTable

        args = docopt(doc, ['list', '--json'])
        results = self.junc.what_to_do_with(args)

        print(results)
        assert type(results) is str

    def test_new_server(self):
        args = docopt(doc, ['add', 'server-name', 'username', '123.456.789', 'right here'])
        server = self.junc.new_server(args)
        assert type(server) is dict
        for item in ['name', 'username', 'ip', 'location']:
            assert item in server.keys()
            assert type(server[item]) is str

    # def test_add(self):
    #     old_size = len(self.junc.servers)
    #     self.junc.add()
