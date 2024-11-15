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
        self.assertTrue(isinstance(self.calc.divide(0, 0), str))
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(7, -3), -2)
        self.assertEqual(self.calc.divide(-6, 4), -1)
        self.assertEqual(self.calc.divide(-12, -5), 2)
    
    def test_mod(self):
        self.assertEqual(self.calc.modulo(3, 10), 3)
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(0, 0), 0)
        self.assertEqual(self.calc.modulo(5, 0), 5)
        self.assertEqual(self.calc.modulo(-4, 0), -4)
        self.assertEqual(self.calc.modulo(0, 3), 0)
        self.assertEqual(self.calc.modulo(0, -8), -8)
        self.assertEqual(self.calc.modulo(2, -3), -1)
        self.assertEqual(self.calc.modulo(7, -3), -2)
        self.assertEqual(self.calc.modulo(4, -3), -2)
        self.assertEqual(self.calc.modulo(2, -3), -1)
        self.assertEqual(self.calc.modulo(-3, -7), -3)
        self.assertEqual(self.calc.modulo(-8, -3), -2)
        

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()