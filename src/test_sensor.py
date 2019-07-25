#!/usr/bin/env python

import rospy
import numpy as np
import message_filters
from std_msgs.msg import Int64

class subscribe_sensors():
	def __init__(self):
		self.a_array = []
		self.b_array = []
		self.c_array = []
		self.max_array = []
		self.average_array = []
		rospy.init_node("test_sensor")
	    sub_a = message_filters.Subscriber("a/light_sensor", Int64)
	    # sub_a.registerCallback(callback_a)
	    sub_b = message_filters.Subscriber("b/light_sensor", Int64)
	    # sub_b.registerCallback(callback_b)
	    sub_c = message_filters.Subscriber("c/light_sensor", Int64)
	    # sub_c.registerCallback(callback_c)
	    ts = message_filters.TimeSynchronizer([sub_a, sub_b, sub_c], 10)
	    ts.registerCallback(callback)
	    rospy.spin()

	def callback(self, a, b, c):
		self.a_array.append(a)
		self.b_array.append(b)
		self.c_array.append(c)
		lights = np.array([a,b,c])
		maximum = np.amax(lights)
		average = np.mean(lights)
		self.max_array.append(maximum)
		self.average_array.append(average)
		rospy.loginfo("light sensor a: %s", str(a))
		rospy.loginfo("light sensor b: %s", str(b))
		rospy.loginfo("light sensor c: %s", str(c))
		rospy.loginfo("max sensor: %s", str(maximum))
		rospy.loginfo("avg sensor: %s", str(average))
		

	# Call other functions


if __name__ == '__main__':
    listener()