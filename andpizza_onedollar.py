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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Necessary imports for qr
from PIL import Image
from pyzbar.pyzbar import decode

"""
Something to optimize performance and speed
WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, codedollar))
        )
"""

# Register Account for &pizza
def register_account():
    global driver
    s = Service("webdriver/chromedriver")
    driver = webdriver.Chrome(service = s)
    driver.get('https://order.andpizza.com/#/register')
    # First Name Input
    first_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[1]/ion-input/input'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, first_name_input))
    )
    driver.find_element(By.XPATH, first_name_input).click()
    driver.find_element(By.XPATH, first_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Last Name Input
    last_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[2]/ion-input/input'
    driver.find_element(By.XPATH, last_name_input).click()
    driver.find_element(By.XPATH, last_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Phone Number
    phone_number1 = 208
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
    time.sleep(10)    
    # Submit Register
    register_button = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[7]/ion-col/button/span'
    driver.find_element(By.XPATH, register_button).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-homepage/ion-content/div[2]/ion-grid/ion-row/ion-col[1]/home-rewards/div/div[2]/div/div[1]'))
    )
    try:
        if(("phone" in driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/p').text)):
            print("Phone Number issue. Registering Again")
            register_account() 
        else:
            print("Register Account Successful")
    except:
        print("Register Account Successful")
        
# Scrape for Pizza Discount Codes
def navigate_page():
    # Five Dollar Code
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(8)
    code5 = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[1]/offer-tile'
    time.sleep(8)
    driver.find_element(By.XPATH, code5).click()
    time.sleep(4)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all('img', class_="offer-details__qr"):
        qrfile = "qr5.png"
        urllib.request.urlretrieve(link['src'], qrfile)
    time.sleep(3)
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(4)
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(4)

    # One Dollar Codes
    for i in range(5):
        shop_rewards = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/div/ion-grid/ion-row/ion-col[1]/p'
        driver.find_element(By.XPATH, shop_rewards).click()
        time.sleep(15)
        redeem_code = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[1]/div/div/ion-grid/ion-row[3]/ion-col[1]/offer-tile/div/ion-grid/ion-row[3]/ion-col[1]/button'
        driver.find_element(By.XPATH, redeem_code).click()
        time.sleep(5)
        get_offer = '/html/body/ion-app/ion-modal/div/page-offer-details/ion-footer/button'
        driver.find_element(By.XPATH, get_offer).click()
        add = '/html/body/ion-app/ion-alert/div/div[3]/button[1]/span'
        time.sleep(3)
        driver.find_element(By.XPATH, add).click()
        time.sleep(8)
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(4)
    driver.get("https://order.andpizza.com/#/marketplace")
    time.sleep(8)

    for i in range(5):
        codedollar = '/html/body/ion-app/ng-component/ion-nav/page-marketplace/ion-content/div[2]/marketplace-wallet/div/ion-slides/div/div[1]/ion-slide[2]/div/div/ion-grid/ion-row[2]/ion-col[' + str(i+2) + ']/offer-tile/div'
        driver.find_element(By.XPATH, codedollar).click()
        time.sleep(3)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        for link in soup.find_all('img', class_="offer-details__qr"):
            qrfile = "qr" + str(i) +  ".png"
            urllib.request.urlretrieve(link['src'], qrfile)
        time.sleep(4)
        driver.get("https://order.andpizza.com/#/marketplace")
        time.sleep(8) 
    time.sleep(8)
    # driver.quit()

# Convert QR to text
def qr_code():
    global text_codes
    text_codes = []
    for i in range(6):
        text_codes.append(decode(Image.open('qr' + str(i) + '.png'))[0].data.decode('UTF-8'))
    print("Your discount codes are")
    print(text_codes)

def write():
    # Append-adds at last
    file1 = open("pizza_codes.csv", "a")  # append mode
    for codes in text_codes:
        file1.write(codes + ",")
    file1.write("\n")
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
main()