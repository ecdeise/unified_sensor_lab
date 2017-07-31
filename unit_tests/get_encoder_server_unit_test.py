import unittest
from get_encoder_server import get_encoder

# edeise@D13:~/code/Robot/unified_sensor_lab (master)$ python -m unit_tests/get_encoder_server_unit_test

class TestGetEncoder(unittest.TestCase):

    def test_get_encoder(self):
        res = get_encoder(100)
        self.assertEqual(res, 100)


if __name__ == '__main__':
    unittest.main()
