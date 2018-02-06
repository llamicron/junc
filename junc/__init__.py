"""
Usage:
    junc list [--json]
    junc connect <name>
    junc add [(<name> <username> <ip>)] [<location>]
    junc remove <name>
    junc backup [<file>]
    junc restore [<file>]

Options:
    -h --help     Show this screen.
    --version     Show version.
    --json        Output server list as JSON instead of a (readable) table

Arguments:
    name          Human-readable name of a server
    username      Username you wish to login with
    ip            The IP of the server
    location      (Optional) Where the server is located (useful for headless machines ie. raspberry pi)
    file          A backup is created at (or restored from) this location (default: ~/.junc.json.bak)

Notes:
    Data is stored in ~/.junc.json
    Default backup location is ~/.junc.json.bak
"""

import os
import json

from docopt import docopt
from terminaltables import AsciiTable

try:
    from storage import Storage
except ImportError:
    from .storage import Storage

class Junc(object):
    def __init__(self, testing = False):
        self.st = Storage(testing=testing)

        self.servers = self.st.get_servers()

    def what_to_do_with(self, args):
        """
        Inteprets the docopt argument vector and does something cool with it
        """
        if args['list']:
            return self.list_servers(raw=args['--json'])

    def list_servers(self, raw=False):
        if raw:
            return json.dumps(self.servers)
        else:
            return self.get_server_table()

    def new_server(self, args):
        # Don't have to validate, docopt does that for us
        attrs = ['<ip>', '<username>', '<name>', '<location>']
        new_server = {}
        for attr in attrs:
            new_server[attr[1:-1]] = args[attr]
        return new_server

    def get_server_table(self):
        """
        Gets all the servers and plops them into a terminal table
        """
        table_data = [
            ['Name', "Address", "Location"],
        ]
        if not self.servers:
            table_data.append(["No Servers yet :(\nAdd some!"])
        else:
            for server in self.servers:
                table_data.append(
                    [server['name'], server['username'] + "@" + server['ip'], server['location']])
        return AsciiTable(table_data)

if __name__ == '__main__':
    args = docopt(__doc__)
    junc = Junc()
    results = junc.what_to_do_with(args)
    if type(results) is AsciiTable:
        print(results.table)
    else:
        print(results)

