from selenium import webdriver
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Register Account for &pizza
def register_account():
    global driver
    driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
    driver.get('https://order.andpizza.com/#/register')
    # First Name Input
    first_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[1]/ion-input/input'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, first_name_input))
    )
    driver.find_element_by_xpath(first_name_input).click()
    driver.find_element_by_xpath(first_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Last Name Input
    last_name_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[1]/ion-col[2]/ion-input/input'
    driver.find_element_by_xpath(last_name_input).click()
    driver.find_element_by_xpath(last_name_input).send_keys(''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
    # Phone Number
    phone_number1 = 212
    phone_number2 = random.randrange(1000000, 9999999, 1)
    phone_number = str(phone_number1) + str(phone_number2)
    phone_number_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[2]/ion-col/ion-input/input'
    driver.find_element_by_xpath(phone_number_input).click()
    driver.find_element_by_xpath(phone_number_input).send_keys(phone_number)
    # Email
    email_begin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    email_end = "@gmail.com"
    email_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[3]/ion-col/ion-input/input'
    driver.find_element_by_xpath(email_input).click()
    driver.find_element_by_xpath(email_input).send_keys(email_begin + email_end)
    # Password and Confirm
    password_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[4]/ion-col/ion-input/input'
    driver.find_element_by_xpath(password_input).click()
    password = '!@'.join(random.choice(string.ascii_uppercase + string.digits + '@' + '!') for _ in range(16))
    driver.find_element_by_xpath(password_input).send_keys(password)
    password_confirm_input = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[5]/ion-col/ion-input/input'
    driver.find_element_by_xpath(password_confirm_input).click()
    driver.find_element_by_xpath(password_confirm_input).send_keys(password)
    # DO NOT SIGN UP
    driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/notification-opt-in/div/ion-grid/ion-row[2]/ion-col/div/ion-col/ion-toggle/button').click()
    # Submit Register
    register_button = '/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[7]/ion-col/button/span'
    driver.find_element_by_xpath(register_button).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-homepage/ion-content/div[2]/ion-grid/ion-row/ion-col[1]/home-rewards/div/div[2]/div/div[1]'))
    )
    try:
        if(("phone" in driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-register/ion-content/div[2]/register-form/form/ion-grid/ion-row[6]/ion-col/p').text)):
            print("Phone Number issue. Registering Again")
            register_account() 
        else:
            print("Register Account Successful")
    except:
        print("Register Account Successful")