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
from tempHumidityReader import randomTempHumidity
from tempHumidityReader import steadyTempHumidity

for x in range(0, 24):
	randomWater = waterLevel(randomWaterLevelSim())
	steadyWater = waterLevel(steadyWaterLevelSim())
	randomTemp, randomHumidity = randomTempHumidity()
	steadyTemp, steadyHumidity = steadyTempHumidity()
	print "random water level:", randomWater, "steady water level:", steadyWater
	print "random temp and humidity: temperature = %0.1f, humidity = %0.1f" %(randomTemp, randomHumidity)
	print "steady temp and humidity: temperature = %0.1f, humidity = %0.1f" %(steadyTemp, steadyHumidity)
	time.sleep(1)
