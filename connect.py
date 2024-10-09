from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

def get_login_info():
    login = os.environ["CHESS_USERNAME"]
    password = os.environ["CHESS_PASSWORD"]
    return login, password

def click_button(xpath):
    button = browser.find_element("xpath", xpath)
    button.click()

def fill_fields(xpath, text):
    field = browser.find_element("xpath", xpath)
    for c in text: ### simulation of input 
        field.send_keys(c)
        time.sleep(0.1)

def start_bots():
    play_button = browser.find_element("xpath", '//*[@id="sb"]/div[3]/a[2]')
    ActionChains(browser).move_to_element(play_button).perform()
    time.sleep(1)
    bots_button = browser.find_element("xpath", '//*[@id="sb"]/div[3]/div[2]/div/div[2]/a[2]')
    bots_button.click()
    time.sleep(3)

options = Options()
options.add_argument("window-size={},{}".format(1920, 1080))
browser = webdriver.Chrome(options=options)
url = "https://www.chess.com/"
browser.get(url)

###get auth_info:
try:
    login, password = get_login_info()
except:
    assert False

###login button

click_button('//*[@id="sb"]/div[3]/div[10]/a[2]')
time.sleep(3)

fill_fields('//*[@id="username-input-field"]/div/input', login)
time.sleep(1)

fill_fields('//*[@id="password-input-field"]/div/input', password)
time.sleep(1)

click_button('//*[@id="login"]')
time.sleep(3)

start_bots()

print(login_button)
