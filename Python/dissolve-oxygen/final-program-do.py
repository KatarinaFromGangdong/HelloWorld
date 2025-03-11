# final program for DO
import smbus
import time

while True:
    try:
        # I2C do_address of the EZO DO sensor
        do_address = 0x61  # 0x63 for pH

        # Create an instance of the SMBus
        bus = smbus.SMBus(1)

        # Send the "R" command to the EZO DO sensor to request a reading
        bus.write_byte(do_address, ord('R'))

        # Wait for the EZO DO sensor to complete the reading
        time.sleep(1.5)

        # Read the response from the EZO DO sensor
        response = bus.read_i2c_block_data(do_address, 0x00, 7)

        # Convert the response to DO level
        DO_level = bytearray(response[1:6]).decode('utf-8')

        # Print the DO level
        print("DO level: ", DO_level)
        time.sleep(4)  # gives 4s before reading again

    except Exception as error:
        print("Something went wrong! --->", error)
    except KeyboardInterrupt:
        print("\nKeyboard interrupted")
