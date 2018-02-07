import json
from shutil import copy2
import os

from terminaltables import AsciiTable


class Storage():
    """
    Handles storing and retrieving of server data
    """
    def __init__(self, testing = False):
        self.file_path = os.path.join(os.path.expanduser("~"), ".junc.json")
        if testing:
            self.file_path += '.test'
        self.create_file(self.file_path)

    def create_file(self, file_path):
        """
        Creates the storage file if it doesn't exist
        """
        try:
            open(file_path, 'a')
        except IOError:
            print("Error: Permission denied. Change permissions on " + file_path)
            raise
        return True

    def write(self, server_list):
        """
        Writes a whole server list to the storage file
        """
        with open(self.file_path, 'w') as f:
            json.dump(server_list, f, indent=4)

    def get_servers(self):
        try:
            return json.loads(open(self.file_path, 'r').read())
        except ValueError:
            return []

    def backup(self, location=None, reverse=False):
        """
        Copies the contents of the storage file to the location variable
        Default is the storage file with '.bak' appended to the path
        """
        if not location:
            location = self.file_path + '.bak'
        if reverse:
            print('Restoring to', self.file_path)
            copy2(location, self.file_path)
            print('Done')
        else:
            print('Backing up to', location)
            copy2(self.file_path, location)
            print('Done')

    def restore(self, location=None):
        """
        'Backup' the backup to the regular storage file
        """
        self.backup(location, True)
