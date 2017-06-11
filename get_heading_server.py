#!/usr/bin/env python
import rospy
import math


def handle_get_heading(req):
    return get_heading(req)


def get_heading(data_sample):

    # http://www.magnetic-declination.com/
    declinationAngle = 0.25  # boston

    heading = math.atan2(data_sample.y, data_sample.x)

    corrected_heading = heading + declinationAngle

    if corrected_heading < 0:
        corrected_heading += 2 * math.pi

    if corrected_heading > 2 * math.pi:
        corrected_heading -= 2 * math.pi

    return (corrected_heading * 180) / math.pi


def handle_get_heading_server():
    rospy.init_node('find heading raw data')
    s = rospy.Service('get_heading', getHeading, handle_get_heading)
    rospy.spin()


if __name__ == "__main__":
    handle_get_heading()
