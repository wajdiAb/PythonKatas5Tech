import unittest
from katas.list_diff import find_difference


class Testlistdiff(unittest.TestCase):
    def test_find_difference(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22) #test case for hello_world function 

    def test_is_empty(self):
        with self.assertRaises(ValueError):
            find_difference([])

    def test_is_list(self):
        with self.assertRaises(TypeError):
            find_difference("hello world")
        # self.assertEqual(find_difference(10), "Input must be a list") #test case for hello_world function 
