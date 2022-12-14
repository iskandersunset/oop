import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_1():

    def test_select_product(self):
        # s = Service('C:/Users/iskan/PycharmProjects/Selenium/chromedriver.exe')  # Путь дома
        s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
        driver = webdriver.Chrome(service=s)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        # driver.maximize_window()

        print('Start TEST')

        login_standard_user = "standard_user"
        login_password_user = "secret_sauce"

        login = Login_page(driver)
        login.authorization(login_standard_user, login_password_user)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        select_product.click()
        print('Кликнули по кнопке Add to cart')
        time.sleep(5)

        button_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        button_cart.click()
        print('Кликнули по иконке корзины')
        time.sleep(5)

        succes_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "title")))
        value_succes_test = succes_test.text
        assert value_succes_test == 'YOUR CART'
        print('TEST PASSED')
        time.sleep(5)

test = Test_1()
test.test_select_product()
