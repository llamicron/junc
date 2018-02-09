import re

class Server(object):

    def __init__(self, name, username, ip, location=""):
        self.name = name
        self.username = username
        self.ip = ip
        self.location = location

        self.validate()

    def validate(self):
        Server.validate_username(self.username)

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
