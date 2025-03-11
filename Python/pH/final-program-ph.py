# final program for pH
import smbus
import time

while True:
    try:
        # I2C ph_address of the EZO pH sensor
        ph_address = 0x63 # 0x61 for DO

        # Create an instance of the SMBus
        bus = smbus.SMBus(1)

        # Send the "R" command to the EZO pH sensor to request a reading
        bus.write_byte(ph_address, ord('R'))

        # Wait for the EZO pH sensor to complete the reading
        time.sleep(1.5)

        # Read the response from the EZO pH sensor
        response = bus.read_i2c_block_data(ph_address, 0x00, 7)

        # Convert the response to pH level
        ph_level = bytearray(response[1:6]).decode('utf-8')

        # Print the pH level
        print("pH level: ", ph_level)
        time.sleep(4) # gives 4s before reading again

    except Exception as error:
        print("Something went wrong! --->", error)
    except KeyboardInterrupt:
        print("\nKeyboard interrupted")