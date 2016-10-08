import time
from SimpleCV import Camera
from qrtools import QR
x=True
cam = Camera()
#time.sleep(0.5)  # If you don't wait, the image will be dark
while x:
	img = cam.getImage()
	img.save('simplecv.png')
	myCode = QR(filename=u"/home/aditya/Desktop/Project/simplecv.png")
	if myCode.decode():
		  x=False		
		  print myCode.data
		  print myCode.data_type
		  print myCode.data_to_string()
	else:
		  print 'cannotscan!'

