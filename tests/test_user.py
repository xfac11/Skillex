import unittest

from src.user import User
from src.bodyparts import BodyParts
class TestUser(unittest.TestCase):
    def test_user(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Filip", 0, bodypart_xp, 0, 2, 6)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Filip")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 0)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
    
    def test_global_xp(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Louise", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_global_xp(200)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Louise")
        self.assertEqual(user.global_xp, 200)
        self.assertEqual(user.body_xp.get_bodypart_xp("lower arm"), 0)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, 4)
    
    
    def test_body_xp(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Louise", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_body_xp("back", 200)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Louise")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 200)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, 3)
    
    def test_body_nonexisting(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Louise", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_body_xp("shoulder", 200)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Louise")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 0)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, -1)
    
    def test_body_non_level_up(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Louise", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_body_xp("back", 10)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Louise")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 10)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, 0)
    
    def test_sleep_streak(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Josefin", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_body_xp("back", 200)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Josefin")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 200)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, 3)
        
        
        user.increase_sleep_streak()
        self.assertEqual(user.sleep_streak, 3)
        
        user.decrease_sleep_streak()
        self.assertEqual(user.sleep_streak, 2)
        
        user.decrease_sleep_streak()
        user.decrease_sleep_streak()
        user.decrease_sleep_streak()
        user.decrease_sleep_streak()
        self.assertEqual(user.sleep_streak, 0)
    
    def test_update_highest_weight(self):
        bodyParts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyParts)
        
        user:User = User(1, "Louise", 0, bodypart_xp, 0, 2, 6)
        
        level = user.increase_body_xp("back", 200)
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Louise")
        self.assertEqual(user.global_xp, 0)
        self.assertEqual(user.body_xp.get_bodypart_xp("back"), 200)
        self.assertEqual(user.streak, 0)
        self.assertEqual(user.sleep_streak, 2)
        self.assertEqual(user.highest_weight, 6)
        self.assertEqual(level, 3)
        
        user.update_highest_weight(15)
        self.assertEqual(user.highest_weight, 15)
    
        