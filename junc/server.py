import re

class Server(object):

    def __init__(self, server_dict, testing = False):
        # This needs to be imported here because python is stupid
        # Or maybe it's me... Nah it's def python
        # from .storage import Storage

        self.name = server_dict['name']
        self.username = server_dict['username']
        self.ip = server_dict['ip']
        self.location = server_dict['location']

        self.validate()

    def validate(self):
        Server.validate_username(self.username)
        Server.validate_ip(self.ip)
        Server.validate_name(self.name)

    @staticmethod
    def validate_name(name):
        if not name:
            raise ValueError("Provide a name")
        # for server in other_names:
        #     if server.name == name:
        #         raise ValueError("Name (%s) taken, try another" % name)

    @staticmethod
    def validate_username(username):
        pattern = r'^[a-z][-a-z0-9_]*'
        leftovers = re.sub(pattern, '', username)
        if leftovers:
            raise ValueError("Found character not allowed in usernames: " + leftovers[0])

    @staticmethod
    def validate_ip(ip):
        """
        Addresses can be pretty much anything
        it could be 1.1.1.1
        or https://us-west-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-west-2#/environment/dashboard?applicationName=somethinghere&environmentId=e-234h8df
        """
        if not ip:
            raise ValueError("Please provide an actual IP or web address. You gave me: " + ip)
