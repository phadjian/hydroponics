# This script is used to test temperature and huminity sensor DHT11
# Reference: https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
# To run this script, in the terminal, type: python temp.py
#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    temp_in_f = temperature * 9. / 5. + 32;

    print 'Temp: {0:0.1f} F, {1:0.1f} C  Humidity: {2:0.1f} % '.format(temp_in_f, temperature, humidity)
    
    if temp_in_f > 70:
    	print 'flag = 1'
    elif temp_in_f <60:
    	print 'flag = 2'
    else:
    	print 'flag = 0'