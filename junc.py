"""
Usage:
    junc connect <connect_to>
    junc list
    junc add (<name> <username> <ip>) [<location>]
    junc remove <name>

Options:
    -h --help     Show this screen.
    --version     Show version.

Notes:
    Data is stored in ~/.junc.json
"""

VERSION = "0.0.4"

from docopt import docopt

from storage import Storage
from server import *

def cli(args):
    storage = Storage()
    server_list = storage.get_servers()
    server_table = storage.get_server_table()

    if args['list']:
        print(server_table)

    if args['add']:
        server_list.append(new_server(args))
        storage.write(server_list)

    if args['connect']:
        print("Connect to a server")

    if args['remove']:
        for i in range(len(server_list)):
            if server_list[i]['name'] == args['<name>']:
                del server_list[i]
                break
            if i == len(server_list) - 1:
                print("Couldn't find that server...")
        storage.write(server_list)

if __name__ == '__main__':
    arguments = docopt(__doc__, version="Junc v" + VERSION)
    cli(arguments)
