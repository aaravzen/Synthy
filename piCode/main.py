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

from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
from adafruit_neotrellis.multitrellis import MultiTrellis

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

# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)
trelli = [
    [NeoTrellis(i2c_bus, False, addr=0x2E), NeoTrellis(i2c_bus, False, addr=0x2F), NeoTrellis(i2c_bus, False, addr=0x30)],
]
trellis = MultiTrellis(trelli)

# this will be called when button events are received
def blink(xcoord, ycoord, edge):
    # turn the LED on when a rising edge is detected
    if edge == NeoTrellis.EDGE_RISING:
        trellis.color(xcoord, ycoord, GREEN)
    # turn the LED off when a rising edge is detected
    elif edge == NeoTrellis.EDGE_FALLING:
        trellis.color(xcoord, ycoord, OFF)

def get_next(x, y):
    if x == 3 and y == 3:
        return 4, 0
    if x == 11 and y == 3:
        return 0, 0
    elif x == 3:
        return 0, y+1
    elif x == 11:
        return 4, y+1
    else:
        return x+1, y

def all_buttons():
    currX = 0
    currY = 0
    while True:
        yield currX, currY
        currX, currY = get_next(currX, currY)
        if currX == 0 and currY == 0:
            break

def forever():
    currX = 0
    currY = 0
    while True:
        yield currX, currY
        currX, currY = get_next(currX, currY)

for x,y in all_buttons():
    # activate rising edge events on all keys
    trellis.activate_key(x, y, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(x, y, NeoTrellis.EDGE_FALLING)
    trellis.set_callback(x, y, blink)
    trellis.color(x, y, PURPLE)
    time.sleep(0.05)

for x,y in all_buttons():
    trellis.color(x, y, OFF)
    time.sleep(0.05)

# This is the event callback routine to handle events
gen = forever()
def switch_event(event, data):
    x,y = next(gen)
    if data == "r1":
        trellis.color(x,y,RED)
    if data == "r2":
        trellis.color(x,y,BLUE)
    if data == "r3":
        trellis.color(x,y,WHITE)

	if event == RotaryEncoder.CLOCKWISE:
		print("%s Clockwise" % data)
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print ("%s Anticlockwise" % data)
	elif event == RotaryEncoder.BUTTONDOWN:
		print ("%s Button down" % data)
	elif event == RotaryEncoder.BUTTONUP:
		print ("%s Button up" % data)
	return

# Define the encoders
r1 = RotaryEncoder(R1_PIN_A,R1_PIN_B,R1_BUTTON,switch_event,"r1")
r2 = RotaryEncoder(R2_PIN_A,R2_PIN_B,R2_BUTTON,switch_event,"r2")
r3 = RotaryEncoder(R3_PIN_A,R3_PIN_B,R3_BUTTON,switch_event,"r3")

print("r1_pin_a=[%d], r1_pin_b=[%d], r1_button=[%d]," % (R1_PIN_A, R1_PIN_B, R1_BUTTON))
print("r2_pin_a=[%d], r2_pin_b=[%d], r2_button=[%d]," % (R2_PIN_A, R2_PIN_B, R2_BUTTON))
print("r3_pin_a=[%d], r3_pin_b=[%d], r3_button=[%d]," % (R3_PIN_A, R3_PIN_B, R3_BUTTON))

while True:
    # the trellis can only be read every 17 millisecons or so
    trellis.sync()
    time.sleep(0.02)
