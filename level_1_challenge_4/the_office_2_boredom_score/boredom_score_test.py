import unittest

from boredom_score import main, calculate_boredom_score


class TestBoredomScoreSolution(unittest.TestCase):

    def test_overwhelmed_message(self):
        self.assertEqual(
            main(calculate_boredom_score({
                "tim": "change",
                "jim": "accounts",
                "randy": "canteen",
                "sandy": "change",
                "andy": "change",
                "katie": "IS",
                "laura": "change",
                "saajid": "IS",
                "alex": "trading",
                "john": "accounts",
                "mr": "finance"
            })), "kill me now")

    def test_manageable_message(self):
        self.assertEqual(
            main(calculate_boredom_score({
                "tim": "IS",
                "jim": "finance",
                "randy": "pissing about",
                "sandy": "cleaning",
                "andy": "cleaning",
                "katie": "cleaning",
                "laura": "pissing about",
                "saajid": "regulation",
                "alex": "regulation",
                "john": "accounts",
                "mr": "canteen"
            })), "i can handle this")

    def test_celebration_message(self):
        self.assertEqual(
            main(calculate_boredom_score({
                "tim": "accounts",
                "jim": "accounts",
                "randy": "pissing about",
                "sandy": "finance",
                "andy": "change",
                "katie": "IS",
                "laura": "IS",
                "saajid": "canteen",
                "alex": "pissing about",
                "john": "retail",
                "mr": "pissing about"
            })), "party time!!")


if __name__ == '__main__':
    unittest.main()
