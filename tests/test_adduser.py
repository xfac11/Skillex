import unittest

from src.adduser import add_user
from src.user import User
from src.bodyparts import BodyParts
class TestAddUser(unittest.TestCase):
    def test_addoneuser(self):
        body_parts = ["lower_arms", "shoulder", "cardio", "upper_arms","chest", "lower_legs", "back", "upper_legs", "waist"]
        body_xp = BodyParts(body_parts)
        user = User(None, "Filip", 100, body_xp, 0, 0, 0)
        add_user(user)