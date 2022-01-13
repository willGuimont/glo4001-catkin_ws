#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def make_callback(pub):
    def on_message(data):
        data.ranges = [-x for x in data.ranges]
        rospy.loginfo(f'{rospy.get_caller_id()} Received {data.ranges[0]}')
        pub.publish(data)

    return on_message

if __name__ == '__main__':
    pub = rospy.Publisher('/range/front', LaserScan, queue_size=10)
    rospy.init_node('range_sensor', anonymous=True)

    rospy.Subscriber('/proximity/front', LaserScan, make_callback(pub))

    rospy.spin()
