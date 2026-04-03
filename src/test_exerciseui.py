import unittest
from exerciseui import ExerciseUI
from exercisecatalog import ExerciseCatalog
class TestExerciseUI(unittest.TestCase):
    def test_exercise_farmers_walk(self):
        id = "qPEzJjA"
        ex_ui = ExerciseUI(ExerciseCatalog().get_exercise(id))
        print(ex_ui.to_string())