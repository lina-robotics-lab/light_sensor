#!/usr/bin/env python

import rospy
import time
import smbus
from std_msgs.msg import Int16

class sensor():
	def __init__(self, addr):
		rospy.init_node("light_sensor", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_reading", Int16, queue_size=10)
		self.rate = rospy.Rate(10)
		# Get I2C bus
		self.bus = smbus.SMBus(1)

		# The TSL2561 default address is 0x39 (57)
		self.addr = addr

		# Select control register, 0x00(00) with command register, 0x80(128)
		#		0x03(03)	Power ON mode
		self.bus.write_byte_data(addr, 0x00 | 0x80, 0x03)

		# Select timing register, 0x01(01) with command register, 0x80(128)
		#		0x02(02)	Nominal integration time = 402ms
		self.bus.write_byte_data(addr, 0x01 | 0x80, 0x02)
		time.sleep(0.5)

	def read_sensor(self):
		# Read data back from 0x0C (12) with command register, 0x80 (128), 2 bytes
		# ch0 LSB, ch0 MSB
		data0 = self.bus.read_i2c_block_data(self.addr, 0x0C | 0x80, 2)

		# Read data back from 0x0E (14) with command register, 0x80 (128), 2 bytes
		# ch1 LSB, ch1 MSB
		data1 = self.bus.read_i2c_block_data(self.addr, 0x0E | 0x80, 2)

		# Convert the data
		ch0 = data0[1] * 256 + data0[0]
		ch1 = data1[1] * 256 + data1[0]

		# Output data to screen 
		print("Full Spectrum (IR + Visible) :%d lux" %ch0)
		print("Infrared Value :%d lux" %ch1)
		print("Visible Value :%d lux" %(ch0 - ch1))

		return ch0
	
	def publish_sensor(self):
		while not rospy.is_shutdown():
			sensor_reading = self.read_sensor()
			self.sensor_publisher.publish(sensor_reading)
			self.rate.sleep()
		rospy.spin()

if __name__ == '__main__':
	try:
		x = sensor(0x29)
		x.publish_sensor()
	except rospy.ROSInterruptException:
		pass
