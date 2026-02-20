import unittest
from src.addtolog import create_exercise
from src.addtolog import add_to_log

from datetime import datetime

import sqlite3

class TestAddToLog(unittest.TestCase):
    def testOneExercise(self):
        exercise = create_exercise("7vG5o25")

        result = add_to_log(1, exercise, 393, 321, 100)

        self.assertEqual(result, True)
    
    def testOneMore(self):
        exercise = create_exercise("isAAZWA")

        result = add_to_log(1, exercise, datetime.now().timestamp(), 300, 200)

        self.assertEqual(result, True)

