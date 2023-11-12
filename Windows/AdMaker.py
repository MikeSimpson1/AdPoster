from selenium import webdriver
from selenium.webdriver.common.by import By
from os import listdir
from time import sleep
import os
import json
from GoogleBookPythonWrapper import GoogleBook

CREDS_PATH = "C:/Users/Mike/Desktop/Projects/MarketplaceAdPoster/Windows/creds.txt"
DIR_PATH = "C:/Users/Mike/Desktop/Projects/MarketplaceAdPoster/Images"
IMG_PATH = DIR_PATH + "/"

def getLoginCredentials():
    with open(CREDS_PATH) as f:
        email = f.readline()
        pw = f.readline()
    return email, pw

def getBookDetails(info_path):
    with open(info_path) as f:
        b = f.readline()
    return GoogleBook(b)

def openNewTab(browser):
    browser.execute_script("window.open('https://www.facebook.com/marketplace/create/item');")
    browser.switch_to.window(browser.window_handles[-1])
    sleep(5)

def performLogin(browser):
    email, pw = getLoginCredentials()
    browser.get('https://www.facebook.com/')
    browser.find_element(By.ID, 'email').send_keys(email)
    sleep(2)
    browser.find_element(By.ID, "pass").send_keys(pw)
    browser.find_element("name", "login").click()

def fillForm(browser, dir):
    path = IMG_PATH + dir
    imgList = os.listdir(path)
    img_path = ""
    title = ""
    author = ""
    for fileName in imgList:
        if fileName.endswith(".txt"):
            title, author = getBookDetails(path + "/" + fileName)
        if fileName.endswith(".jpg"):
            img_path = img_path + path + "/" + fileName + " \n "
    img_path = img_path[:-3]
    
    browser.find_element("xpath", "//label[contains(@aria-label, 'Title')]").send_keys(title + "-" + author)
    browser.find_element("xpath", "//label[contains(@aria-label, 'Price')]").send_keys("20")
    browser.find_element("xpath", "//input[contains(@accept, 'image/*,image/heif,image/heic')]").send_keys(img_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

performLogin(browser)
sleep(3)
dirList = os.listdir(DIR_PATH)
for dir in dirList:
    openNewTab(browser)
    fillForm(browser, dir)
