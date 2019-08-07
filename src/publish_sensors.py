#!/usr/bin/env python

import rospy
import time
import smbus
import python_tsl2591
import numpy as np
from std_msgs.msg import Int32MultiArray

# Machine Variables (No Touchy!)
NUM_SENSORS = 8
ADDRESS = 0x70
VISIBLE = 2
INFRARED = 1
FULLSPECTRUM = 0

# Actions
SWITCH = 0x04

# Channels
CHANNEL0 = 0x01
CHANNEL1 = 0x02
CHANNEL2 = 0x04
CHANNEL3 = 0x08
CHANNEL4 = 0x10
CHANNEL5 = 0x20
CHANNEL6 = 0x40
CHANNEL7 = 0x80
CHANNELS = [CHANNEL0, CHANNEL1, CHANNEL2, CHANNEL3, CHANNEL4, CHANNEL5, CHANNEL6, CHANNEL7]


class sensors():
	def __init__(self, address=0x70):
		rospy.init_node("light_sensors", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_readings", Int32MultiArray, queue_size=10)
		self.rate = rospy.Rate(1)
		self.sensor_readings = Int32MultiArray()
		self.sensor_readings.data = [0,0,0,0,0,0,0,0]
		
		# Get I2C bus
		self.bus = smbus.SMBus(1)

		# The TSL2561 default address is 0x70
		self.address = address
		self.bus.write_byte_data(self.address, SWITCH, 0xff) # Start with Channel 0
		self.tsl2591 = python_tsl2591.tsl2591()

		time.sleep(0.5)

	def read_sensors(self):
		for i in range(8):
			self.bus.write_byte_data(self.address, SWITCH, CHANNELS[i])
			self.sensor_readings.data[i] = self.tsl2591.get_full_luminosity()[0]
		print(self.sensor_readings.data)

	
	def publish_sensors(self):
		while not rospy.is_shutdown():
			self.read_sensors()
			self.sensor_publisher.publish(self.sensor_readings)
			self.rate.sleep()
			
		rospy.spin()

if __name__ == '__main__':
	try:
		x = sensors()
		while not rospy.is_shutdown():
			x.publish_sensors()
	except rospy.ROSInterruptException:
		pass
