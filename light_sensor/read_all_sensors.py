import time
import board
import busio
import adafruit_tsl2591
import adafruit_tca9548a
import numpy as np

class sensor_reader:
	def __init__(self):
  		# Create I2C bus as normal
		self.i2c = busio.I2C(board.SCL,board.SDA)
		
		self.tca = adafruit_tca9548a.TCA9548A(self.i2c)		
	def read_all_sensors(self):
        	# Create the TCA9548A object and give it the I2C bus
		sensor_reading = []
		sensors_at_position = []
		for i in range(8):
			try:
				tsl=adafruit_tsl2591.TSL2591(self.tca[i])
				sensor_reading.append(tsl.lux)
				sensors_at_position.append(i)
			except ValueError:
				#print('Sensor Not Found at position {}'.format(i))
				pass
		print("Sensors at position"+str(sensors_at_position))
		return sensor_reading


if __name__ == '__main__':
	sr = sensor_reader()
	while True:
		print(np.mean(sr.read_all_sensors()))
		time.sleep(0.1)
