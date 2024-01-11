# from adafruit_circuitplayground import cp

import board

import neopixel

# import random
# import time

RED = (255, 0, 0)
ORANGE = (245, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
PINK = (255, 3, 183)
BLACK = (0, 0, 0)
colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]

strip_pin = board.A1
strip_num_lights = 20
strip = neopixel.NeoPixel(strip_pin, strip_num_lights, brightness=1, auto_write=True)

i = 0

DIRECTION = 1

r = 255
g = 0
b = 0
rgb = (r, g, b)
turning_yellow = True
turning_green = False
turning_cyan = False
turning_blue = False
turning_purple = False
turning_red = False
while True:
    if turning_yellow:
        g += DIRECTION
        if g == 225:

            turning_yellow = False
            turning_green = True

    if turning_green:
        r -= DIRECTION
        if r== 0:
            turning_green = False
            turning_cyan  = True

    if turning_cyan:
        b += DIRECTION
        if b == 255:
            turning_cyan = False
            turning_blue = True

    if turning_blue:
        g -= DIRECTION
        if g == 0:
            turning_blue = False
            turning_purple = True

    if turning_purple:
        r += DIRECTION
        if r == 255:
            turning_purple = False
            turning_red = True

    if turning_red:
        b -= DIRECTION
        if b == 0:
            turning_red = False
            turning_yellow = True
    rgb = (r, g, b)
    strip.fill(rgb)
