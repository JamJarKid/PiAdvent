from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)


while True:
    
    time.sleep(0.5)
    
    if button1.value() == 1:
        print('left')
        
        green.toggle()
    
    elif button2.value() == 1:
        print('middle')
        
        amber.toggle()
        
    elif button3.value() == 1:
        print('right')
        
        red.toggle()
    