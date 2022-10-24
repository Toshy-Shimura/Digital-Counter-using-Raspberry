import utime
from machine import Pin

class ultrasonic(object):

    def __init__(self, trigger, echo):
        self.trigger = Pin(trigger, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)
    
    def HCSR04(self):
        self.trigger.low()
        utime.sleep_us(2)
        
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()

        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        
        
        while self.echo.value() == 1:
            signalon = utime.ticks_us()

        self.timepass = signalon - signaloff

        self.distance = (self.timepass * 0.0343) / 2
