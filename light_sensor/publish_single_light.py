import os
import sys
import socket

tools_root = os.path.join(os.path.dirname(__file__))
sys.path.insert(0,os.path.abspath(tools_root))

import rclpy
from rclpy.qos import QoSProfile
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray,Float32

from read_single_sensor import sensor_reader
import pickle as pkl

class light_publisher(Node):
	def __init__(self,robot_namespace):
		super().__init__('light_publisher',namespace=robot_namespace)
		sleep_time = 0.5
		qos = QoSProfile(depth=10)
		self.pub = self.create_publisher(Float32MultiArray,'sensor_readings',qos)
		self.timer = self.create_timer(sleep_time,self.timer_callback)
		self.sr = sensor_reader()

	def timer_callback(self):

		out = Float32MultiArray()
		out.data = self.sr.read_sensor()

		# self.get_logger().info(str(out.data))
		self.pub.publish(out)


def main(args = sys.argv):
	rclpy.init(args=args)
	args_without_ros = rclpy.utilities.remove_ros_args(args)
	path_to_coef = None

	lp = light_publisher(robot_namespace = socket.gethostname())
	try:
		print("Light Publisher Up")
		rclpy.spin(lp)
	except KeyboardInterrupt:
		print("Keyboard Interrupt. Shutting Down...")
	finally:
		lp.destroy_node()
		print('Light Publisher Node Down')
		rclpy.shutdown()
if __name__ == '__main__':
	main()
