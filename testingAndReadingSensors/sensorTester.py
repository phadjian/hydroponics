# sensorTester.py
# Oliver Mulcahy
# input: four different sensor readings
# output: none 
# this prints out what values the reading sensor functions are providing. This is for testing purposes.
import time
import datetime


from waterLevelSim import randomWaterLevelSim
from waterLevelSim import steadyWaterLevelSim
from waterLevelReader import waterLevel

for x in range(0, 24):
	randomWater = waterLevel(randomWaterLevelSim())
	steadyWater = waterLevel(steadyWaterLevelSim())
	print "random water level:", randomWater, "steady water level:", steadyWater
	time.sleep(1)
