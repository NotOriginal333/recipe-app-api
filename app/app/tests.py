"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """
    Tests the Calc module
    """

    def test_add_numbers(self):
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting two numbers"""

        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)
