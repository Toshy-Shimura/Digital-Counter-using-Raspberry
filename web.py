import network
import usocket as socket
from page import HTMLPAGE

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
            print(f"{wlan.ifconfig()}")

        else:
            print("Error")
            wlan.active(not self.active)
            pass

        self.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr)
        self.s.listen(1)
        