# Imports
from machine import Pin
import time

# Set up our beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)
i=0
while True: # Run forever
    
    time.sleep(0.1) # Short delay
    
    if beam.value() == 0: # If the beam is broken
        i+=1
        print("Beam Broken!"+ str(i))
