#!/usr/bin/env python3
#
# Raspberry Pi Rotary Encoder Class
# $Id: rotary_class.py,v 1.4 2021/04/23 08:15:57 bob Exp $
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses standard rotary encoder with push switch
# 
#

import RPi.GPIO as GPIO

class RotaryEncoder:

    CLOCKWISE=1
    ANTICLOCKWISE=2
    BUTTONDOWN=3
    BUTTONUP=4

    rotary_a = 0
    rotary_b = 0
    rotary_c = 0
    last_state = 0
    direction = 0

    # Initialise rotary encoder object
    def __init__(self,pinA,pinB,button,callback,name):
        self.pinA = pinA
        self.pinB = pinB
        self.button = button
        self.callback = callback
        self.name = name

        GPIO.setmode(GPIO.BCM)
        
        # The following lines enable the internal pull-up resistors
        # on version 2 (latest) boards
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # For version 1 (old) boards comment out the above four lines
        # and un-comment the following 3 lines
        #GPIO.setup(self.pinA, GPIO.IN)
        #GPIO.setup(self.pinB, GPIO.IN)
        #GPIO.setup(self.button, GPIO.IN)

        # Add event detection to the GPIO inputs
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event, bouncetime=200)
        return

    # Call back routine called by switch events
    def switch_event(self,switch):
        if GPIO.input(self.pinA):
            self.rotary_a = 1
        else:
            self.rotary_a = 0

        if GPIO.input(self.pinB):
            self.rotary_b = 1
        else:
            self.rotary_b = 0

        # print(str(self.rotary_a) + str(self.rotary_b))

        self.rotary_c = self.rotary_a ^ self.rotary_b
        new_state = self.rotary_a * 4 + self.rotary_b * 2 + self.rotary_c * 1
        delta = (new_state - self.last_state) % 4
        self.last_state = new_state
        event = 0

        if delta == 1:
            if self.direction == self.CLOCKWISE:
                # print "Clockwise"
                event = self.direction
            else:
                self.direction = self.CLOCKWISE
        elif delta == 3:
            if self.direction == self.ANTICLOCKWISE:
                # print "Anticlockwise"
                event = self.direction
            else:
                self.direction = self.ANTICLOCKWISE
        if event > 0:
            self.callback(event, self.name)
        return


    # Push button up event
    def button_event(self,button):
        if GPIO.input(button): 
            event = self.BUTTONUP 
        else:
            event = self.BUTTONDOWN 
        self.callback(event, self.name)
        return

    # Get a switch state
    def getSwitchState(self, switch):
        return  GPIO.input(switch)

# End of RotaryEncoder class
