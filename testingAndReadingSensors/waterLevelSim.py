# waterLevelSim.py
# Oliver Mulcahy
# input: None
# output: digital resistance
# generates an int. int is voltage value in volts (0 to 1023) as if the signal was converted by the ADC. 

import random

#random adc value
def randomWaterLevelSim():
	return random.randrange(0, 1023, 1)

#steady adc value
def steadyWaterLevelSim():
	return 550
