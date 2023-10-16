#!/usr/bin/env python
from picamera import PiCamera
from cv2 import VideoCapture, imwrite
import cv2
import time
from time import sleep
from gpiozero import Button, LED
import os
import shutil
import BarcodeReader as BR
from DisplayController import LCD_Display

isPiCamera = True
picture_root_path = "/home/mike/Desktop/Projects/Images"
current_folder = 1
extension = ".jpg"

def barcodeCheck(image):
    if BR.containsBarcode(image):
        blueLed.on()
        print("barcode detected")
        sleep(0.5)
        blueLed.off()

def takePicture():
    path = get_path_string()
    if (isPiCamera):
        camera.capture(path)
    else:
        result, image = cam.read()
        imwrite(path, image)
    return path

def current_milli_time():
    return round(time.time() * 1000)

def get_path_string():
    return picture_root_path + "/" + str(current_folder) + "/" + str(current_milli_time()) + extension

def increment_folder_name(current_folder):
    current_folder+=1
    os.mkdir(picture_root_path + "/" + str(current_folder))
    return current_folder

def initializePath(path, curr_directory):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(path)
    os.mkdir(path + "/" + str(curr_directory))
##

if (isPiCamera):
    camera = PiCamera()
    camera.start_preview()
else:
    cam = VideoCapture(0)


takePictureButton = Button(21)
newFolderButton = Button(9)
endProgramButton = Button(4)

greenLed = LED(16)
redLed = LED(14)
blueLed = LED(15)
initializePath(picture_root_path, current_folder)
greenLed.on()

LCD_Display = LCD_Display(camera)
LCD_Display.setup()

run_program = True
while run_program:
    if takePictureButton.is_pressed:
        redLed.on()
        print("takePictureButton is pressed")
        file_name = takePicture()
        print("New image save: " + file_name)
        sleep(1)
    elif newFolderButton.is_pressed:
        redLed.on()
        print("newFolderButton is pressed")
        current_folder = increment_folder_name(current_folder)
        print("New folder created: " + str(current_folder))
        sleep(1)
    elif endProgramButton.is_pressed:
        redLed.on()
        print("endProgramButton is pressed")
        run_program = False
        sleep(1)
    redLed.off()
    camera.capture(LCD_Display.rawCapture, format="rgb")
    print(barcodeCheck(LCD_Display.rawCapture.array))
    LCD_Display.display()
greenLed.off()
LCD_Display.close()
print("End")
