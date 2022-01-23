#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('timer')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(1)
s = 0
m = 0
while not rospy.is_shutdown():
    s += 1
    if s == m + 60:
        m += 100
        s += 100
        s -= 60
    pub.publish(s)
    rate.sleep()
