import unittest
from decode_the_message import format_key, decode_message

class TestDecodeTheMessage(unittest.TestCase):
    def test_one(self):
        formatted_key = format_key("the quick brown fox jumps over the lazy dog")
        decoded_message = decode_message(
                "vkbs bs t suepuv",
                formatted_key
                )
        self.assertEqual(decoded_message, "this is a secret")
    def test_two(self):
        formatted_key = format_key("eljuxhpwnyrdgtqkviszcfmabo")
        decoded_message = decode_message(
                "zwx hnfx lqantp mnoeius ycgk vcnjrdb",
                formatted_key
                )
        self.assertEqual(decoded_message, "the five boxing wizards jump quickly")

if __name__ == "__main__":
    unittest.main()
