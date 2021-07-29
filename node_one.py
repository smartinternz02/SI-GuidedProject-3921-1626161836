#! /usr/bin/env python3
import rospy
rospy.init_node("node_1")

rate=rospy.Rate(3)

while not rospy.is_shutdown():
     print ('sensor :  sensor : 1')
     rate.sleep()
     
