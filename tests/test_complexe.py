import unittest
from math import pi

from mathCustom.complexe import Compl

# TODO: Investigate the impact of the following line.
# while True:
#     try:
#         from mathCustom.complexe import Compl
#
#         break
#     except ModuleNotFoundError:
#         # Running `python tests/test_complexe.py` will fail because
#         # Python doesn't automatically add the parent directory
#         # (your project root) to the Python path. This means it can't find the mathCustom package.
#         # The following line will add the parent directory to the Python path.
#         import os
#         import sys
#
#         sys.path.insert(
#             0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#         )


class TestComplClass(unittest.TestCase):
    def test_initialization(self):
        i = Compl(0, 1)
        c1 = Compl(3, 4)
        self.assertEqual(c1.real, 3)
        self.assertEqual(c1.img, 4)

        c2 = Compl()
        self.assertEqual(c2.real, 0)
        self.assertEqual(c2.img, 0)

        c3 = 1 + i
        self.assertEqual(c3.real, 1)
        self.assertEqual(c3.img, 1)

        c4 = Compl()
        self.assertEqual(c4.real, 0)
        self.assertEqual(c4.img, 0)

    def test_norm(self):
        c = Compl(3, 4)
        self.assertAlmostEqual(c.norm(), 5)

    def test_conjugate(self):
        c = Compl(3, 4)
        conj = c.conjugate()
        self.assertEqual(conj.real, 3)
        self.assertEqual(conj.img, -4)

    def test_trig(self):
        c = Compl(1, 1)
        r, theta = c.trig()
        self.assertAlmostEqual(r, 2**0.5)
        self.assertAlmostEqual(theta, pi / 4)

    def test_str_and_repr(self):
        c1 = Compl(3, 4)
        self.assertEqual(str(c1), "(3 + 4i)")
        self.assertEqual(repr(c1), "(3 + 4i)")

        c2 = Compl(0, 1)
        self.assertEqual(str(c2), "(i)")

        c3 = Compl(2, 0)
        self.assertEqual(str(c3), "(2)")

        c4 = Compl(0, 0)
        self.assertEqual(str(c4), "0")

    def test_addition(self):
        c1 = Compl(1, 2)
        c2 = Compl(3, 4)
        c3 = c1 + c2
        self.assertEqual(c3.real, 4)
        self.assertEqual(c3.img, 6)

        c4 = c1 + 5
        self.assertEqual(c4.real, 6)
        self.assertEqual(c4.img, 2)

    def test_subtraction(self):
        c1 = Compl(3, 4)
        c2 = Compl(1, 2)
        c3 = c1 - c2
        self.assertEqual(c3.real, 2)
        self.assertEqual(c3.img, 2)

        c4 = c1 - 2
        self.assertEqual(c4.real, 1)
        self.assertEqual(c4.img, 4)

    def test_multiplication(self):
        c1 = Compl(1, 2)
        c2 = Compl(3, 4)
        c3 = c1 * c2
        self.assertEqual(c3.real, -5)
        self.assertEqual(c3.img, 10)

        c4 = c1 * 2
        self.assertEqual(c4.real, 2)
        self.assertEqual(c4.img, 4)

    def test_division(self):
        c1 = Compl(3, 4)
        c2 = Compl(1, 2)
        c3 = c1 / c2
        self.assertAlmostEqual(c3.real, 2.2)
        self.assertAlmostEqual(c3.img, -0.4)

        c4 = c1 / 2
        self.assertEqual(c4.real, 1.5)
        self.assertEqual(c4.img, 2)

    def test_power(self):
        c = Compl(1, 1)
        c2 = c**2
        self.assertAlmostEqual(c2.real, 0)
        self.assertAlmostEqual(c2.img, 2)

        c3 = c**0
        self.assertEqual(c3.real, 1)
        self.assertEqual(c3.img, 0)

        c4 = Compl(0, 0) ** 2
        self.assertEqual(c4.real, 0)
        self.assertEqual(c4.img, 0)

        with self.assertRaises(ValueError):
            Compl(0, 0) ** -1

    def test_equality(self):
        c1 = Compl(3, 4)
        c2 = Compl(3, 4)
        c3 = Compl(4, 3)
        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)
        self.assertEqual(Compl(0, 0), 0)

        self.assertEqual(c1 == 5, False)

    def test_in_place_operations(self):
        c = Compl(1, 1)
        c += Compl(2, 2)
        self.assertEqual(c.real, 3)
        self.assertEqual(c.img, 3)

        c -= Compl(1, 1)
        self.assertEqual(c.real, 2)
        self.assertEqual(c.img, 2)

        c *= Compl(2, 0)
        self.assertEqual(c.real, 4)
        self.assertEqual(c.img, 4)

        c /= 2
        self.assertEqual(c.real, 2)
        self.assertEqual(c.img, 2)


if __name__ == "__main__":
    unittest.main()
