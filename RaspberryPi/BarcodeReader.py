from pyzbar import pyzbar
import cv2
import os
from GoogleBookPythonWrapper import GoogleBook

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
        return "", []
    b = GoogleBook(isbn)
    return b.getTitle(), b.getAuthor()

def generateMetaFile(path):
    title, author = getTitleAndAuthor(path)
    if title == "" or author == []:
        return
    with open(path + '/info.txt', 'w') as f:
        f.write(title + "\n")
        f.write(author)
            
def containsBarcode(imagePath):
    image = cv2.imread(imagePath)
    decoded_objects = pyzbar.decode(image)
    return decoded_objects != []

def test():
    path = "C:/Users/Mike/Desktop/Projects/Images/1"
    print(getTitleAndAuthor(path))
    generateMetaFile(path)
test()