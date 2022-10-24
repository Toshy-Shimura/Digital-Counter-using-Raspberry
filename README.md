# Digital counter using raspberry pico
Digital counter using ultrasonic sensor and raspberry pi pico W
* Rasberry pi pico W
* Ultrasonic Sensor HC-SR04
* LCD Display 1602  (16x2)

[TOCM]

##Requirements
                    
> [MicroPython](https://micropython.org/)


####Ampy

`$ pip install ampy`
`$ ampy --port "COM PORT" put "file"`




###Images

![](https://media.discordapp.net/attachments/891482128234197052/1033247732086886450/unknown.png?width=949&height=671)

> Diagram

###Price (US)
| Item      | Value |
| --------- | -----:|
| Raspberry Pi Pico W  | $6 |
| HC-SR04   |   $4.50 |
| LCD 1602A      |    $1.26|

###Block diagram

```flow
st=>start: 
op=>operation: Calculating distance
cond=>condition: Distance < 15cm 	Yes or No?
e=>end: Counter + 1

st->op->cond
cond(yes)->e
cond(no)->op
```

###End
