# Gia Trinh
# This program controls the speed of the fan based on the temperature
# The fan: 12v, 4 pin, PWM fan
# Using 2N3904 as an BJT invertor and MOSFET
# Assumption input: flag = 0, 1, 2, 3
# output GPIO 14

#!/usr/bin/python

import time
import RPi.GPIO as GPIO  # Use this library

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

pwmOut = GPIO.PWM(14,200) 
pwmOut.start(0)

# Create pwmOut objectand start the PWM signal
# The .PWM() function takes 2 argument: output pin and the frequency of the PWM signal
# I set PWM signal 20000Hz

# Remember, the fan is connected to an inverter (BJT)
# so the duty cycle is the opposite

dutyCycle = 0

# Main program loop

while(1):

   time.sleep(0.2)

   dutyCycle = dutyCycle + 1

   if(dutyCycle > 100):

       dutyCycle = 0

   pwmOut.ChangeDutyCycle(100 - dutyCycle)
   
   
   
   
   