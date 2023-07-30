#!/usr/bin/env python3
from gpiozero import Button
import os
button = Button(21)
while True:
    if button.is_pressed:
        os.system("/home/mike/Desktop/Projects/RaspberryPi/RPiRunSequence.sh")
