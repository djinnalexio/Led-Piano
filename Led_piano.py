#!/usr/bin/python
import RPi.GPIO as pin
pin.setmode(pin.BCM)
pin.setwarnings(True)

s1 = 20 #38
s2 = 19 #35
s3 = 6 #31
s4 = 5 #29
s5 = 23 #16
s6 = 22 #15
s7 = 27 #13
s8 = 17 #11
all_switches = [s5,s4,s1,s2,s3,s6,s7,s8]
pin.setup(all_switches,pin.IN,pull_up_down=pin.PUD_UP)

left=21 #40
yellow=16 #36
red=12 #32
blue=25 #22
green=24 #18
right=13 #33
white= (left, right)
all_lights = (left, yellow, red, blue, green, right)

all = [all_lights,white,left, yellow, red, blue, green, right]

pin.setup(all_lights,pin.OUT)

try:
	while True:
		for i,j in zip(all_switches,all):
			if pin.input(i) == False:
				pin.output(j,pin.HIGH)
		pin.output(all_lights,pin.LOW)

except KeyboardInterrupt:
	pin.cleanup()

#pin.cleanup()
