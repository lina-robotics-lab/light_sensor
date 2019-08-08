#!/usr/bin/env python3
import rospy
from read_all_sensors import read_all_sensors
from std_msgs.msg import Float32MultiArray

class sensor():
	def __init__(self):
		self.node = rospy.init_node("light_sensors", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_readings", Float32MultiArray, queue_size=10)
		self.sensor_readings = Float32MultiArray()
		
	def publish_sensor(self):
		while not rospy.is_shutdown():
			try:
				self.sensor_readings.data = read_all_sensors()
			except RuntimeError as e:
				print(e)
			print(self.sensor_readings.data)
			self.sensor_publisher.publish(self.sensor_readings)


if __name__ == '__main__':
	try:
		print("Error Here?")
		a = sensor()
		while not rospy.is_shutdown():
			a.publish_sensor()
	except rospy.ROSInterruptException:
		pass
