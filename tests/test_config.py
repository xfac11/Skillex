import unittest
from src.config import*

class TestConfig(unittest.TestCase):
    def test_config_save(self):
        name = "Filip"
        id = 0
        self.assertTrue(save_config(name, id))
    
    def test_config_load(self):
        user_tuple = load_config()
        name = user_tuple[0]
        id = user_tuple[1]
        self.assertEqual(name, "Filip")
        self.assertEqual(id, 0)