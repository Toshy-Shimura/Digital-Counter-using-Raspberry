import _thread, network, utime
import usocket as socket
from web import wifi
from ultrasonic import ultrasonic
from machine import Pin, ADC
from gpio_lcd import GpioLcd
from page import HTMLPAGE

count = 0

ultra = ultrasonic(2, 3)
internal_led = Pin("LED", Pin.OUT)
lcdObj = GpioLcd(
d4_pin=Pin(21),
d5_pin=Pin(22),
d6_pin=Pin(26), 
d7_pin=Pin(27),
rw_pin=Pin(19), rs_pin = Pin(18), enable_pin = Pin(20), 
num_lines=2,
num_columns=16)

#pageObj = page("index.html")
dinoLeft = bytearray([0x00,0x1C,0x1D,0x0D,0x1F,0x0E,0x0A,0x1E])
dinoRight = bytearray([0x00,0x07,0x17,0x16,0x1F,0x0E,0x0A,0x0F])

lcdObj.move_to(0, 0)
lcdObj.putstr("DIGITAL COUNTER")
lcdObj.move_to(0, 1)


wifiObj = wifi("YOURWIFINAME", "YOURWIFIPASS", True)


def core1():

    while(True):

        global count
        
        ultra.HCSR04()
        
        if ultra.distance < 15:
            count=count+1
            print(f"Count: {count}")
            lcdObj.move_to(0, 1)
            lcdObj.putstr(f"Count: {count}")
            while ultra.distance < 15:
                ultra.HCSR04()
                utime.sleep_ms(50)

def core2():
    wifiObj.connect()

    while True:
            pageObj = HTMLPAGE(counter = count)
            cl, wifiObj.addr = wifiObj.s.accept()
            cl_file = cl.makefile('rwb', 0)
            while True:
                line = cl_file.readline()
                if not line or line == b'\r\n':
                    break
            response = pageObj.page()
            
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()

_thread.start_new_thread(core1, ())

core2()