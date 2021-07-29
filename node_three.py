#! /usr/bin/env python3
import rospy
rospy.init_node("node_3")

rate=rospy.Rate(2)

while not rospy.is_shutdown():
     print ('sensor :  node 3')
     rate.sleep()
     