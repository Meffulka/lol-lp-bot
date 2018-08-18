from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
import time
from random import randint
import telegram
import os

def findGift():
    try:
        driver.find_element_by_css_selector(".gift__button")
        print("Обнаружен подарок: "+ driver.find_element_by_css_selector(".gift__title").text)
    except NoSuchElementException:
        return False
    return True

print("Start")

bot = telegram.Bot(token=os.environ['TOKEN'])
login = os.environ['LOGIN']
password =  os.environ['PASSWORD']
chat_id = os.environ['CHAT_ID']


driver = webdriver.Firefox()
driver.get("https://live.ru.lolesports.com/")
welcome = driver.find_element_by_class_name("welcome")
if welcome:
    welcome.find_element_by_class_name("slider__close").click()
driver.find_element_by_css_selector("#riotbar-account > a:nth-child(2)").click()

driver.find_element_by_css_selector("#login-form-username").send_keys(login)
driver.find_element_by_css_selector("#login-form-password").send_keys(password)
driver.find_element_by_css_selector("#login-button").click()

while True:
    gift = findGift()
    if gift:
        time.sleep(randint(10, 300))
        driver.find_element_by_css_selector(".gift__button").click()
        msg = "У " + login + " получен: "+ driver.find_element_by_css_selector(".gift__title").text
        print(msg)
        bot.sendMessage(chat_id=chat_id, text=msg)
        time.sleep(10)
        driver.find_element_by_css_selector(".gift__button").click()
    time.sleep(60)







#.gift__title