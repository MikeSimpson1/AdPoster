#!/usr/bin/env python
from gpiozero import Button
import os
button = Button(21)
while True:
    if button.is_pressed:
        os.system("/home/mike/Desktop/Projects/Run.sh")
