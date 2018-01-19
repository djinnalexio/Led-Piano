#!/usr/bin/python
<<<<<<< HEAD

"By Andre Akue"

import RPi.GPIO as GPIO
=======
#by Philippe Akue
import RPi.GPIO as pin
>>>>>>> 3292f895d66b079da5649a77fe4ece413e1dcbae
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

<<<<<<< HEAD
pull_up_down = raw_input("Choose between a pull 'UP' or 'DOWN' resistor\n>").lower()
=======
#This is a code to test if the press buttons works correctly.

pull_up_down = raw_input('Pull UP or DOWN resistor\n>').lower()# choose to use a pull up or down resistor
>>>>>>> 3292f895d66b079da5649a77fe4ece413e1dcbae
#activates a pull resitor to set a fix input voltage to an input pin
print ('\nPull %s resistor') % pull_up_down
if pull_up_down == 'down': #with a pull down resistor, the second pin must a 3.3V output
	PUD = GPIO.PUD_DOWN	#pin reads low by default and high when the button is pressed
	pressed = True
<<<<<<< HEAD
elif pull_up_down == 'up': #with a pull up resistor, the second pin must be ground
	PUD = GPIO.PUD_UP	#pin reads high by default and low when the button is pressed
	pressed = False
else:
	print "not a resistor"
	exit()
class switches:
	def __init__(self,name,pin):
		self.name = name
		self.pin = pin
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=PUD)
=======
elif pull_up_down == 'up':#the second pin must output 0V(ground)
	PUD = pin.PUD_UP	#pin reads high by default and low when the button is pressed
	pressed = False

#Pull up resistor is recommended when using push buttons to avoid false readings.
	
pin.setmode(pin.BCM)
>>>>>>> 3292f895d66b079da5649a77fe4ece413e1dcbae

	def check(self):
		if GPIO.input(self.pin) == pressed:#set the condition the button fufills
			print "{0} is pressed, reading {1}".format(self.name,GPIO.input(self.pin))
		else:
			print "{0} is not pressed, reading {1}".format(self.name,GPIO.input(self.pin))

try:
	s1 = switches('Button 1', 20)
	s2 = switches('Button 2', 19)
	s3 = switches('Button 3', 6)
	s4 = switches('Button 4', 5)
	s5 = switches('Button 5', 23)
	s6 = switches('Button 6', 22)
	s7 = switches('Button 7', 27)
	s8 = switches('Button 8', 17)

	while 1:
		for i in [s1,s2,s3,s4,s5,s6,s7,s8]:
			i.check()
			time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
