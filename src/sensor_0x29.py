#!/usr/bin/env python

import rospy
import publish_sensor

if __name__ == '__main__':
	try:
		a = publish_sensor.sensor(0x29)
		a.publish_sensor()
	except rospy.ROSInterruptException:
		pass
