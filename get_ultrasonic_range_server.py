#!/usr/bin/env python
import rospy


def handle_get_ultrasonic_range(req):
    return get_ultrasonic_range(req.data)


def get_ultrasonic_range(data_sample):

    # Distance in meters = (duration in seconds) * (speed of sound m/s) / 2
    # Distance in cm = (t * 1e-6) * (340 * 1e2) / 2 = t * 17/1000
    # Distance in millimeters = (t * 1e-6) * (340 * 1e3) / 2 = t * 17/100
    # Return distance in mm, sensor is supposedly accurate to 0.3cm = 3mm
    # Clamp to 4000mm, which is 4m or maximum effective range of this sensor.

    return min(4000, data_sample * 17 / 1000)


def handle_get_ultrasonic_range_server():
    rospy.init_node('find ultrasonic range from raw data to mm')
    s = rospy.Service('get_ultrasonic_range',
                      getUltraSonicRange, handle_get_ultrasonic_range)
    rospy.spin()


if __name__ == "__main__":
    handle_get_ultrasonic_range_server()
