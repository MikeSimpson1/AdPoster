from selenium import webdriver
from os import listdir
from time import sleep
import os

DIR_PATH = os.getcwd()+"/Images"
IMG_PATH = DIR_PATH + "/"

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
    browser.find_element("xpath", "//label[contains(@aria-label, 'Title')]").send_keys("@gmail.com")
    browser.find_element("xpath", "//label[contains(@aria-label, 'Price')]").send_keys("20")
    for fileName in imgList:
        img_path = path + "/" + fileName
        browser.find_element("xpath", "//input[contains(@accept, 'image/*,image/heif,image/heic')]").send_keys(img_path)
        sleep(5)

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