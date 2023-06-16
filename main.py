# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# PIXEL COLORS GBR format RBG

Black = (0, 0, 0)
colors = {"Black": (0, 0, 0), "Purple": (160, 240, 32)}
# END PIXEL COLORS

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 309

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def racer(length=10, color=colors["Purple"], delay_time=0.001):
    current_length = 0
    for led in range(num_pixels):

        if current_length < length:
            current_length += 1
            pixels[led] = color

        elif led == 99:

            pixels[led] = color
            time.sleep(delay_time)

            for subled in range(current_length):
                pixels[led - current_length + subled] = colors["Black"]
                pixels.show()
                time.sleep(delay_time)

            pixels[99] = colors["Black"]
            pixels.show()

        elif current_length == length:
            pixels[led] = color
            pixels[led - current_length] = colors["Black"]

        pixels.show()
        time.sleep(delay_time)


def lights_server_link():
    while True:

        try:
            racer()

        except KeyboardInterrupt:
            break
