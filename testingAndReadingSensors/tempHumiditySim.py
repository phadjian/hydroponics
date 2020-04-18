# tempHumiditySim.py
# Nicholas Tai
# Input: None
# Output: Digital Signal
# Mimic the rate and signal sent out by the temperature and humidity sensor

import RPi.GPIO as GPIO

#check if input is high if it is, set the output to high
def gpioTempHumidity():
	if GPIO.input(22) == 1:
		GPIO.output(18,1)
		return GPIO.input(18)
