#!/usr/bin/env python
import rospy
import time
import board
import busio
import adafruit_tsl2591
import adafruit_tca9548a

from std_msgs.msg import Int16MultiArray

class sensor():
	def __init__(self, addr):
		rospy.init_node("light_sensors", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_readings", Int16MultiArray, queue_size=10)
		sensor_readings = Int16MultiArray()
		
		# Create I2C bus as normal
		i2c = busio.I2C(board.SCL, board.SDA)

		# Create the TCA9548A object and give it the I2C bus
		tca = adafruit_tca9548a.TCA9548A(i2c)

		# For each sensor, create it using the TCA9548A channel instead of the I2C object
		tsl0 = adafruit_tsl2591.TSL2591(tca[0])
		tsl1 = adafruit_tsl2591.TSL2591(tca[1])
		tsl2 = adafruit_tsl2591.TSL2591(tca[2])
		tsl3 = adafruit_tsl2591.TSL2591(tca[3])
		tsl4 = adafruit_tsl2591.TSL2591(tca[4])
		tsl5 = adafruit_tsl2591.TSL2591(tca[5])
		tsl6 = adafruit_tsl2591.TSL2591(tca[6])
		tsl7 = adafruit_tsl2591.TSL2591(tca[7])
		sensor_reading.data = [tsl0.lux, tsl1.lux, tsl2.lux, tsl3.lux, tsl4.lux, tsl5.lux, tsl6.lux, tsl7.lux]
	
	def publish_sensor(self):
		while not rospy.is_shutdown():
			self.sensor_publisher.publish(sensor_reading)
			self.rate.sleep()
		rospy.spin()

if __name__ == '__main__':
	try:
		a = sensor()
		a.publish_sensor()
	except rospy.ROSInterruptException:
		pass
