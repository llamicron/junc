import os
import json

from docopt import docopt

try:
    from storage import Storage
except ImportError:
    from .storage import Storage

class Junc(object):
    def __init__(self, jsonfile=False):
        self.jsonfile = jsonfile
        if not jsonfile:
            self.jsonfile = os.path.join(os.path.expanduser('~'), '.junc.json')

        Junc.create_file(self.jsonfile)
        self.servers = self.get_servers()


    @staticmethod
    def create_file(fi):
        if not os.path.isfile(fi):
            open(fi, 'w')

    def get_servers(self):
        if not os.path.isfile(self.jsonfile):
            raise FileNotFoundError('File ' + self.jsonfile + ' could not be found')
        try:
            return json.load(open(self.jsonfile, 'r'))
        except json.JSONDecodeError:
            return []
