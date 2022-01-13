#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def make_callback(pub):
    def on_message(data):
        rospy.loginfo(f'{rospy.get_caller_id()} Received {data.data}')
        pub.publish(f'Hello {data.data}')

    return on_message

if __name__ == '__main__':
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('range_sensor', anonymous=True)

    rospy.Subscriber('/proximity/front', LaserScan, make_callback(pub))

    rospy.spin()
