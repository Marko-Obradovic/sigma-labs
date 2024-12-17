import unittest
from decode_the_message import decode_message

class TestDecodeTheMessage(unittest.TestCase):
    def test_one(self):
        self.assertEqual(decode_message("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"), "this is a secret")
    def test_two(self):
        self.assertEqual(decode_message("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"), "the five boxing wizards jump quickly")

if __name__ == "__main__":
    unittest.main()
    
