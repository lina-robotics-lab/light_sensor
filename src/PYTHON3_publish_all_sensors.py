#!/usr/bin/env python3
import busio
import board
import rospy
from PYTHON3_read_all_sensors import read_all_sensors
from std_msgs.msg import Float32MultiArray
import adafruit_tca9548a
class sensor():
	def __init__(self):
		self.node = rospy.init_node("light_sensors", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_readings", Float32MultiArray, queue_size=10)
		self.sensor_readings = Float32MultiArray()
   # Create I2C bus as normal
		self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create the TCA9548A object and give it the I2C bus
		self.tca = adafruit_tca9548a.TCA9548A(self.i2c)

		
	def publish_sensor(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			try:
				self.sensor_readings.data = read_all_sensors(self.tca)
			except RuntimeError as e:
				return
				#print(e)
			#print(self.sensor_readings.data)
			self.sensor_publisher.publish(self.sensor_readings)
			r.sleep()

if __name__ == '__main__':
	try:
		print("Starting Light Sensor Readings")
		a = sensor()
		while not rospy.is_shutdown():
			a.publish_sensor()
	except rospy.ROSInterruptException:
		pass
