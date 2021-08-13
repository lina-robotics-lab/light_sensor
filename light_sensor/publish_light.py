import os
import sys

tools_root = os.path.join(os.path.dirname(__file__))
sys.path.insert(0,os.path.abspath(tools_root))

import rclpy
from rclpy.qos import QoSProfile
from rclpy.node import Node

from read_all_sensors import read_all_sensors

class light_publisher(Node):
	def __init__(self):
		super().__init__('light_publisher')
		sleep_time = 0.1
		self.timer = self.create_timer(sleep_time,self.timer_callback)
		
	def timer_callback(self):
		print('Hello World')

def main(args = sys.argv):
	rclpy.init(args=args)
	args_without_ros = rclpy.utilities.remove_ros_args(args)

	lp = light_publisher()
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
