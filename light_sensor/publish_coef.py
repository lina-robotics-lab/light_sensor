import os
import sys
import socket

tools_root = os.path.join(os.path.dirname(__file__))
sys.path.insert(0,os.path.abspath(tools_root))

import rclpy
from rclpy.qos import QoSProfile
from rclpy.node import Node
from std_msgs.msg import Float32

import pickle as pkl

class coef_publisher(Node):
	def __init__(self,robot_namespace,path_to_coef):
		super().__init__('coef_publisher')
		sleep_time = 0.1
		self.timer = self.create_timer(sleep_time,self.timer_callback)

		qos = QoSProfile(depth=10)

		self.coefs = {}
		if not path_to_coef is None:
			with open(path_to_coef,'rb') as file:
				self.coefs = pkl.load(file)
				self.coef_pub = {name:self.create_publisher(Float32,'/{}/{}'.format(robot_namespace,name),qos) for name in self.coefs.keys()}

	def timer_callback(self):
		print('Publishing Coefs')
		for name,val in self.coefs.items():
			msg = Float32()
			msg.data = val
			self.coef_pub[name].publish(msg)


def main(args = sys.argv):
	rclpy.init(args=args)
	args_without_ros = rclpy.utilities.remove_ros_args(args)
	path_to_coef = None
	if len(args_without_ros)>1:
		path_to_coef = args_without_ros[1]
	else:
		print("No path_to_coef is supplied!")
		#path_to_coef = '{}/coefs.pkl'.format(os.environ['HOME'],socket.gethostname())

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
