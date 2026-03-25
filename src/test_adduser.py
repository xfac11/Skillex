import unittest

from adduser import add_user
from user import User
from bodyparts import BodyParts
class TestAddUser(unittest.TestCase):
    def test_addoneuser(self):
        body_parts = ["lower_arms", "shoulder", "cardio", "upper_arms","chest", "lower_legs", "back", "upper_legs", "waist"]
        body_xp = BodyParts(body_parts)
        user = User(None, "Filip", 100, body_xp, 0, 0, 0)
        result = add_user(user)
        self.assertTrue(result)
    
    def test_addnone(self):
        result = add_user(None)
        self.assertFalse(result)
    
    