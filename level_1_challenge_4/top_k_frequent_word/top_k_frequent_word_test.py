import unittest

from top_k_frequent_word import generate_top_k_frequent_words

class TestTopKFrequentWord(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(generate_top_k_frequent_words(["i","love","leetcode","i","love","coding"], k=2), ["i","love"])
    def test_case_two(self):
        self.assertEqual(generate_top_k_frequent_words(["the","day","is","sunny","the","the","the","sunny","is","is"], k=4), ["the","is","sunny","day"])

if __name__ == '__main__':
    unittest.main()
