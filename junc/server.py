import re

from terminaltables import AsciiTable

from .storage import Storage

class _Server(object):

    def __init__(self, server_dict, testing = False):
        # This needs to be imported here because python is stupid
        # Or maybe it's me... Nah it's def python
        # from .storage import Storage
        self.name = server_dict['name']
        self.username = server_dict['username']
        self.ip = server_dict['ip']
        self.location = server_dict['location']


class ServerList(object):
    def __init__(self, testing = False):
        self.st = Storage(testing = testing)
        self.servers = self.get()

    def get(self):
        servers = []
        servers_json = self.st.get_servers()
        for attrs in servers_json:
            servers.append(_Server(attrs))
        return servers

    def add(self, server):
        if type(server) is not _Server:
            raise ValueError("_Server object needs to be given to ServerList.add() You gave me: " + type(server))
        self.servers.append(server)

    def remove(self, name):
        """
        Removes a server from the server list
        If not found, raise ValueError
        """
        for i in range(len(self.servers)):
            if name == self.servers[i].name:
                del self.servers[i]
                return True
        raise ValueError('Server not found: ' + name)

    def save(self):
        self.st.write(self.servers)

    def table(self):
        table_data = [
            ['Name', 'Address', 'Location']
        ]
        for server in self.servers:
            table_data.append([server.name, server.username + "@" + server.ip, server.location])
        return AsciiTable(table_data)


    def validate_name(self, name):
        assert type(name) is str
        for server in self.servers:
            if name == server.name:
                raise ValueError("Name '" + name + "' taken, try another")

    def validate_username(self, username):
        pattern = r'^[a-z][-a-z0-9_]*'
        leftovers = re.sub(pattern, '', username)
        if leftovers:
            raise ValueError(
                "Found character not allowed in usernames: " + leftovers[0])

    def validate_ip(self, ip):
        """
        Addresses can be pretty much anything
        it could be 1.1.1.1
        or https://us-west-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-west-2#/environment/dashboard?applicationName=somethinghere&environmentId=e-234h8df
        """
        if not ip:
            raise ValueError(
                "Please provide an actual IP or web address. You gave me: " + ip)
