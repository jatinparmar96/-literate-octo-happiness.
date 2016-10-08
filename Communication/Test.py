'''
Created on Oct 7, 2016

@author: Aditya
'''
from xbee import ieee
from serial import Serial

PORT = 'com4'
BAUD = 9600
x=True
ser = Serial(PORT, BAUD)
while x:
    print 'Sending.............'
    xbee = ieee(ser)
    # Send the string 'Hello World' to the module with MY set to 1
    print xbee.rx()
    x=False
    
print 'Done........'





ser.close()
