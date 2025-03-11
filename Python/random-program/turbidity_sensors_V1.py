#create a python program for raspberry pi that measures turbidity of a water using DF Robot turbidity sensor

#importing necessary libraries
import time
import RPi.GPIO as GPIO

#setting GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#defining the function to get turbidity values
def getTurbidity():
    reading = 0
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(4, GPIO.IN)
    while (GPIO.input(4) == GPIO.LOW):
        reading += 1
    return reading

#main loop
while True:
    print(getTurbidity())
    time.sleep(1)