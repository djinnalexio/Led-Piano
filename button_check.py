#!/usr/bin/python

"By Andre Akue"

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

pull_up_down = raw_input("Choose between a pull 'UP' or 'DOWN' resistor\n>").lower()
#activates a pull resitor to set a fix input voltage to an input pin
print ('\nPull %s resistor') % pull_up_down
if pull_up_down == 'down': #with a pull down resistor, the second pin must a 3.3V output
	PUD = GPIO.PUD_DOWN	#pin reads low by default and high when the button is pressed
	pressed = True
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
	s5 = switches('Button 5', 13)
	s6 = switches('Button 6', 22)
	s7 = switches('Button 7', 27)
	s8 = switches('Button 8', 17)

	while 1:
		for i in [s1,s2,s3,s4,s5,s6,s7,s8]:
			i.check()
			time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
