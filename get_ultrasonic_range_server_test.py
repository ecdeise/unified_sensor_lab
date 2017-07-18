import unittest
from get_ultrasonic_range_server import get_ultrasonic_range


class TestGetUSRange(unittest.TestCase):

    def test_get_ultrasonic_range(self):
        res = get_ultrasonic_range(100)
        self.assertEqual(res, min(4000, 100 * 17 / 1000))


if __name__ == '__main__':
    unittest.main()
