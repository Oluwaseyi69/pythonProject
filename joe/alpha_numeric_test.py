import unittest
from joe.alpha_numeric import new_number


class AlphaNumeric(unittest.TestCase):
    def setUp(self) -> None:
        self.input = AlphaNumeric()

    def test_second_largest(self):
        self.input.first_input()
