#!/usr/bin/python

"By Andre Akue"

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

class keys:

    def __init__(self, button, led):
        self.key = button
        self.led = led
        GPIO.setup(self.key, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(self.led, GPIO.OUT, initial = 0)
        
    def press(self):
        if GPIO.input(self.key) == 0:
            GPIO.output(self.led,1)

K1 = keys(20,21)
K2 = keys(19,16)
K3 = keys(6,12)
K4 = keys(5,(21,13)) #key for both white lights
K5 = keys(23,(21,16,12,25,24,13)) #key for all lights
K6 = keys(22,25)
K7 = keys(27,24)
K8 = keys(17,13)

try:
	while True:
		for i in [K1,K2,K3,K4,K5,K6,K7,K8]:
			i.press()
		GPIO.output((K5.led),0)

except KeyboardInterrupt:
	GPIO.cleanup()
