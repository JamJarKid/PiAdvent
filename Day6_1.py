# Imports
from machine import ADC, Pin
import time

# Define pin for our sensor
lightsensor = ADC(Pin(26))

while True:
    
    light = lightsensor.read_u16()

    print(light)
    
    time.sleep(0.5)
