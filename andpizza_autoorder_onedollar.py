# Necessary imports for register_account
from selenium import webdriver
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Necessary imports for navigate_page
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Necessary imports for read
import csv

def read_and_use():
    global text_codes
    with open('pizza_codes.csv', newline='') as csvfile:
        lines = csvfile.readlines()
        text_codes = lines[0].split(',')[:-1]
    print("Your discount codes are")
    print(text_codes)
    with open('pizza_codes.csv', 'w') as csvfile:
        for number, line in enumerate(lines):
            if number != 0:
                csvfile.write(line)

def login_order_checkout():
    s = Service("webdriver/chromedriver")
    driver = webdriver.Chrome(service = s)
    # Login
    driver.get("https://order.andpizza.com/#/login")
    time.sleep(1)
    email = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[1]/div/ion-input/input'
    driver.find_element(By.XPATH, email).click()
    driver.find_element(By.XPATH, email).send_keys("EMAIL")
    next_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element(By.XPATH, next_button).click()
    time.sleep(2)
    password = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[2]/div/ion-input/input'
    driver.find_element(By.XPATH, password).click()
    driver.find_element(By.XPATH, password).send_keys("PASSWORD")
    login_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element(By.XPATH, login_button).click()
    time.sleep(3)

    # Menu
    driver.get('https://order.andpizza.com/#/menu/30/hits/100/new')
    time.sleep(3)
    get_button = '/html/body/ion-app/ng-component/ion-nav/page-hits-detail-browser/ion-footer/ion-row/ion-col[2]/button'
    driver.find_element(By.XPATH, get_button).click()
    time.sleep(3)

    # Checkout
    # Five Dollar Code
    driver.get('https://order.andpizza.com/#/review-order')
    time.sleep(8)
    insert = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row/ion-col/ion-input/input'
    driver.find_element(By.XPATH, insert).click()
    driver.find_element(By.XPATH, insert).send_keys(text_codes[5])
    apply = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row/ion-col/button'
    driver.find_element(By.XPATH, apply).click()
    time.sleep(5)

    # One Dollar Codes
    for i in range(5):
        insert = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row[' + str(i + 2) + ']/ion-col/ion-input/input'
        driver.find_element(By.XPATH, insert).click()
        driver.find_element(By.XPATH, insert).send_keys(Keys.COMMAND + "a")
        driver.find_element(By.XPATH, insert).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH, insert).send_keys(text_codes[i])
        apply = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row[' + str(i + 2) + ']/ion-col/button'
        driver.find_element(By.XPATH, apply).click()
        time.sleep(6)
    

    driver.get('https://order.andpizza.com/#/checkout')
    time.sleep(6)

def main():
    start = time.time()
    read_and_use()
    login_order_checkout()
    stop = time.time()
    print("The time of the run:", stop - start)
main()