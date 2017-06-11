#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
from get_ir_range_server import *
from get_heading_server import *
from get_ultrasonic_range_server import *


def callback_ir(data):
    #rospy.loginfo(rospy.get_caller_id() + "ir raw data: %s", data.data)
    range_mm = handle_get_ir_range(data)
    print("range: {0} mm".format(range_mm))
    # print(data.data)


def callback_mag(data):
    # rospy.loginfo(rospy.get_caller_id())
    heading = handle_get_heading(data)
    print("Heading: {0}".format(heading))
    #print("Magnetometer:  x {0}, y {1}, z {2}".format(data.x, data.y, data.z))


def callback_sonar(data):
    #rospy.loginfo(rospy.get_caller_id() + "ultrasonic raw data: %s", data.data)
    range_cm = handle_get_ultrasonic_range(data)
    print("range: {0} cm".format(range_cm))


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("ir_data_raw", Float32, callback_ir)

    rospy.Subscriber("mag_data_raw", Point, callback_mag)

    rospy.Subscriber("ultrasonic_data_raw", Float32, callback_sonar)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
