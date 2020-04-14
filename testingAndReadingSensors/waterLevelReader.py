# waterLevelReader.py
# Oliver Mulcahy
# input: digital voltage
# output: integer (water level in inches)
# converts the voltage into inches using the manufactuer provided formula

# the max value on the water level sensor is 12in, so I assume that the voltage should be divided by 12
divValue = 85

def waterLevel(voltage):
	return voltage / divValue
