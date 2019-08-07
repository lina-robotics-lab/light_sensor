
#!/usr/bin/env python
import smbus
import time

# Reading light sensor on TSL 2561
def read_sensor():
	# Get I2C bus
	bus = smbus.SMBus(1)

	# The TSL2561 address is 0x39 (57)

	# TSL2561 address, 0x39(57)
	# Select control register, 0x00(00) with command register, 0x80(128)
	#		0x03(03)	Power ON mode
	bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)

	# TSL2561 address, 0x39(57)
	# Select timing register, 0x01(01) with command register, 0x80(128)
	#		0x02(02)	Nominal integration time = 402ms
	bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

	time.sleep(0.5)

	# Read data back from 0x0C (12) with command register, 0x80 (128), 2 bytes
	# ch0 LSB, ch0 MSB
	data0 = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

	# Read data back from 0x0E (14) with command register, 0x80 (128), 2 bytes
	# ch1 LSB, ch1 MSB
	data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

	# Convert the data
	ch0 = data0[1] * 256 + data0[0]
	ch1 = data1[1] * 256 + data1[0]

	# Output data to screen 
	print("Full Spectrum (IR + Visible) :%d lux" %ch0)
	print("Infrared Value :%d lux" %ch1)
	print("Visible Value :%d lux" %(ch0 - ch1))

	return ch0

if __name__ == "__main__":
	read_sensor()

