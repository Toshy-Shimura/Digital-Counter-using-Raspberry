import time
from machine import Pin
from gpio_lcd import GpioLcd

lcdObj = GpioLcd(
d4_pin=Pin(21),
d5_pin=Pin(22),
d6_pin=Pin(26),
d7_pin=Pin(27),
rw_pin=Pin(19), rs_pin = Pin(18), enable_pin = Pin(20), 
num_lines=2,
num_columns=16)

dinoLeft = bytearray([0x00,0x1C,0x1D,0x0D,0x1F,0x0E,0x0A,0x1E])
dinoRight = bytearray([0x00,0x07,0x17,0x16,0x1F,0x0E,0x0A,0x0F])

lcdObj.putstr("DIGITAL COUNTER")
lcdObj.move_to(0, 1)
lcdObj.custom_char(0, dinoLeft)
lcdObj.custom_char(1, dinoRight)
lcdObj.putchar(chr(0))
lcdObj.putstr("--------------")
lcdObj.putchar(chr(1))
time.sleep(5)

led = Pin("LED", Pin.OUT)

led.on()
print("Raspberry Pi Pico W ON")

time.sleep(5)
led.off()