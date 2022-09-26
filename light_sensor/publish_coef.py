import os
import sys
import socket

tools_root = os.path.join(os.path.dirname(__file__))
sys.path.insert(0,os.path.abspath(tools_root))

import rclpy
from rclpy.qos import QoSProfile
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

import pickle as pkl

class coef_publisher(Node):
	def __init__(self,robot_namespace,path_to_coef):
		super().__init__('coef',namespace=robot_namespace)
		self.coefs = []
		sleep_time = 0.5
		if not path_to_coef is None:
			with open(path_to_coef,'rb') as file:
				coefs = pkl.load(file)
				self.coefs = [coefs['k'],coefs['b'],coefs['C0'],coefs['C1']]
				self.pub = self.create_publisher(Float32MultiArray,'sensor_coefs',qos)
				self.timer = self.create_timer(sleep_time,self.timer_callback)
	def timer_callback(self):

		out = Float32MultiArray()
		out.data = self.coefs

		# self.get_logger().info(str(out.data))
		self.pub.publish(out)

def main(args = sys.argv):
	rclpy.init(args=args)
	args_without_ros = rclpy.utilities.remove_ros_args(args)
	path_to_coef = None
	if len(args_without_ros)>1:
		path_to_coef = args_without_ros[1]
	else:
		print("No path_to_coef is supplied!")
	cp = coef_publisher(robot_namespace = socket.gethostname(),path_to_coef = path_to_coef)
	try:
		print("Coef Publisher Up")
		rclpy.spin(cp)
	except KeyboardInterrupt:
		print("Keyboard Interrupt. Shutting Down...")
	finally:
		cp.destroy_node()
		print('Coef Publisher Node Down')
		rclpy.shutdown()
if __name__ == '__main__':
	main()
