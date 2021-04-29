import time

from PIL import ImageColor
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis
trellis = NeoTrellis(i2c_bus)
instrument_layout = "chromatic"
engine = synth
encoder_control = "volume"
volume = 5
octave = 3

# colors
OFF = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 75, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# this will be called when button events are received
def instrument_switch(event):
    if instrument_layout == "chromatic":
        instrument_layout = "diatonic"
        trellis.pixels[event.number] = GREEN
    elif instrument_layout == "diatonic":
        instrument_layout = "chromatic"
        trellis.pixels[event.number] = YELLOW

def engine_switch(event):
    if engine == "synth":
        instrument_layout = "drums"
        trellis.pixels[event.number] = ORANGE
    elif engine == "drums":
        instrument_layout = "synth"
        trellis.pixels[event.number] = BLUE

def encoder_switch(event):
    if event.number == 2:
        encoder_control = "volume"
        trellis.pixels[2] = PURPLE
        trellis.pixels[3] = OFF
    elif event.number == 3:
        encoder_control = "octave"
        trellis.pixels[2] = OFF
        trellis.pixels[3] = CYAN

def send_note(event):
    i = event.number - 4
    if event.edge == NeoTrellis.EDGE_RISING: # note on, eventually
        if instrument_layout == "chromatic":
            trellis.pixels[event.number] = YELLOW
        else:
            trellis.pixels[event.number] = GREEN
        time.sleep(0.05)
        if engine == "synth":
            trellis.pixels[event.number] = BLUE
        else:
            trellis.pixels[event.number] = ORANGE
        print("Send note %d for layout %s using %s engine" % (i, instrument_layout, engine))
    elif event.edge == NeoTrellis.EDGE_FALLING: # note off
        trellis.pixels[event.number] = OFF

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    if i == 0:
        trellis.activate_key(i, NeoTrellis.EDGE_RISING)
        trellis.callbacks[i] = instrument_switch
        trellis.pixels[event.number] = YELLOW
    elif i == 1:
        trellis.activate_key(i, NeoTrellis.EDGE_RISING)
        trellis.callbacks[i] = engine_switch
        trellis.pixels[event.number] = BLUE
    elif i == 2 or i == 3:
        trellis.activate_key(i, NeoTrellis.EDGE_RISING)
        trellis.callbacks[i] = encoder_switch
        trellis.pixels[2] = PURPLE
        trellis.pixels[3] = OFF
    else:
        trellis.activate_key(i, NeoTrellis.EDGE_RISING)
        trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
        trellis.callbacks[i] = send_note

cycle = 0
while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 millisecons or so
    time.sleep(0.02)
    cycle += 1
    if cycle == 50000:
        print("cycle! instr=[%s], eng=[%s], vol=[%d], oct=[%d]" % (instrument_layout, engine, volume, octave))
        cycle = 0