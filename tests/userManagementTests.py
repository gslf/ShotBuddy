import unittest

from webapp.User import User
from webapp.UsersManager import UsersManager

class TestUserManagement(unittest.TestCase):

    

    def __init__(self, *args, **kwargs):
        super(TestUserManagement, self).__init__(*args, **kwargs)

        # Init params
        self.username = "StrangeUser1212451235111"
        self.pwd1 = "test_pwd_1"
        self.pwd2 = "test_pwd_2"


    def testNewUsermanagement(self):
        user = User(self.username)
        um = UsersManager(user)

        # Create a new user
        result = um.add(self.pwd1)
        self.assertNotEqual(result[0], False)

        # Change Password
        result = um.newPassword(self.pwd2)
        self.assertNotEqual(result[0], False)

        # Check new Password
        user.password = self.pwd2
        result = um.check()
        self.assertNotEqual(result, False)

        # Delete the user
        result = um.remove()
        self.assertNotEqual(result[0], False)

