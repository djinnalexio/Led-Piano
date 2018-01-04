#!/usr/bin/python
#By Philippe Akue
import RPi.GPIO as pin
pin.setmode(pin.BCM)
pin.setwarnings(True)

#Press buttons#
s1 = 20 #38 <- those commented out numbers are the physical places of the pins I use
s2 = 19 #35
s3 = 6 #31
s4 = 5 #29
s5 = 23 #16
s6 = 22 #15
s7 = 27 #13
s8 = 17 #11
all_switches = [s5,s4,s1,s2,s3,s6,s7,s8] #the list of all buttons
pin.setup(all_switches,pin.IN,pull_up_down=pin.PUD_UP)# GPIO pins set up as inputs with pull up resistors

#Lights#
left=21 #40 #left white led
yellow=16 #36
red=12 #32
blue=25 #22
green=24 #18
right=13 #33 #right white led
white= (left, right) # assign 'white' to a button to control both white leds at once
all_lights = (left, yellow, red, blue, green, right) # assign 'all_lights' to control all lights at once

all = [all_lights,white,left, yellow, red, blue, green, right] #The list of all lights, this order matters

pin.setup(all_lights,pin.OUT) #GPIO pins set up as outputs

try:
	while True:
		for i,j in zip(all_switches,all):
			if pin.input(i) == False: #when the button is pressed and the pin is connected to ground (reads 0V)
				pin.output(j,pin.HIGH)
		pin.output(all_lights,pin.LOW)
#In this loop, the buttons and lights are assigned respectively to each other.
#That's why the order of the items in the lists matter.
#('s5' turns on 'all_lights', 's4' turns on 'white', etc.)
#Also, since there is no delay between when the lights are turned on and off,
#the lights turn off as soon as the button is released.

except KeyboardInterrupt: # clean the GPIO pins and exit when Ctrl+C is pressed
	pin.cleanup()
