import os
import socket

from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
	return LaunchDescription([
			Node(package = 'light_sensor',
				executable = 'publish_light',
				),
			Node(package = 'light_sensor',
				executable = 'publish_coef',
				arguments = ['{}/coefs.pkl'.format(os.environ['HOME'])]
				),
		])
