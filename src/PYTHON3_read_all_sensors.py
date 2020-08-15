#!/usr/bin/env python3
import time
import board
import busio
import adafruit_tsl2591
import adafruit_tca9548a


def read_all_sensors(tca):
	sensor_reading = []
	for i in range(8):
		try:
			tsl=adafruit_tsl2591.TSL2591(tca[i])
			sensor_reading.append(tsl.lux)
		except ValueError:
			pass
			# ValueError arises normally the sensor is missing at that position.

	return sensor_reading

if __name__ == '__main__':
  # Create I2C bus as normal
	i2c = busio.I2C(board.SCL, board.SDA)

        # Create the TCA9548A object and give it the I2C bus
	tca = adafruit_tca9548a.TCA9548A(i2c)
	sensor_reading = []
	for i in range(8):
		try:
			tsl=adafruit_tsl2591.TSL2591(tca[i])
			sensor_reading.append(tsl.lux)
		except ValueError:
			print('Sensor Not Found at position {}'.format(i))
	print(sensor_reading)
	#while True:
	#	print(read_all_sensors(tca))
