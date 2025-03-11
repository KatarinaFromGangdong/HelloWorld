import smbus2
import time

# I2C address of the dissolved oxygen sensor
DO_SENSOR_ADDR = 0x61

# Command to read the dissolved oxygen level
DO_READ_CMD = b'R'

# Initialize the I2C bus
bus = smbus2.SMBus(1)

# Send the read command to the dissolved oxygen sensor
bus.write_i2c_block_data(DO_SENSOR_ADDR, 0x00, DO_READ_CMD)

# Wait for the sensor to respond
time.sleep(1)

# Read the response from the sensor
response = bus.read_i2c_block_data(DO_SENSOR_ADDR, 0x00)

# Convert the response to a floating point value
dissolved_oxygen = float(response[1:6].decode('utf-8'))

# Print the dissolved oxygen level
print(f"Dissolved Oxygen Level: {dissolved_oxygen:.2f} mg/L")
