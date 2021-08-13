import rospy
import numpy as np
import message_filters
from std_msgs.msg import Int16
import matplotlib.pyplot as plt

class subscribe_sensors():
	def __init__(self):
		self.a_array = []
		self.b_array = []
		self.c_array = []
		self.max_array = []
		self.avg_array = []

	def callback(self, a, b, c):
		a = a.data
		b = b.data
		c = c.data
		self.a_array.append(a)
		self.b_array.append(b)
		self.c_array.append(c)
		lights = np.array([a,b,c])
		maximum = np.amax(lights)
		average = np.mean(lights)
		self.max_array.append(maximum)
		self.avg_array.append(average)
		rospy.loginfo("light sensor a: %s", str(a))
		rospy.loginfo("light sensor b: %s", str(b))
		rospy.loginfo("light sensor c: %s", str(c))
		rospy.loginfo("max sensor: %s", str(maximum))
		rospy.loginfo("avg sensor: %s", str(average))


	def listener(self):
		rospy.init_node("test_sensor")
		sub_a = message_filters.Subscriber("/a/sensor_reading", Int16)
		# sub_a.registerCallback(callback_a)
		sub_b = message_filters.Subscriber("/b/sensor_reading", Int16)
		# sub_b.registerCallback(callback_b)
		sub_c = message_filters.Subscriber("/c/sensor_reading", Int16)
		# sub_c.registerCallback(callback_c)
		ts = message_filters.ApproximateTimeSynchronizer([sub_a, sub_b, sub_c], 10, 0.1, allow_headerless=True)
		ts.registerCallback(self.callback)
		rospy.spin()
		

if __name__ == '__main__':
	test = subscribe_sensors()
	test.listener()

	plt.figure(1)
	plt.plot(test.max_array, 'r', label='max')
	plt.plot(test.avg_array, 'b', label='avg')
	plt.legend()

	g = plt.figure(2)
	plt.plot(test.a_array, 'r', label='a')
	plt.plot(test.b_array, 'b', label='b')
	plt.plot(test.c_array, 'g', label='c')
	plt.legend()
	plt.show()