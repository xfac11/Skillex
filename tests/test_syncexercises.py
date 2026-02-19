import unittest

from scripts.sync_exercises import *

class TestSyncExercises(unittest.TestCase):
    def test_connection(self):
        exercises = get_exercises_from_api(True)

        self.assertNotEqual(exercises[0]["name"], None)
        
