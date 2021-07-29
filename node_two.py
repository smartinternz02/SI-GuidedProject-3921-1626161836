#! /usr/bin/env python3
import rospy
rospy.init_node("node_2")

rate=rospy.Rate(1)

while not rospy.is_shutdown():
     print ('sensor  : sensor : 2')
     rate.sleep()