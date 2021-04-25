# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from PIL import ImageColor
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis
trellis = NeoTrellis(i2c_bus)

# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

colors = [
    [
        ["#DD1139", "#DD125B", "#DC216E", "#E02177"], 
        ["#DD1139", "#DE226F", "#DF2373", "#E02177"], 
        ["#DD1259", "#DF2276", "#E5217F", "#D61680"], 
        ["#E02275", "#D61680", "#B81B7E", "#BA1B7E"]
    ], [
        ["#B1CB36", "#B1CB36", "#68AE4D", "#F9FFFF"], 
        ["#62B03F", "#278D4C", "#FEFEFE", "#2E9F99"], 
        ["#249A43", "#2A9B66", "#299770", "#249ED6"], 
        ["#2C9C6C", "#28996C", "#29A19B", "#249ED6"]
    ], [
        ["#333483", "#5A2877", "#87267B", "#87267B"], 
        ["#2262AC", "#313682", "#3E2D78", "#5A2877"], 
        ["#2D84C5", "#1B408C", "#303684", "#3E2D7C"], 
        ["#2E84C5", "#2262AC", "#1B408C", "#2F3686"]
    ]
]

# this will be called when button events are received
def blink(event):
    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        i = event.number
        color = ImageColor.getcolor(colors[2][i//4][i%4])
        trellis.pixels[event.number] = color
    # turn the LED off when a rising edge is detected
    elif event.edge == NeoTrellis.EDGE_FALLING:
        trellis.pixels[event.number] = OFF


for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # cycle the LEDs on startup
    color = ImageColor.getcolor(colors[1][i//4][i%4], "RGB")
    print(color)
    trellis.pixels[i] = color
    time.sleep(0.05)

for i in range(16):
    trellis.pixels[i] = OFF
    time.sleep(0.05)

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 millisecons or so
    time.sleep(0.02)
