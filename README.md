# hydroponics
This is a github repo for our senior design project in hydroponics.

# Code summary:
So far we just have code for the sensors. My idea is for each sensor to have a function that when ran, writes its value to a data file. We could also create a program that writes fake data to this file. Other programs, including our 'main' or potentially a web, will read data by reading in the data file.

# Sensors:
## WaterLevel ADC.py:
Uses a python library that reads SPI data from an ADC. 

## WaterLevel:
I don't think we'll be using this file. Disregard.

## temperature_code.c:
C program that prints humidity and temp.

## temperature_lcd.c:
C program that puts humidity and temp on lcd screen. 

# webapp
## app.py
python file that runs the Flask code to start a web server on the pi.

## templates:
### index.html:
used for testing

### newPage.html:
html bootstrap file that will be used to display sensor/actuator info and possibly change things
