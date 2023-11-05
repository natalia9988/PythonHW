import unittest
from Task3 import Rect


class TestRect(unittest.TestCase):
    def setUp(self):
        self.r1 = Rect(3,3)
        self.r2 = Rect(4,3)

    def test_raise_valueerror(self):
        with self.assertRaises(ValueError):
            Rect(3, -4)

    def test_is_rect(self):
        self.assertIsInstance(self.r1 + self.r2, Rect)

    def test_per(self):
        self.assertEqual(self.r1.per(), 12)


if __name__ == '__main__':
    unittest.main(verbosity=1)