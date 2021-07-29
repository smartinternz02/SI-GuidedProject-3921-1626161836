#! /usr/bin/env python3
import rospy
from ros_topics.msg import IoTSensor

import random


rospy.init_node('iot_sensor_publisher', anonymous=True)

pub=rospy.Publisher('/iot_sensor_topic',IoTSensor, queue_size=10)

rate=rospy.Rate(1)

i=0
while not rospy.is_shutdown():
    iot_sensor= IoTSensor()
    iot_sensor.id =1
    iot_sensor.name="Sensor"
    iot_sensor.temperature =24.33+(random.random()*2)
    iot_sensor.humidity =33.44 +(random.random()*2)

    rospy.loginfo("Sensor Information Published")
    pub.publish(iot_sensor)
    rate.sleep()
    i=i+1