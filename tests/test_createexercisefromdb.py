import unittest
import sqlite3

from src.addtolog import create_exercise



class TestCreateExerciseFromDB(unittest.TestCase):
    def test_create_one(self):
        exercise = create_exercise("OmQ8w0p")
        self.assertEqual(exercise.bodypart, "back")
    
    def test_create_none(self):
        exercise = create_exercise("dlo")
        self.assertEqual(exercise, None)
    
    def test_create_two(self):
        exercise1 = create_exercise("G70mEAJ")
        exercise2 = create_exercise("7vG5o25")

        self.assertEqual(exercise1.bodypart, "back")
        self.assertEqual(exercise2.equipment, "dumbbell")
