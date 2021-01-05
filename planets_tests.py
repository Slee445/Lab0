import unittest
from planets import *

# Write more test cases!

class Test_planets(unittest.TestCase):

    def test_mars(self) -> None:
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight,"Mars"),51.68)

    def test_Jupiter(self) -> None:
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight,"Jupiter"),318.24)

    def test_mars1(self) -> None:
        weight = 250
        self.assertAlmostEqual(weight_on_planets(weight,"Mars"),95.0)

    def test_Jupiter1(self) -> None:
        weight = 250
        self.assertAlmostEqual(weight_on_planets(weight,"Jupiter"),585.0)

    def test_Venus(self) -> None:
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight,"Venus"),123.76)

    def test_Venus1(self) -> None:
        weight = 250
        self.assertAlmostEqual(weight_on_planets(weight,"Venus"),227.5)



    def test_error(self) -> None:
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            weight = 99
            weight_on_planets(weight,"Neptune")

if __name__ == "__main__":
        unittest.main()