#!/usr/bin/env python3
import rospy
import numpy as np
import socket
import os
from std_msgs.msg import Float32MultiArray
class sensor():
	def __init__(self):
		self.node = rospy.init_node("light_sensor_coef", anonymous=True)
		self.coefs_publisher = rospy.Publisher("sensor_coefs", Float32MultiArray, queue_size=10)
		self.coefs=Float32MultiArray()
		self.coefs.data=np.loadtxt('{}/coefs_{}.txt'.format(os.environ['HOME'],socket.gethostname()),delimiter=',')
			
	def publish_coef(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			self.sensor_publisher.publish(self.sensor_readings)
			self.coefs_publisher.publish(self.coefs)
			r.sleep()

if __name__ == '__main__':
	try:
		print("Starting Light Sensor Readings")
		a = sensor()
		while not rospy.is_shutdown():
			a.publish_coef()
	except rospy.ROSInterruptException:
		pass
