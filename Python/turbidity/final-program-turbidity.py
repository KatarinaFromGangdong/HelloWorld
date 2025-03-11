import time
import board
import busio
# from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

try:
    # Initialize I2C bus and analog input
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    chan = AnalogIn(ads, ADS.P0)

    # Define function to read sensor data
    def read_sensor():
        # Read sensor data
        voltage = chan.voltage
        turbidity = (3.3 - voltage) * 1000 / 3.3 # convert voltage to turbidity (NTU)

        # Return sensor data
        return turbidity

    # Continuously read and print sensor data
    while True:
        turbidity = read_sensor()
        print("Turbidity: {} NTU".format(turbidity))
        time.sleep(1)
        
except Exception as error:
    print("Something went wrong! --->", error)
except KeyboardInterrupt:
    print("\nKeyboard interrupted")
