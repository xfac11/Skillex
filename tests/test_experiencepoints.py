import unittest

from src.calculatexperience import *

class TestExperiencePoints(unittest.TestCase):
    def test_30_repeats(self):
        exercise_exp = ExerciseExperience(30)
        exercise_exp.apply_strength_multiplier(2, 10, 3, 40)
        exercise_exp.apply_strength_record_multiplier(2, 6)
        self.assertEqual(exercise_exp.get_experience_points(), 315)
    
    def test_30min_cardio(self):
        self.assertEqual(ExerciseExperience(30).apply_intensity_multiplier(15, 20).apply_effort_multiplier().get_experience_points(), 300)
    
    def test_cardio_and_repeats(self):
        cardio_xp = ExerciseExperience(30)
        
        repeats_xp = ExerciseExperience(15)
        repeats_xp.apply_strength_multiplier(2, 15, 15, 100)
        repeats_xp.apply_strength_record_multiplier(2, 6)

        self.assertEqual(cardio_xp.get_experience_points()+repeats_xp.get_experience_points(), 100+225)
    
    def test_sleep_experience_2(self):
        exercise_exp = ExerciseExperience(30)
        exercise_exp.apply_sleep_multiplier(2)

        self.assertEqual(exercise_exp.get_sleep_multiplier(), 1.02)
    
    def test_sleep_experience_0(self):
        exercise_exp = ExerciseExperience(30)
        exercise_exp.apply_sleep_multiplier(0)

        self.assertEqual(exercise_exp.get_sleep_multiplier(), 1.0)
    
    def test_getting_level_90000xp(self):
        current_xp = 90000
        level = calculate_body_level(current_xp)
        self.assertEqual(level, 33)
    
    def test_getting_level_8264xp(self):
        current_xp = 8265
        level = calculate_body_level(current_xp)
        self.assertEqual(level, 10)
    
    def test_getting_level_13495xp(self):
        current_xp = 13495
        level = calculate_body_level(current_xp)
        self.assertEqual(level, 12)
    
    def test_getting_level_xp_743(self):
        current_xp = 744
        level = calculate_body_level(current_xp)
        self.assertEqual(level, 3)
    
    def test_xp_progress(self):
        xp = 650
        progress = calculate_body_progress_to_next(xp)
        self.assertGreater(progress, 0.5)
    
    def test_xp_progress_340(self):
        xp = 340
        progress = calculate_body_progress_to_next(xp)
        self.assertLess(progress, 0.5)