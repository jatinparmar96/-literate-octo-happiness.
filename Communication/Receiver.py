'''
Created on Oct 7, 2016

@author: Aditya
'''
from xbee import ZigBee
from serial import Serial

PORT = 'com3'
BAUD = 9600
x=True
ser = Serial(PORT, BAUD)
while x:
    print 'Sending.............'
    xbee = ZigBee(ser)
    # Send the string 'Hello World' to the module with MY set to 1
    xbee.tx(dest_addr='\x48\xAF', data='Hello from Coordinator')
    x=False
    
print 'Done........'





ser.close()
