import cv2 as cv
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import string
import time
import urllib.request
from PIL import Image
from pyzbar.pyzbar import decode
import pickle
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def register_account():
    global driver
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    driver.get('https://order.andpizza.com/#/register')
    first_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[1]/ion-input/input'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, first_name_input))
    )
    driver.find_element_by_xpath(first_name_input).click()
    driver.find_element_by_xpath(first_name_input).send_keys("First")
    #Last Name Input
    last_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[2]/ion-input/input'
    driver.find_element_by_xpath(last_name_input).click()
    driver.find_element_by_xpath(last_name_input).send_keys("Last")
    # Attempt to create account script
    # Phone Number
    phone_number1 = 571
    phone_number2 = random.randrange(1000000, 9999999, 1)
    phone_number = str(phone_number1) + str(phone_number2)
    phone_number_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[2]/ion-col/ion-input/input'
    driver.find_element_by_xpath(phone_number_input).click()
    driver.find_element_by_xpath(phone_number_input).send_keys(phone_number)
    # Email
    email_begin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    email_end = "@gmail.com"
    email_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[3]/ion-col/ion-input/input'
    driver.find_element_by_xpath(email_input).click()
    driver.find_element_by_xpath(email_input).send_keys(email_begin + email_end)
    # Password and Confirm
    password_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[4]/ion-col/ion-input/input'
    driver.find_element_by_xpath(password_input).click()
    driver.find_element_by_xpath(password_input).send_keys("VF@c2#@!C12C2ws")
    password_confirm_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[5]/ion-col/ion-input/input'
    driver.find_element_by_xpath(password_confirm_input).click()
    driver.find_element_by_xpath(password_confirm_input).send_keys("VF@c2#@!C12C2ws")
    # DO NOT SIGN UP
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/ion-item/ion-checkbox/button').click()
    # Submit Register
    register_button = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[7]/ion-col/button/span'
    driver.find_element_by_xpath(register_button).click()
    time.sleep(3)
    try:
        if(("phone" in driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/p').text)):
            print("Phone Number issue. Registering Again")
            register_account() 
        else:
            print("Register Account Successful")
    except:
        print("Register Account Successful")

def navigate_page():
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(3.5)
    shop_rewards = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/div/ion-grid/ion-row/ion-col[1]/p'
    driver.find_element_by_xpath(shop_rewards).click()
    time.sleep(4.5)
    redeem_code = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[1]/div/div/ion-grid/ion-row[3]/ion-col[3]/offer-tile/div/ion-grid/ion-row[3]/ion-col[1]/button'
    driver.find_element_by_xpath(redeem_code).click()
    time.sleep(3.2)
    get_offer = '/html/body/ion-app/ion-modal/div/page-offer-details/ion-footer/button'
    driver.find_element_by_xpath(get_offer).click()
    add = '/html/body/ion-app/ion-alert/div/div[3]/button[1]/span'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, add))
    )
    driver.find_element_by_xpath(add).click()
    time.sleep(6)
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(2)
    code1 = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[1]/offer-tile/div'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, code1))
    )
    driver.find_element_by_xpath(code1).click()
    time.sleep(1.8)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img', class_="offer-details__qr"):
        qrfile = "qr1.png"
        urllib.request.urlretrieve(link['src'], qrfile)
    driver.get("https://order.andpizza.com/#/marketplace")
    code2 = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[2]/offer-tile/div'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, code2))
    )
    driver.find_element_by_xpath(code2).click()
    time.sleep(1.8)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img', class_="offer-details__qr"):
        qrfile = "qr2.png"
        urllib.request.urlretrieve(link['src'], qrfile)

def qr_code():
    global text_code1
    global text_code2
    data1 = decode(Image.open('qr1.png'))
    text_code1 = data1[0].data.decode('UTF-8')
    data2 = decode(Image.open('qr2.png'))
    text_code2 = data2[0].data.decode('UTF-8')
    print("Your discount codes are")
    print(text_code1 + " " + text_code2)

def getcookie():
    str1 = "https://order.andpizza.com/#/login"
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    driver.get(str1)
    time.sleep(1)
    #Email input
    email = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[1]/div/ion-input/input'
    driver.find_element_by_xpath(email).click()
    driver.find_element_by_xpath(email).send_keys("EMAIL")
    # Next
    next_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(next_button).click()
    time.sleep(3)
    password = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[2]/div/ion-input/input'
    driver.find_element_by_xpath(password).click()
    driver.find_element_by_xpath(password).send_keys("PASSWORD")
    login_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(login_button).click()
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

def cookie():
    str1 = "https://order.andpizza.com"
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    driver.get(str1)
    time.sleep(1)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(str1)

def login_order_checkout():
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    # Login
    driver.get("https://order.andpizza.com/#/login")
    time.sleep(1)
    email = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[1]/div/ion-input/input'
    driver.find_element_by_xpath(email).click()
    driver.find_element_by_xpath(email).send_keys("EMAIL")
    next_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(next_button).click()
    time.sleep(2)
    password = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[2]/div/ion-input/input'
    driver.find_element_by_xpath(password).click()
    driver.find_element_by_xpath(password).send_keys("PASSWORD")
    login_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(login_button).click()
    time.sleep(3)

    # Menu
    driver.get('https://order.andpizza.com/#/menu/30/hits/100/new')
    time.sleep(3)
    get_button = '/html/body/ion-app/ng-component/ion-nav/page-hits-detail-browser/ion-footer/ion-row/ion-col[2]/button'
    driver.find_element_by_xpath(get_button).click()
    time.sleep(3)

    # Checkout
    driver.get('https://order.andpizza.com/#/review-order')
    time.sleep(4)
    insert = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row/ion-col/ion-input/input'
    driver.find_element_by_xpath(insert).click()
    driver.find_element_by_xpath(insert).send_keys(text_code1)
    apply = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row/ion-col/button'
    driver.find_element_by_xpath(apply).click()
    time.sleep(3)
    driver.find_element_by_xpath(insert).click()
    driver.find_element_by_xpath(insert).send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath(insert).send_keys(Keys.DELETE)
    driver.find_element_by_xpath(insert).send_keys(text_code2)
    apply = '/html/body/ion-app/ng-component/ion-nav/page-review-order/ion-content/div[2]/div/promo-code/ion-grid/ion-row[2]/ion-col/button'
    driver.find_element_by_xpath(apply).click()
    driver.get('https://order.andpizza.com/#/checkout')
    time.sleep(3)
    # Uncheck Spam
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-checkout/ion-content/div[2]/div/contact-form/form/ion-item/ion-checkbox/button/span').click()
    cred_card = '/html/body/div/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input'
    #'/html/body/ion-app/ng-component/ion-nav/page-checkout/ion-content/div[2]/div/pay-method/div/div[2]/div' 
       
    driver.find_element_by_xpath(cred_card).click()
    driver.find_element_by_xpath(cred_card).send_keys(10)
    #4847189162778161062821422193
    while(True):
        pass

def login_checkout():
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    # Login
    driver.get("https://order.andpizza.com/#/login")
    time.sleep(1)
    email = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[1]/div/ion-input/input'
    driver.find_element_by_xpath(email).click()
    driver.find_element_by_xpath(email).send_keys("EMAIL")
    next_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(next_button).click()
    time.sleep(2)
    password = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[1]/ion-col/ion-slides/div/div[1]/ion-slide[2]/div/ion-input/input'
    driver.find_element_by_xpath(password).click()
    driver.find_element_by_xpath(password).send_keys("PASSWORD")
    login_button = '/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row/ion-col/ion-grid/ion-row[3]/ion-col/login-2oath/form/ion-grid/ion-row[2]/ion-col[3]/button'
    driver.find_element_by_xpath(login_button).click()
    time.sleep(3)

    #Checkout
    driver.get('https://order.andpizza.com/#/checkout')
    time.sleep(3)
    # Uncheck Spam
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-checkout/ion-content/div[2]/div/contact-form/form/ion-item/ion-checkbox/button/span').click()
    # NEED FIX
    # driver.switch_to.frame("__privateStripeFrame" + .)
    "__privateStripeFrame88110"
    cred_card = '/html/body/div/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input'
    #'/html/body/ion-app/ng-component/ion-nav/page-checkout/ion-content/div[2]/div/pay-method/div/div[2]/div' 
    driver.find_element_by_xpath(cred_card).click()
    driver.find_element_by_xpath(cred_card).send_keys(4847189162778161062821422193)
    while(True):
        pass

def main():
    start = time.time()
    try:
        register_account()
    except:
        register_account()
    navigate_page()
    qr_code()
    #getcookie()
    #cookie()
    #login_order_checkout()
    #order()
    #login_checkout()
    stop = time.time()
    print("The time of the run:", stop - start)
main()