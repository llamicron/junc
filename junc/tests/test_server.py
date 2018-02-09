import unittest

from ..server import Server

class TestServer(unittest.TestCase):

    def test_username_validation(self):
        with self.assertRaises(ValueError):
            Server.validate_username("username_with_@_in_it")
            Server.validate_username("username_with_^_in_it")
            Server.validate_username("username_with_*_in_it")
            Server.validate_username("username_with_$#@!@#$%^&*(^%$%^&*(_in_it")
            Server.validate_username("you_get_the_f$#%ing_picture")

    def test_ip_validation(self):
        # Addresses can be pretty much anything
        # it could be 1.1.1.1
        # Or https://us-west-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-west-2#/environment/dashboard?applicationName=somethinghere&environmentId=e-234h8df
        # I check that it's not an empty string
        with self.assertRaises(ValueError):
            Server.validate_ip('')
