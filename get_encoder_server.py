#!/usr/bin/env python
import rospy

def handle_get_encoder(req):
    return get_encoder(req)


def get_encoder(data_sample):
    return (data_sample)


def handle_get_encoding_server():
    rospy.init_node('find encoding data ticks')
    s = rospy.Service('get_encoder', getEncoder, handle_get_encoder)
    rospy.spin()


if __name__ == "__main__":
    handle_get_encoding_server()
