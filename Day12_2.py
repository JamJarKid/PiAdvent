# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[0] = (255,20,147)
strip[1] = (255,20,147)
strip[2] = (255,20,147)
strip[3] = (255,20,147)
strip[4] = (255,20,147)

# Send the data to the strip
strip.write()