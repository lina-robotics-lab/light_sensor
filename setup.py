from setuptools import setup
from glob import glob

package_name = 'light_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
('share/' + package_name, glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tianpeng',
    maintainer_email='tzhang@g.harvard.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'listener = light_sensor.listener:main',
        'talker = light_sensor.talker:main',
	'publish_light = light_sensor.publish_light:main',
	'publish_single_light = light_sensor.publish_single_light:main',
	'publish_coef = light_sensor.publish_coef:main'
        ],
    },
)
