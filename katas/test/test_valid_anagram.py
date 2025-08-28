import unittest
from katas.valid_anagram import is_anagram

class TestValidAnagram(unittest.TestCase):
    def test_true_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("elbow", "below"))
        self.assertTrue(is_anagram("study", "dusty"))
        self.assertTrue(is_anagram("The Eyes", "They See"))
        self.assertTrue(is_anagram("Dormitory", "Dirty Room"))
        self.assertTrue(is_anagram("Astronomer", "Moon starer"))

    def test_false_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("test", "settle"))
        self.assertFalse(is_anagram("anagram", "nag a ram!"))  # punctuation ignored

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertTrue(is_anagram(" ", "  "))
        self.assertFalse(is_anagram("a", ""))

    def test_case_insensitivity(self):
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("ElBoW", "BeLoW"))

if __name__ == '__main__':
    unittest.main()