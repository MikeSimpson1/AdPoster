#!/usr/bin/env python3
from gpiozero import Button, LED
import os
button = Button(2)
led = LED(12)
led.on()
while True:
    led.on()
    if button.is_pressed:
        led.off()
        os.system("/home/mike/Desktop/Projects/RaspberryPi/RPiRunSequence.sh")
