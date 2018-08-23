#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from base64 import b64decode
from io import BytesIO
import time
import telegram
import os
import datetime


def findGift():
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/live-app/div/div/div/div/gifts-outlet/div/gift/div/div/div[4]/button")
        print("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"]: найден подарок")
    except NoSuchElementException:
        print("[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"]: пусто")
        return False
    return True

print("Start")

bot = telegram.Bot(token=os.environ['TOKEN'])
login = os.environ['LOGIN']
password =  os.environ['PASSWORD']
chat_id = os.environ['CHAT_ID']

options = Options()
options.add_argument("--headless")

binary = FirefoxBinary('/usr/lib/firefox/firefox')

#driver = webdriver.Remote("http://selenium:4444/wd/hub", desired_capabilities=options.to_capabilities())
driver = webdriver.Firefox(firefox_options=options, firefox_binary=binary)
driver.implicitly_wait(30)


driver.get("https://live.ru.lolesports.com/")



driver.find_element_by_xpath("/html/body/div[1]/welcome-popup/div/slider/button").click()

driver.find_element_by_xpath('//*[@id="riotbar-account"]/a[2]').click()

driver.find_element_by_xpath('//*[@id="login-form-username"]').send_keys(login)
driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login-button"]').click()

while True:
    gift = findGift()
    if gift:
        time.sleep(10)
        driver.find_element_by_css_selector(".gift__button").click()
        screen = BytesIO(b64decode(driver.get_screenshot_as_base64()))
        msg = "Подарок получен" 
        print("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"]:" + msg)
        bot.send_photo(chat_id=chat_id, photo=screen)
        time.sleep(10)
        driver.find_element_by_css_selector(".gift__button").click()
    time.sleep(60)

driver.quit()
