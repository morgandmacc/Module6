import unittest
from more_functions import validate_input_in_functions as val_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python1!: 0", val_input.score_input("Python1!"))

    def test_score_input_test_score_valid(self):
        self.assertEqual(True, False)

    def test_score_input_test_score_below_range(self):
        self.assertEqual(True, False)

    def test_score_input_test_score_above_range(self):
        self.assertEqual(True, False)

    def test_test_score_non_numeric(self):
        self.assertEqual(True, False)

    def test_score_input_invalid_message(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
