import os
import sys
import socket

tools_root = os.path.join(os.path.dirname(__file__))
sys.path.insert(0,os.path.abspath(tools_root))

import rclpy
from rclpy.qos import QoSProfile
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray,Float32

from read_all_sensors import sensor_reader
import pickle as pkl

class light_publisher(Node):
	def __init__(self,robot_namespace,path_to_coef=None):
		super().__init__('light_publisher')
		sleep_time = 0.1
		qos = QoSProfile(depth=10)
		self.pub = self.create_publisher(Float32MultiArray,'/{}/sensor_readings'.format(robot_namespace),qos)
		self.timer = self.create_timer(sleep_time,self.timer_callback)
		self.sr = sensor_reader()
		
		self.coefs = {}
		if not path_to_coef is None:
			with open(path_to_coef,'rb') as file:
				self.coefs = pkl.load(file)
				self.coef_pub = {name:self.create_publisher(Float32,'/{}/{}'.format(robot_namespace,name),qos) for name in self.coefs.keys()}

	def timer_callback(self):

		out = Float32MultiArray()
		out.data = self.sr.read_all_sensors()

		print(out.data)
		self.pub.publish(out)

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

	lp = light_publisher(robot_namespace = socket.gethostname(),path_to_coef = path_to_coef)
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
