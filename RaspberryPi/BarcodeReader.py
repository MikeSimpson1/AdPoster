from pyzbar import pyzbar
import cv2
import os
import urllib.request
import json

#Pass in a path and return the info from the first Barcode that was found

def decode(path):
    # decodes all barcodes from an image
    images = getImages(path)
    for image in images:
        image = cv2.imread("C:/Users/Mike/Desktop/Projects/MarketplaceAdPoster/Images/1/" +image)
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

def getTitleAndAuthor(isbn):
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    with urllib.request.urlopen(base_api_link + isbn) as f:
        text = f.read()
    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0]["volumeInfo"]
    return [volume_info["title"],",".join(volume_info["authors"])]

isbn = decode("C:/Users/Mike/Desktop/Projects/MarketplaceAdPoster/Images/1")
print(getTitleAndAuthor(isbn))