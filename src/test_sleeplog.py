import unittest
from addtosleeplog import*

class TestSleepLog(unittest.TestCase):
    def testYesterday(self):
        self.assertTrue(sleep_log_yesterday(1))