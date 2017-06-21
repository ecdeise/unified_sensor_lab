#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int16
from geometry_msgs.msg import Point
from get_ir_range_server import *
from get_heading_server import *
from get_ultrasonic_range_server import *
from get_encoder_server import *

# toggle the led
#  rostopic pub toggle_led std_msgs/Empty --once


def callback_ir(data):
    #rospy.loginfo(rospy.get_caller_id() + "ir raw data: %s", data.data)
    ir_range_mm = handle_get_ir_range(data)
    print("Infrared range: {0} mm".format(ir_range_mm))
    return ir_range_mm


def callback_mag(data):
    heading = handle_get_heading(data)
    print("Heading: {0}".format(heading))
    return heading


def callback_sonar(data):
    us_range_cm = handle_get_ultrasonic_range(data)
    print("ultrasonic range: {0} cm".format(us_range_cm))
    return us_range_cm


def callback_encoder_right(data):
    ticks_right = handle_get_encoder(data)
    print("ticks right: {0}".format(ticks_right))
    return ticks_right


def callback_encoder_left(data):
    ticks_left = handle_get_encoder(data)
    print("ticks left: {0}".format(ticks_left))
    return ticks_left


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

    rospy.Subscriber("encoder_data_right", Int16, callback_encoder_right)

    rospy.Subscriber("encoder_data_left", Int16, callback_encoder_left)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
