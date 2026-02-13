import unittest

from src.calculatexperience import calculate_exercise_experience
from src.calculatexperience import calculate_sleep_experience

class TestExperiencePoints(unittest.TestCase):
    def test_30_repeats(self):
        self.assertEqual(calculate_exercise_experience(10, 6, 0, 0), 300)
    
    def test_30min_cardio(self):
        self.assertEqual(calculate_exercise_experience(0, 0, 10, 20), 300)
    
    def test_cardio_and_repeats(self):
        cardio_xp = calculate_exercise_experience(0, 0, 5, 30)
        repeats_xp = calculate_exercise_experience(45)
        self.assertEqual(cardio_xp+repeats_xp, 100+225)
    
    def test_sleep_experience_2(self):
        self.assertEqual(calculate_sleep_experience(2), 200)
    
    def test_sleep_experience_0(self):
        self.assertEqual(calculate_sleep_experience(0), 0)

