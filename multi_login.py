import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from login_page import Login_page
from test_first import Test_login

users_login = ('standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user')
users_password = 'secret_sauce'

s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

for i in range(len(users_login)):
    print('Заходим пользователем:', users_login[i])
    login = Login_page(driver)
    login.authorization(users_login[i], users_password)
    if driver.find_elements(By.CLASS_NAME, "error-button"):
        print('Логин или пароль неверен или заблокирован')
        print('TEST FAILED\n', '===' * 20)
        driver.find_element(By.CLASS_NAME, "error-button").click()
        time.sleep(3)
        driver.get(base_url)
    else:
        test = Test_login()
        test.test_login(driver, base_url)


