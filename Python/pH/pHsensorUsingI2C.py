import smbus2
import time

# Define I2C address of EZO pH sensor
PH_SENSOR_ADDR = 0x63

# Create an instance of the I2C bus
bus = smbus2.SMBus(1)

# Function to read the pH value from the EZO pH sensor
def read_ph():
    # Send the "R" command to the EZO pH sensor to request the pH value
    bus.write_i2c_block_data(PH_SENSOR_ADDR, 0x52, [])

    # Wait for the EZO pH sensor to respond with the pH value
    time.sleep(0.5)

    # Read the pH value from the EZO pH sensor
    data = bus.read_i2c_block_data(PH_SENSOR_ADDR, 0x00, 7)

    # Check if the response is valid
    if data[0] == 1 and data[1] == 2:
        # Convert the raw pH value to a float
        ph = float(data[2:6].decode('utf-8'))
        return ph
    else:
        print("Invalid response from EZO pH sensor")
        return None

# Main program loop
while True:
    # Read the pH value from the EZO pH sensor
    ph = read_ph()

    if ph is not None:
        # Print the pH value
        print("pH: {}".format(ph))

    # Wait for 1 second before reading again
    time.sleep(1)