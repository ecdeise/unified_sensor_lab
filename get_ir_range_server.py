#!/usr/bin/env python
import rospy


def handle_get_ir_range(req):
    return get_ir_range(req.data)


def get_ir_range(data_sample):
    return 9462 / (data_sample - 16.92)


def handle_get_ir_range_server():
    rospy.init_node('find IR range from raw data to mm')
    s = rospy.Service('get_ir_range', getIrRange, handle_get_ir_range)
    rospy.spin()


if __name__ == "__main__":
    handle_get_ir_range_server()
