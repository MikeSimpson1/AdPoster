from selenium import webdriver
from os import listdir
from time import sleep
import os

DIR_PATH = "C:/Users/Mike/Desktop/Projects/MarketplaceAdPoster/Images"
IMG_PATH = DIR_PATH + "/"

def getBookDetails(info_path):
    with open(info_path) as f:
        lines = f.readlines()
    return lines[0], lines[1]

def openNewTab(browser):
    browser.execute_script("window.open('https://www.facebook.com/marketplace/create/item');")
    browser.switch_to.window(browser.window_handles[-1])
    sleep(5)

def performLogin(browser):
    browser.get('https://www.facebook.com/')
    browser.find_element("id", "email").send_keys("@gmail.com")
    browser.find_element("id", "pass").send_keys("aB3@")
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
browser = webdriver.Chrome(chrome_options=chrome_options)

performLogin(browser)
sleep(3)
dirList = os.listdir(DIR_PATH)
for dir in dirList:
    openNewTab(browser)
    fillForm(browser, dir)