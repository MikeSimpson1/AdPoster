from pyzbar import pyzbar
import cv2
import os
import urllib.request
import json

#Pass in a path and return the info from the first Barcode that was found

def decode(images):
    for image in images:
        image = cv2.imread("/home/mike/Desktop/Projects/Images/1/" +image)
        decoded_objects = pyzbar.decode(image)
        for obj in decoded_objects:
            return obj.data.decode('utf-8')
    return ""

def getImages(path):
    fileList = os.listdir(path)
    imgList = []
    for file in fileList:
        if file.endswith(".jpg") or file.endswith(".png"):
            imgList.append(file)
    return imgList

def getTitleAndAuthor(path):
    images = getImages(path)
    isbn = decode(images)
    if isbn == "":
        return []
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    with urllib.request.urlopen(base_api_link + isbn) as f:
        text = f.read()
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0]["volumeInfo"]
    return [volume_info["title"],",".join(volume_info["authors"])]

def generateMetaFile(path):
    info = getTitleAndAuthor(path)
    if info == []:
        return
    with open(path + '/info.txt', 'w') as f:
        for item in info:
            f.write(item + "\n")
            
def containsBarcode(imagePath):
    image = cv2.imread(imagePath)
    decoded_objects = pyzbar.decode(image)
    return decoded_objects != []

def test():
    path = "/home/mike/Desktop/Projects/Images/1"
    print(getTitleAndAuthor(path))
    generateMetaFile(path)