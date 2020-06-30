import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):    
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(10, -5), 5)
        self.assertEqual(calculator.add(-10, -5), -15)

    def test_subtract(self):    
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(10, -5), 15)
        self.assertEqual(calculator.sub(-10, -5), -5)

    def test_div(self):    
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(10, -5), -2)
        self.assertEqual(calculator.div(-10, -5), 2)

        self.assertRaises(ValueError, calculator.div, 10,0)

        with self.assertRaises(ValueError):
            calculator.div(10, 0)
    
    def test_mul(self):    
        self.assertEqual(calculator.mul(10, 5), 50)
        self.assertEqual(calculator.mul(10, -5), -50)
        self.assertEqual(calculator.mul(-10, -5), 50)

    def test_modulus(self):    
        self.assertEqual(calculator.mod(10, 3), 1)
        self.assertEqual(calculator.mod(3, 10), 3)
        self.assertEqual(calculator.mod(3, -10), -7)


if __name__ == "__main__":
    unittest.main()
    pass