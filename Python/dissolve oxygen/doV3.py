import smbus2
import time

# Define I2C address of the dissolved oxygen sensor
DO_SENSOR_ADDR = 0x61

# Define commands to read the dissolved oxygen level
READ_DO_CMD = b'R'

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Read dissolved oxygen level
bus.write_i2c_block_data(DO_SENSOR_ADDR, 0x00, READ_DO_CMD)
time.sleep(1)  # wait for the sensor to respond
response = bus.read_i2c_block_data(DO_SENSOR_ADDR, 0x00)

# Parse the response to get the dissolved oxygen level
do_level = float(response[1:6].decode("utf-8"))

# Print the dissolved oxygen level
print("Dissolved Oxygen Level: {:.2f} mg/L".format(do_level))
