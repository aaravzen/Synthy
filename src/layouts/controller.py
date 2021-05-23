from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
from adafruit_neotrellis.multitrellis import MultiTrellis
from RPi import GPIO


'''
Layout controller: orchestrates the current button functionality and look.

Everything 
'''
clk = 17
dt = 18

class Controller:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.counter = 0
        self.clkLastState = GPIO.input(clk)
        i2c_bus = busio.I2C(SCL, SDA)
        trelli = [
            [NeoTrellis(i2c_bus, False, addr=0x2E), NeoTrellis(i2c_bus, False, addr=0x2F), NeoTrellis(i2c_bus, False, addr=0x30)],
        ]
        trellis = MultiTrellis(trelli)
    
    def set_buttons(self):
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

    def sync(self):
        self.trellis.sync()