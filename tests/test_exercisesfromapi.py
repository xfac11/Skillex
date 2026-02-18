import unittest
from src.createexercisedb import *

class TestExerciseFromAPI(unittest.TestCase):
    def testConnection(self):
        get_exercises_from_api()