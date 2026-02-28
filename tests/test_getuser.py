import unittest
from src.getuser import get_user
from src.user import User
class TestGetUser(unittest.TestCase):
    def test_get_existing_user(self):
        user = get_user("Filip")
        
        self.assertIsNotNone(user)
        self.assertEqual(user.global_xp, 100)
        self.assertEqual(user.body_xp.get_bodypart_xp("cardio"), 0)
        self.assertEqual(user.highest_weight, 0)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Filip")
        self.assertEqual(user.sleep_streak, 0)
        
    def test_get_non_existing_user(self):
        user = get_user("Louise")
        
        self.assertIsNone(user)
    
    