import unittest
from get_encoder_server import get_encoder


class TestGetEncoder(unittest.TestCase):

    def test_get_encoder(self):
        res = get_encoder(100)
        self.assertEqual(res, 100)


if __name__ == '__main__':
    unittest.main()
