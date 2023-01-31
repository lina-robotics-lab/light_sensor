import time
import board
import busio
import adafruit_tsl2591
#import adafruit_tca9548a
import numpy as np

class sensor_reader:
	def __init__(self):
  		# Create I2C bus as normal
		self.i2c = busio.I2C(board.SCL,board.SDA)
		
#		self.tca = adafruit_tca9548a.TCA9548A(self.i2c)		
		self.tsl = adafruit_tsl2591.TSL2591(self.i2c)
	def read_sensor(self):
        	# Create the TCA9548A object and give it the I2C bus
		sensor_reading = []
		try:
			sensor_reading.append(self.tsl.lux)
		except ValueError:
			print('Sensor Not Found')
		except RuntimeError:
			print('Sensor Not Found')
		except OSError:		
			print('Skipping Remote I/O Error. Try again next time.')

		return sensor_reading


if __name__ == '__main__':
	sr = sensor_reader()
	while True:
		print(np.mean(sr.read_sensor()))
		time.sleep(0.1)
