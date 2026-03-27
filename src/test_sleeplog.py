import unittest
from addtosleeplog import*

class TestSleepLog(unittest.TestCase):
    def test_yesterday(self):
        self.assertTrue(sleep_log_yesterday(1))
    
    def test_sleep_streak_update(self):
        user = User(1, "Fredrik", sleep_streak=2)
        codes = update_sleep_streak(user, 7, True)
        self.assertEqual(SleepUpdateCode.SLEPT_7, codes[0])
        self.assertEqual(SleepUpdateCode.LOGGED_YESTERDAY, codes[1])
        self.assertEqual(user.sleep_streak, 3)
    
    def test_sleep_streak_update_forgot_yesterday(self):
        user = User(1, "Wilma", sleep_streak=4)
        codes = update_sleep_streak(user, 7, False)
        self.assertEqual(SleepUpdateCode.SLEPT_7, codes[0])
        self.assertEqual(SleepUpdateCode.FORGOT_YESTERDAY, codes[1])
        self.assertEqual(user.sleep_streak, 1)
    
    def test_sleep_streak_update_forgot_and_less_7(self):
        user = User(1, "Peter", sleep_streak=2)
        codes = update_sleep_streak(user, 6, False)
        self.assertEqual(SleepUpdateCode.SLEPT_LESS_7, codes[0])
        self.assertEqual(SleepUpdateCode.FORGOT_YESTERDAY, codes[1])
        self.assertEqual(user.sleep_streak, 1)
    
    def test_sleep_streak_update_less_7(self):
        user = User(1, "Ture", sleep_streak=4)
        codes = update_sleep_streak(user, 6, True)
        self.assertEqual(SleepUpdateCode.SLEPT_LESS_7, codes[0])
        self.assertEqual(SleepUpdateCode.LOGGED_YESTERDAY, codes[1])
        self.assertEqual(user.sleep_streak, 3)
    
    