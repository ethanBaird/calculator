import unittest

from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(10, 5)

    def test_can_add(self):
        self.assertEqual(15, self.calculator.add())

    def test_can_subtract(self):
        self.assertEqual(5, self.calculator.subtract())

    def test_can_multiply(self):
        self.assertEqual(50, self.calculator.multiply())

    def test_can_divide(self):
        self.assertEqual(2, self.calculator.divide())

