import unittest
from get_ir_range_server import get_ir_range

# edeise@D13:~/code/Robot/unified_sensor_lab (master)$ python -m unit_tests/get_ir_range_server_unit_test


class TestGetIrRange(unittest.TestCase):

    def test_get_ir_range(self):
        res = get_ir_range(100)
        self.assertEqual(res, 9462 / (100 - 16.92))


if __name__ == '__main__':
    unittest.main()
