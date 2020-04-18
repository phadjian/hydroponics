# ecSim.py
# Gia Trinh
# Input: probe --> float
# Output: I2C --> float
# Input & output range: 0.07 - 500000 μS/cm
# simulate a int number from 0 to 500000

import random

def randomECSim():
	return random.randrange(0, 500000, 1)

