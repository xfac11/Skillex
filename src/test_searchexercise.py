import unittest

from searchexercise import search_exercise

class TestSearchExercise(unittest.TestCase):
    def test_query_bench(self):
        hits = search_exercise("bench")
        self.assertIn("bench pull-ups", hits[0])
    
    def test_query_by_id(self):
        hit = search_exercise("khlHMqs")
        self.assertEqual(len(hit), 1)
        self.assertIn("band bench press", hit[0])
    
    def test_query_by_exact_name(self):
        hit = search_exercise("barbell jm bench press")
        self.assertEqual(len(hit), 1)
        self.assertIn("ZsiqXYa", hit[0])
    
    def test_query_by_nonexisting(self):
        hit = search_exercise("111")
        self.assertListEqual(hit, [])
    
    def test_query_None(self):
        hit = search_exercise(None)
        self.assertListEqual(hit, [])