import unittest
from os import remove
from os.path import isfile, join, expanduser
import json

from docopt import docopt
from terminaltables import AsciiTable

from .. import Junc, __doc__ as doc

class TestJunc(unittest.TestCase):
    def setUp(self):
        self.junc = Junc(testing = True)
        self.seed_test_file()
        self.junc.get_servers()

    def tearDown(self):
        # Files that may be created during testing
        base_path = join(expanduser('~'), '.junc.json.test')
        files = [
            base_path,
            base_path + '.bak',
            base_path + '.custom_bak',
        ]
        for fi in files:
            if isfile(fi):
                remove(fi)

    def seed_test_file(self):
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
        with open(self.junc.st.file_path, 'w') as fi:
            fi.write(json.dumps(servers))

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

    def test_add_server_CLI(self):
        old_length = len(self.junc.servers)
        args = docopt(doc, ['add', 'server-name', 'username', '123.456.789', 'Pytest :)'])
        self.junc.what_to_do_with(args)
        assert len(self.junc.servers) == old_length + 1



    def test_add_server_directly(self):
        """
        Uses the add_server() method, not through the CLI
        """
        old_length = len(self.junc.servers)
        new_server = {
            "name": "another_server",
            "ip": "192.168.0.169",
            "username": "username",
            "location": "Pytest :)"
        }

        self.junc.add_server(new_server)
        assert len(self.junc.servers) == old_length + 1


    def test_remove_server(self):
        servers = [
            {
                'name': 'to_remove',
                'ip': '19213.1235',
                'username': 'doesnt matter',
                'location': 'this really doesnt matter'
            },
            {
                'name': 'another one',
                'ip': '19213.1235',
                'username': 'doesnt matter',
                'location': 'this really doesnt matter'
            }
        ]
        self.junc.servers = servers
        self.junc.save()
        old_size = len(self.junc.st.get_servers())
        args = docopt(doc, ['remove', 'to_remove'])
        self.junc.what_to_do_with(args)

        assert len(self.junc.st.get_servers()) == old_size - 1

    def test_backup_and_restore_with_custom_location(self):
        fi = self.junc.st.file_path
        custom_fi = fi + '.custom_bak'

        assert isfile(fi)
        assert not isfile(custom_fi)

        args = docopt(doc, ['backup', custom_fi])
        self.junc.what_to_do_with(args)

        assert isfile(custom_fi)
        remove(fi)
        assert not isfile(fi)

        args = docopt(doc, ['restore', custom_fi])
        self.junc.what_to_do_with(args)

        assert isfile(custom_fi)
        assert isfile(fi)

    def test_restore(self):
        fi = self.junc.st.file_path

        assert not isfile(fi + '.bak')

        args = docopt(doc, ['backup'])
        self.junc.what_to_do_with(args)

        assert isfile(fi)
        assert isfile(fi + '.bak')

        remove(fi)
        assert not isfile(fi)

        args = docopt(doc, ['restore'])
        self.junc.what_to_do_with(args)

        assert isfile(fi)
        assert isfile(fi + '.bak')

    def test_similarities(self):
        new_server = {
            "name": "brewpi-prod",  # This name exists in the seed data
            "ip": "192.168.0.169",
            "username": "pi",      # So does this username + ip combination
            "location": "Pytest :)"
        }
        assert self.junc.find_similar_server(new_server) == ['name', 'address']
