import unittest

from src.bodyparts import BodyParts

class TestBodyparts(unittest.TestCase):
    def test_valid_bodypart(self):
        bodyparts = ["cardio", "back", "lower arm"]
        bodypart_xp = BodyParts(bodyparts)
        
        bodypart_xp.set_bodypart_xp("cardio", 100)
        
        self.assertEqual(bodypart_xp.get_bodypart_xp("cardio"), 100)
    
    def test_non_valid_bodypart(self):
        bodyparts = ["cardio", "back", "lower arm"]
        
        bodypart_xp = BodyParts(bodyparts)
        
        result = bodypart_xp.set_bodypart_xp("lower leg", 100)
        
        self.assertEqual(result, False)
    
    def test_getting_level(self):
        bodyparts = ["cardio", "back", "lower arm"]
        
        bodypart_xp = BodyParts(bodyparts)
        
        bodypart_xp.set_bodypart_xp("back", 300)
        
        level = bodypart_xp.get_bodypart_level("back")
        
        self.assertNotEqual(level, -1)