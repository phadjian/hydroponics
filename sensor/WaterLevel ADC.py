# From: https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx/blob/master/examples/mcp3xxx_mcp3002_single_ended_simpletest.py

import busio
import digitalio
import board
import adafruit_mcp3008.mcp3xxx_mcp3002 as MCP
from adafruit_mcp3008.analog_in import AnalogIn

# create spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create chip select
cs = digitalio.DigitalInOut(board.D5)

#create the mcp object
mcp = MCP.MCP3002(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

print("Raw ADC Value: ", chan.value)
print("ADC Voltage: " + str(chan.voltage) + "V")