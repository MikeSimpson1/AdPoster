import os
import BarcodeReader as BR

path = "/home/mike/Desktop/Projects/Images"
dirList = os.listdir(path)
for dir in dirList:
	BR.generateMetaFile(path + "/" + dir)
