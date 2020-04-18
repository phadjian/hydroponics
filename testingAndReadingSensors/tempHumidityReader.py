# tempHumidityReader.py
# Nicholas Tai
# Input: Digital Signal
# Output: a float (temp), a float (humidity)
# When called returns a float of the temp and a float of the humidity that was converted from the sensors digital signal

import RPi.GPIO as GPIO
import random

from tempHumiditySim import gpioTempHumidity

#setup the input and output of GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

#check if output is high if it is create random values of temperature and humidity
def randomTempHumidity():
	output = gpioTempHumidity();
	if output == 1:
		temp = random.uniform (50, 75)
		humidity = random.uniform (0, 100)
		return temp, humidity

#check if output is high if it is create a fixed value of temperature and humidity
def steadyTempHumidity():
	output = gpioTempHumidity();
	if output == 1:
		temp = 68.8
		humidity = 50.0
		return temp, humidity

