import unittest
from simple_calculator import SimpleCalculator

class Test_simple_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(-3, 4), 1)
        self.assertEqual(self.calc.add(-3, -4), -7)
        self.assertEqual(self.calc.add(-3, 4), 1)
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-5, -4), -1)
        self.assertEqual(self.calc.subtract(5, -4), 9)
        self.assertEqual(self.calc.subtract(-5, 4), -9)
        self.assertEqual(self.calc.subtract(5, 4), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-9, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(-9, -1), 9)
        self.assertEqual(self.calc.multiply(9, 1), 9)
        self.assertEqual(self.calc.multiply(9, 4), 36)

    def test_divide(self):
        self.assertEqual(self.calc.divide(3, 0), None)
        self.assertEqual(self.calc.divide(3, 1), 3)
        self.assertEqual(self.calc.divide(3, 3), 1)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-3, 0), None)
        self.assertEqual(self.calc.divide(-3, 1), -3)
        self.assertEqual(self.calc.divide(-3, 3), -1)
        self.assertEqual(self.calc.divide(-3, -3), 1)
        self.assertEqual(self.calc.divide(3, -1), -3)

if __name__ == "__main__":
    unittest.main()




