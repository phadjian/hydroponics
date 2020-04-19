# skeleton.py
# this will be the main entry point for our program.

# functions will be spread between here and other locations in the repo.  

if _name_ == '__main__':
	main()

def main(): ##sofia 
	print "this is the main function. This is where the user will answer what they would like to do."
	# options include: 1. simulate 2. read sensor/write actuator 3. run main loop

def simulate(): 
	print "simulate function. This is where the state machine will be run with simulated input with quicker time"
	# From here, the tester can select how they'd like to simulate input (random or realistic). 
	# Then, the tester will select how quickly to progress through time. 
	# The simulated input would then be read in, and when actuator output is set, 
	# it will be displayed as so.

def readSensorWriteActuator():
	print "this is where sensor data can be displayed, or actuator values can be written for debugging purposes"

def loop():
	print "this is where our main code will go, and can be run in real time"
	# this loop could also be run in a 'simulate' mode, where time is modified and sensor data is simulated. 
	# in 'loop' mode, the actuator data would be output to the terminal, not actually written to the hardware

def germinate(): ##paniz
	print "this is where the terminal will guide the steps towards germination"


