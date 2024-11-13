import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-2, 0), -2)
    
    def test_sub(self):
        self.assertEqual(self.calc.subtract(0, 1), -1)
        self.assertEqual(self.calc.subtract(2, -5), 7)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(-6, 7), -42)
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_div(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertTrue(isinstance(self.calc.divide(0, 0), str))

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()