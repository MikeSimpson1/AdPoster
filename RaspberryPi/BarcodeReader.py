from pyzbar import pyzbar
import cv2
import os
import json
#import cv2.barcode as barcode
from GoogleBookPythonWrapper import GoogleBook

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
        return "", []
    b = GoogleBook(isbn)
    return b

def generateMetaFile(path):
    book = getTitleAndAuthor(path)
    if book.getTitle() == "" or book.getAuthor() == []:
        return
    with open(path + '/info.txt', 'w') as f:
        f.write(json.dumps(book.__dict__))
            
def containsBarcode(image):
    return pyzbar.decode(image) != []
    #ret_val, decoded_objects, _, _ = barcode.BarcodeDetector().detectAndDecode(image)
    #return ret_val

def writeToFile(book):
    with open('C:/Users/Mike/Desktop/info.txt', 'w') as f:
        f.write(json.dumps(book.__dict__))

def test():
    writeToFile(GoogleBook('9781668016138'))
    #path = "C:/Users/Mike/Desktop/Projects/Images/1"
    #print(getTitleAndAuthor(path))
    #generateMetaFile(path)
#test()
