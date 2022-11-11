import network, utime
import usocket as socket
from page import HTMLPAGE
from gpio_lcd import GpioLcd
from machine import Pin

lcdObj = GpioLcd(
d4_pin=Pin(21),
d5_pin=Pin(22),
d6_pin=Pin(26),
d7_pin=Pin(27),
rw_pin=Pin(19), rs_pin = Pin(18), enable_pin = Pin(20), 
num_lines=2,
num_columns=16)

class wifi(object):
    def __init__(self, ssid: str, password: str, active: bool):
        self.ssid = ssid
        self.password = password
        self.active = active

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(self.active)

        wlan.connect(self.ssid, self.password)


        if wlan.isconnected():
            status = wlan.ifconfig()
            ipsend = status[0]
            print(f"{status[0]}")
            utime.sleep(1)
            lcdObj.move_to(0, 0)
            lcdObj.putstr(status[0])
        else:
            print("Error")
            wlan.active(not self.active)
            pass

        self.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr)
        self.s.listen(1)
