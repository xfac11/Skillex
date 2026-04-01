import unittest
from averageover import AverageOver

class TestAverageOver(unittest.TestCase):
    def test_average5days(self):
        ordered_speed_by_date = [5, 3, 1, 5, 6, 7, 1, 3]
        avg = AverageOver(5, ordered_speed_by_date)
        average = avg.average()
        should_be_average = (5 + 3 + 1 + 5 + 6) / 5
        self.assertAlmostEqual(average, should_be_average)
    
    def test_average10days(self):
        ordered_speed_by_date = [5, 3, 1, 5, 6, 7, 1, 3, 10, 5, 6, 7, 8, 12, 12, 12, 13]
        avg = AverageOver(10, ordered_speed_by_date)
        average = avg.average()
        should_be_average = (5 + 3 + 1 + 5 + 6 + 7 + 1 + 3 + 10 + 5) / 10
        self.assertAlmostEqual(average, should_be_average)