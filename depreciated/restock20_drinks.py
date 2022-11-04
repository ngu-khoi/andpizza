# Necessary imports for register_account
from selenium import webdriver
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Necessary imports for navigate_page
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Necessary imports for qr
from PIL import Image
from pyzbar.pyzbar import decode

# Register Account for &pizza
def register_account():
    global driver
    s = Service("C:/webdriver/chromedriver.exe")
    driver = webdriver.Chrome(service = s)
    driver.get('https://order.andpizza.com/#/register')
    # First Name Input
    first_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[1]/ion-input/input'
    time.sleep(8)
    driver.find_element(By.XPATH, first_name_input).click()
    driver.find_element(By.XPATH, first_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Last Name Input
    last_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[2]/ion-input/input'
    driver.find_element(By.XPATH, last_name_input).click()
    driver.find_element(By.XPATH, last_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Phone Number
    phone_number1 = 212
    phone_number2 = random.randrange(1000000, 9999999, 1)
    phone_number = str(phone_number1) + str(phone_number2)
    phone_number_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[2]/ion-col/ion-input/input'
    driver.find_element(By.XPATH, phone_number_input).click()
    driver.find_element(By.XPATH, phone_number_input).send_keys(phone_number)
    # Email
    email_begin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    email_end = "@gmail.com"
    email_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[3]/ion-col/ion-input/input'
    driver.find_element(By.XPATH, email_input).click()
    driver.find_element(By.XPATH, email_input).send_keys(email_begin + email_end)
    # Password and Confirm
    password_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[4]/ion-col/ion-input/input'
    driver.find_element(By.XPATH, password_input).click()
    password = '!@'.join(random.choice(string.ascii_uppercase + string.digits + '@' + '!') for _ in range(16))
    driver.find_element(By.XPATH, password_input).send_keys(password)
    password_confirm_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[5]/ion-col/ion-input/input'
    driver.find_element(By.XPATH, password_confirm_input).click()
    driver.find_element(By.XPATH, password_confirm_input).send_keys(password)
    # DO NOT SIGN UP
    driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/notification-opt-in/div/ion-grid/ion-row[2]/ion-col/div/ion-col/ion-toggle/button').click()
    # Submit Register
    register_button = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[7]/ion-col/button/span'
    driver.find_element(By.XPATH, register_button).click()
    time.sleep(8)
    try:
        if(("phone" in driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/p').text)):
            print("Phone Number issue. Registering Again")
            register_account() 
        else:
            print("Register Account Successful")
    except:
        print("Register Account Successful")
        
# Scrape for Drink Discount Codes
def navigate_page():
    # Drink 1
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(10)
    shop_rewards = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/div/ion-grid/ion-row/ion-col[1]/p'
    driver.find_element(By.XPATH, shop_rewards).click()
    time.sleep(8)
    redeem_code = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[1]/div/div/ion-grid/ion-row[3]/ion-col[2]/offer-tile/div/ion-grid/ion-row[2]'
    driver.find_element(By.XPATH, redeem_code).click()
    time.sleep(46)
    get_offer = '/html/body/ion-app/ion-modal/div/page-offer-details/ion-footer/button'
    driver.find_element(By.XPATH, get_offer).click()
    add = '/html/body/ion-app/ion-alert/div/div[3]/button[1]/span'
    time.sleep(6)
    driver.find_element(By.XPATH, add).click()
    time.sleep(8)
    # Drink 2
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(8)
    shop_rewards = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/div/ion-grid/ion-row/ion-col[1]/p'
    driver.find_element(By.XPATH, shop_rewards).click()
    time.sleep(6)
    redeem_code = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[1]/div/div/ion-grid/ion-row[3]/ion-col[2]/offer-tile/div/ion-grid/ion-row[2]'
    driver.find_element(By.XPATH, redeem_code).click()
    time.sleep(6)
    get_offer = '/html/body/ion-app/ion-modal/div/page-offer-details/ion-footer/button'
    driver.find_element(By.XPATH, get_offer).click()
    add = '/html/body/ion-app/ion-alert/div/div[3]/button[1]/span'
    time.sleep(6)
    driver.find_element(By.XPATH, add).click()
    time.sleep(8)
    driver.get("https://order.andpizza.com/#/marketplace")
    code1 = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[2]/offer-tile/div'
    time.sleep(8)
    driver.find_element(By.XPATH, code1).click()
    time.sleep(4)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img', class_="offer-details__qr"):
        qrfile = "qr1.png"
        urllib.request.urlretrieve(link['src'], qrfile)
    driver.get("https://order.andpizza.com/#/marketplace")
    code2 = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[3]/offer-tile/div'
    time.sleep(8)
    driver.find_element(By.XPATH, code2).click()
    time.sleep(4)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img', class_="offer-details__qr"):
        qrfile = "qr2.png"
        urllib.request.urlretrieve(link['src'], qrfile)
    time.sleep(4)
    driver.quit()
    
# Convert QR to text
def qr_code():
    global text_code1
    global text_code2
    data1 = decode(Image.open('qr1.png'))
    text_code1 = data1[0].data.decode('UTF-8')
    data2 = decode(Image.open('qr2.png'))
    text_code2 = data2[0].data.decode('UTF-8')
    print("Your discount codes are")
    print(text_code1 + " " + text_code2)
    
def write():
    # Append-adds at last
    file1 = open("restock20_drinks.txt", "a")  # append mode
    file1.write("Free Drink Code: " + text_code1 + "\n")
    file1.write("Free Drink Code: " + text_code2 + "\n")
    file1.close()
    
# MAIN
def main():
    start = time.time()
    try:
        register_account()
    except:
        register_account()
    try:
        navigate_page()
    except:
        navigate_page()
    qr_code()
    write()
    stop = time.time()
    print("The time of the run:", stop - start)
   
for x in range(10):   
    main()
    print(x)