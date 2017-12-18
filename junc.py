"""
Usage:
    junc connect <connect_to>
    junc list
    junc add [(<name> <username> <ip> <location>)]
    junc remove [<name>]

Options:
    -h --help     Show this screen.
    --version     Show version.

Notes:
    Data is stored in ~/.junc.json
"""

VERSION = "0.0.4"

from docopt import docopt

from storage import Storage

def cli(args):
    storage = Storage()
    server_list = storage.get_servers()
    server_table = storage.get_server_table()
    print(args)
    if args['list']:
        print(server_table.table)
    if args['add']:
        print("Add a server")
    if args['connect']:
        print("Connect to a server")
    if args['remove']:
        print("Remove a server")


if __name__ == '__main__':
    arguments = docopt(__doc__, version="Junc v" + VERSION)
    cli(arguments)
