#!/usr/bin/python
#by Philippe Akue
import RPi.GPIO as pin
import time

#This is a code to test if the press buttons works correctly.

pull_up_down = raw_input('Pull UP or DOWN resistor\n>').lower()# choose to use a pull up or down resistor
#activates a pull resitor to set a fix input voltage to an input pin
if pull_up_down == 'down':#the second pin must output 3.3V
	PUD = pin.PUD_DOWN	#pin reads low by default and high when the button is pressed
	pressed = True
elif pull_up_down == 'up':#the second pin must output 0V(ground)
	PUD = pin.PUD_UP	#pin reads high by default and low when the button is pressed
	pressed = False

#Pull up resistor is recommended when using push buttons to avoid false readings.
	
pin.setmode(pin.BCM)

s1 = 20 #38
s2 = 19 #35
s3 = 6 #31
s4 = 5 #29
s5 = 23 #16
s6 = 22 #15
s7 = 27 #13
s8 = 17 #11
pin.setup([s1,s2,s3,s4,s5,s6,s7,s8],pin.IN,pull_up_down=PUD)

print ('\nPull %s resistor') % pull_up_down

def check():
	while True:
		for i in ['s1','s2','s3','s4','s5','s6','s7','s8']:
			if pin.input(eval(i)) == pressed:#set the condition the button fufills
				print '%s pressed %s' % (i,pin.input(eval(i)))
			else:
				print '%s not pressed %s' % (i,pin.input(eval(i)))
			time.sleep(0.2)

try:
	check()	
except KeyboardInterrupt:
	pin.cleanup()
