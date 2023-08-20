import os
import sys 
import time
import logging
from picamera.array import PiRGBArray
import io
import numpy as np
import cv2
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

class LCD_Display():
    rawCapture = []
    disp = LCD_2inch.LCD_2inch()

    def __init__(self, camera):
        self.rawCapture = PiRGBArray(camera)

    def setup(self):
        self.disp.Init()
        self.disp.clear()
    
    def display(self):
        image = self.rawCapture.array
        image = Image.fromarray(np.uint8(image)).convert('RGB')
        image = image.resize((320,240))
        self.disp.ShowImage(image)
        self.rawCapture.seek(0)

    def close(self):
        self.disp.module_exit()