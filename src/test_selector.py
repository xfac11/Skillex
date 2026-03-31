import unittest
import click
from effort import EffortLevel
from selector import Selector
from exercise import Exercise
class TestSelector(unittest.TestCase):
    def test_selector(self):
        selector = Selector("Select your effort", ["Easy", "Medium", "Hard"])
        selection = selector.select(2)
        self.assertEqual(selection, "Medium")
    
    def test_enum_selector(self):
        selector = Selector("Select your effort", [EffortLevel.EASY, EffortLevel.NORMAL, EffortLevel.HARD])
        selection = selector.select(2)
        self.assertEqual(selection, EffortLevel.NORMAL)
    
    def test_exercise_selector(self):
        
        selector = Selector("Select your exercise",
                            [Exercise(1, "Push-up", "cardio", "S", "s"), Exercise(2, "Run", "cardio", "S", "s"), Exercise(3, "Walk", "cardio", "S", "s")])
        selection = selector.select(2)
        self.assertEqual(selection.name, "Run")