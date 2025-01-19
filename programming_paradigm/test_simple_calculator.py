from simple_calculator import SimpleCalculator
import unittest


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        with self.assertRaises(TypeError):
            self.calc.add("a", 1)

    def test_division(self):
        self.assertEqual(self.calc.divide(-1, 1), -1)
        with self.assertRaises(TypeError):
            self.calc.divide("a", 1)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        with self.assertRaises(TypeError):
            self.calc.multiply("a", 1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        with self.assertRaises(TypeError):
            self.calc.subtract("a", 1)


if __name__ == "__main__":
    unittest.main()