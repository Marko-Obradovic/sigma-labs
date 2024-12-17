import unittest
from roman_to_integer import roman_to_int

class TestRomanToInteger(unittest.TestCase):
    def test_one(self):
        self.assertEqual(roman_to_int("III"), 3)
    def test_two(self):
        self.assertEqual(roman_to_int("LVIII"), 58)
    def test_three(self):
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

if __name__ == "__main__":
    unittest.main()
