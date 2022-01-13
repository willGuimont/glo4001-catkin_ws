#!/usr/bin/env python3
import math
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

sensor_curve = [[0, 0], [10, 2.6],
                [15, 2.76], [20, 2.53],
                [30, 1.99], [40, 1.53],
                [50, 1.23], [60, 1.04],
                [70, 0.91], [80, 0.82],
                [90, 0.72], [100, 0.66],
                [110, 0.6], [120, 0.55],
                [130, 0.50], [140, 0.46],
                [150, 0.435], [150, 0]]


def simulate_sensor(reading):
    reading_cm = reading * 100
    for pt1, pt2 in zip(sensor_curve, sensor_curve[1:]):
        if pt1[0] <= reading_cm < pt2[0]:
            dx = pt2[0] - pt1[0]
            dy = pt2[1] - pt1[1]
            return (reading_cm - pt1[0]) * dy / dx + pt1[1]
    return math.inf


def make_callback(pub):
    def on_message(data):
        data.ranges = [simulate_sensor(x) for x in data.ranges]
        pub.publish(data)

    return on_message


if __name__ == '__main__':
    pub = rospy.Publisher('/range/front', LaserScan, queue_size=10)
    rospy.init_node('range_sensor', anonymous=True)
    rospy.Subscriber('/proximity/front', LaserScan, make_callback(pub))
    rospy.spin()
