import top_k_frequent_word
import unittest

class TestTopKFrequentWord(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(top_k_frequent_word.top_k_frequent(["i","love","leetcode","i","love","coding"], k=2), ["i","love"])
    def test_case_two(self):
        self.assertEqual(top_k_frequent_word.top_k_frequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k=4), ["the","is","sunny","day"])

if __name__ == '__main__':
    unittest.main()
