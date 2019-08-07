#!/usr/bin/env python3
import rospy

from read_all_sensors import read_all_sensors

from std_msgs.msg import Int16MultiArray

class sensor():
	def __init__(self, addr):
		rospy.init_node("light_sensors", anonymous=True)
		self.sensor_publisher = rospy.Publisher("sensor_readings", Int16MultiArray, queue_size=10)
		self.sensor_readings = Int16MultiArray()
		
	def publish_sensor(self):
		self.sensor_readings.data = read_all_sensors()
		while not rospy.is_shutdown():
			self.sensor_publisher.publish(self.sensor_readings)
			self.rate.sleep()
		rospy.spin()

if __name__ == '__main__':
	print("Error Here?")
	try:
		a = sensor()
		while not rospy.Shutdown():
			a.publish_sensor()
	except rospy.ROSInterruptException:
		pass
