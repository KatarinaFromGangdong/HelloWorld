import smbus2 # For I2C communication
import time # For sleep function

# Define I2C address of the EZO pH sensor
pH_address = 0x63

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Send command to put the EZO pH sensor into measurement mode
bus.write_byte(pH_address, 0x52)

# Wait for sensor to stabilize
time.sleep(1)

# Read the response from the EZO pH sensor
response = bus.read_i2c_block_data(pH_address, 0x00)

# Parse the response to get the pH value
pH = float(response[1:6])

# Print the pH value
print("pH level: ", pH)
