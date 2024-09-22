import unittest

from mathCustom.vector import Vec


class TestVec(unittest.TestCase):
    def test_initialization(self):
        v = Vec(1, 2, 3)
        self.assertEqual(str(v), "(1, 2, 3)")
        v2 = Vec([4, 5, 6])
        self.assertEqual(str(v2), "(4, 5, 6)")

    def test_norm(self):
        v = Vec(3, 4)
        self.assertEqual(v.norm(), 5.0)
        v2 = Vec(1, 2, 2)
        self.assertEqual(v2.norm(), 3.0)

    def test_addition(self):
        v1 = Vec(1, 2, 3)
        v2 = Vec(4, 5, 6)
        v3 = v1 + v2
        self.assertEqual(str(v3), "(5, 7, 9)")

        # Adding scalar
        v4 = v1 + 5
        self.assertEqual(str(v4), "(6, 7, 8)")

        # Right-side addition
        v5 = 10 + v1
        self.assertEqual(str(v5), "(11, 12, 13)")

        # Addition of vectors with different sizes should raise ValueError
        with self.assertRaises(ValueError):
            v1 + Vec(1, 2)

    def test_subtraction(self):
        v1 = Vec(5, 7, 9)
        v2 = Vec(4, 5, 6)
        v3 = v1 - v2
        self.assertEqual(str(v3), "(1, 2, 3)")

        # Subtracting scalar
        v4 = v1 - 3
        self.assertEqual(str(v4), "(2, 4, 6)")

        # Right-side subtraction
        v5 = 10 - v1
        self.assertEqual(str(v5), "(5, 3, 1)")

        # Subtraction of vectors with different sizes should raise ValueError
        with self.assertRaises(ValueError):
            v1 - Vec(1, 2)

    def test_negation(self):
        v = Vec(1, -2, 3)
        neg_v = -v
        self.assertEqual(str(neg_v), "(-1, 2, -3)")

    def test_multiplication(self):
        v1 = Vec(1, 2, 3)
        v2 = Vec(4, 5, 6)

        # Dot product
        result = v1 * v2
        self.assertEqual(result, 32)

        # Scalar multiplication
        v3 = v1 * 2
        self.assertEqual(v3, 12)

        # Right-side scalar multiplication
        v4 = 3 * v1
        self.assertEqual(v4, 18)

        # Multiplication of vectors with different sizes should raise ValueError
        with self.assertRaises(ValueError):
            v1 * Vec(1, 2)

    def test_division(self):
        v1 = Vec(10, 20, 30)

        # Scalar division
        v2 = v1 / 2
        self.assertEqual(str(v2), "(5.0, 10.0, 15.0)")

        # Right-side scalar division
        v3 = 60 / v1
        self.assertEqual(str(v3), "(6.0, 3.0, 2.0)")

        # Division by zero should raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            v1 / 0

        # Vector division with different sizes should raise ValueError
        with self.assertRaises(ValueError):
            v1 / Vec(1, 2)

    def test_equality(self):
        v1 = Vec(1, 2, 3)
        v2 = Vec(1, 2, 3)
        v3 = Vec(0, 0, 0)
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

    def test_inplace_operations(self):
        v1 = Vec(1, 2, 3)

        # In-place addition
        v1 += Vec(1, 1, 1)
        self.assertEqual(str(v1), "(2, 3, 4)")

        # In-place subtraction
        v1 -= Vec(1, 1, 1)
        self.assertEqual(str(v1), "(1, 2, 3)")

        # In-place multiplication
        v1 *= 2
        self.assertEqual(str(v1), "(2, 4, 6)")

        # In-place division
        v1 /= 2
        self.assertEqual(str(v1), "(1.0, 2.0, 3.0)")


if __name__ == "__main__":
    unittest.main()
