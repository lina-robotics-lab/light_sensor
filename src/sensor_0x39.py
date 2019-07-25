#!/usr/bin/env python

import rospy
import time
import smbus
from std_msgs.msg import Int16
import publish_sensor

if __name__ == '__main__':
	try:
		b = publish_sensor.sensor(0x39)
		b.publish_sensor()
	except rospy.ROSInterruptException:
		pass
