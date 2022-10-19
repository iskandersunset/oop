import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_login:

    def test_login(self, driver):

        print('Start TEST')

        succes_test = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CLASS_NAME, "title")))
        value_succes_test = succes_test.text
        assert value_succes_test == 'PRODUCTS'
        print('TEST PASSED\n', '=====' * 20)
        time.sleep(5)
