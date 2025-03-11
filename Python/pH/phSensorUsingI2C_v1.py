import smbus2
import time

# I2C address of the EZO pH sensor
ADDRESS = 0x63

# Create an instance of the SMBus
bus = smbus2.SMBus(1)

# Send the "R" command to the EZO pH sensor to request a reading
bus.write_byte(ADDRESS, ord('R'))

# Wait for the EZO pH sensor to complete the reading
time.sleep(1.5)

# Read the response from the EZO pH sensor
response = bus.read_i2c_block_data(ADDRESS, 0x00)

# Convert the response to pH level
ph_level = float(response[1:6].decode("utf-8"))

# Print the pH level
print("pH level: ", ph_level)
