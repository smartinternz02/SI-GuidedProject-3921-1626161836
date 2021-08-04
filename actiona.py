#! /usr/bin/env python3

import roslib
import rospy
import actionlib
   
from ros_actions.msg import DoDishesAction
   
class DoDishesServer:
    def init(self):
      self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute, False)
      self.server.start()
  
    def execute(self, goal):
      # Do lots of awesome groundbreaking robot stuff here
      print ('action completed')
      self.server.set_succeeded()
      
  
  
if name == 'main':
    rospy.init_node('do_dishes_server')
    server = DoDishesServer()
    rospy.spin()