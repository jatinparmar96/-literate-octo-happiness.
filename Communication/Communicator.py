#! /usr/bin/python



from xbee import ZigBee
import serial

PORT = 'com4'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser)

# Continuously read and print packets
while True:
    try:
        print xbee.wait_read_frame()
        
    except KeyboardInterrupt:
        break
        
ser.close()
