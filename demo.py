import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

class LP_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')  # Обьявление драйвера

    def test_zacebookAutorization(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://facebook.com')
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('89200323752')
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys('pereriv123')
        driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="signup"]/div/div/div[2]/div/button').click()
        time.sleep(5)
        print('>>> Facebook autorization is Passed')

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()