#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses a standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder

# Define GPIO inputs
R1_PIN_A = 16 
R1_PIN_B = 20
R1_BUTTON = 21
R2_PIN_A = 13
R2_PIN_B = 19
R2_BUTTON = 26
R3_PIN_A = 0 
R3_PIN_B = 5
R3_BUTTON = 6

# This is the event callback routine to handle events
def switch_event(event, data):
	if event == RotaryEncoder.CLOCKWISE:
		print("%s Clockwise" % data)
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print ("%s Anticlockwise" % data)
	elif event == RotaryEncoder.BUTTONDOWN:
		print ("%s Button down" % data)
	elif event == RotaryEncoder.BUTTONUP:
		print ("%s Button up" % data)
	return

# Define the switch
r1 = RotaryEncoder(R1_PIN_A,R1_PIN_B,R1_BUTTON,switch_event,"r1")
r2 = RotaryEncoder(R2_PIN_A,R2_PIN_B,R2_BUTTON,switch_event,"r2")
r3 = RotaryEncoder(R3_PIN_A,R3_PIN_B,R3_BUTTON,switch_event,"r3")

print("Pin A "+ str(R1_PIN_A))
print("Pin B "+ str(R1_PIN_B))
print("BUTTON "+ str(R1_BUTTON))

# Listen
while True:
	time.sleep(0.5)

