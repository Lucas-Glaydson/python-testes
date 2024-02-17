from unittest import TestCase
from App.calculadora import Calculator


class TestCalculadora(TestCase):

    def setUp(self):
        self.my_calc = Calculator(10, 5)

    def test_add(self):
        self.assertEqual(self.my_calc.add(), 15)

    def test_subtract(self):
        self.assertEqual(self.my_calc.subtract(), 5)

    def test_multiply(self):
        self.assertEqual(self.my_calc.multiply(), 50)

    def test_dive(self):
        self.assertEqual(self.my_calc.dive(), 2)
