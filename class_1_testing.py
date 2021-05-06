import unittest

from main import add_2_numbers


class TestMyMaths(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_2_numbers(2, 2), 4, "Adding two numbers failed")
