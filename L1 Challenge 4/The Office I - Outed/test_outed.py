import outed
import unittest


class test_outed_solution(unittest.TestCase):

    def test_bad_outcome_one(self):
        self.assertEqual(
            outed.outed(
                {
                    'tim': 0,
                    'jim': 2,
                    'randy': 0,
                    'sandy': 7,
                    'andy': 0,
                    'katie': 5,
                    'laura': 1,
                    'saajid': 2,
                    'alex': 3,
                    'john': 2,
                    'mr': 0
                }, 'laura'), 'Get Out Now!')

    def test_good_outcome(self):
        self.assertEqual(
            outed.outed(
                {
                    'tim': 1,
                    'jim': 3,
                    'randy': 9,
                    'sandy': 6,
                    'andy': 7,
                    'katie': 6,
                    'laura': 9,
                    'saajid': 9,
                    'alex': 9,
                    'john': 9,
                    'mr': 8
                }, 'katie'), 'Nice Work Champ!')

    def test_bad_outcome_two(self):
        self.assertEqual(
            outed.outed(
                {
                    'tim': 2,
                    'jim': 4,
                    'randy': 0,
                    'sandy': 5,
                    'andy': 8,
                    'katie': 6,
                    'laura': 2,
                    'saajid': 2,
                    'alex': 3,
                    'john': 2,
                    'mr': 8
                }, 'john'), 'Get Out Now!')


if __name__ == '__main__': unittest.main()
