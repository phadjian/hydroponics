# wateradc.py for water level sensor
# Gia Trinh
# 05/04/2020

#!/usr/bin/python
 
import spidev
import RPi.GPIO as GPIO
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 250000 #1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  #print"Checking data in ReadChannel function:".format(data)
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
    
# Function to calculate water level fromn Milone sensor data, 
# rounded to specified number of decimal places.
def ConvertInch(data,places):
 
  # ADC Value
  # (approx) height  Volts   temp

  #    0        0    0.00		-50
  #   83        1    0.275		-22
  #  171        2    0.55		  5
  #  256        3    0.825		 33
  #  341        4    1.1		 60
  #  425        5    1.375		 88
  #  512        6    1.65		115
  #  597        7    1.925		143
  #  683        8    2.2		170
  #  768        9    2.475		198
  #  853       10    2.75		225
  #  939       11    3.025		250
  # 1023       12    3.30		280
 
  inch = (data * 12)/float(1023)
  inch = round(inch,places)
  return inch

def ConvertTemp(data,places):
 
  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp

print ""
print "Testing water level sensor"

while True: 
 	 
  channeldata_0 = ReadChannel(0)
  channeldata_1 = ReadChannel(1)
  water_temp_volts = ConvertVolts(channeldata_0,2)
  water_inch_volts = ConvertVolts(channeldata_1,2)
  water_temp = ConvertTemp(channeldata_0,2)
  water_inch = ConvertInch(channeldata_1,2)
  temp_in_f = water_temp * 9. / 5. + 32;
   
  print "--------------------------------------------"
  print("Water temperature from channel 0: {} ({}V) {} oC {} oF".format(channeldata_0,water_temp_volts,water_temp, temp_in_f))
  print("Water level from channel 1: {} ({}V) {} inch".format(channeldata_1,water_inch_volts,water_inch))
 
  # Wait before repeating loop
  time.sleep(5)

			
