import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random


class LP_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe') 

    def test_player(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        wait = WebDriverWait(driver, 75)
        wait_elem = WebDriverWait(driver, 10)
        count_of_errors = 0
        count_of_good = 0
        count_of_video = 0
        action = ActionChains(driver)
        # Login on page
        driver.get('https://www.freeconferencecall.com/login#login')
        driver.find_element(By.XPATH, "/html//input[@id='login_email']").send_keys('roma.sennikov@freeconferencecall.com')
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys('1234')
        driver.find_element(By.XPATH, "/html//button[@id='loginformsubmit']").click()
        ###qwe123321ewq###
        ###mkrtkv@gmail.com###

        # Go to H&R
        time.sleep(10)
        driver.find_element(By.XPATH, "//div[@id='logged-in']/div/div[2]/ul/li[2]/a[1]").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//div[@id='logged-in']/div/div[2]/ul/li[2]/ul[@role='menu']//a[@href='/profile/history']").click()
        time.sleep(5)
        # Choose type of conference
        element = driver.find_element(By.XPATH, "/html//div[@id='main']/div[@class='ember-view']/div[@class='history-record wall-section']//div[@class='col-xs-12']/div[@class='ember-view']/div/div/div[4]/div[@class='form-group']/div[@class='ember-view']/select")
        drp = Select(element)
        drp.select_by_index(1)
        search = driver.find_element(By.XPATH, "//button[@title='Search']")
        try:
            wait_elem.until(EC.element_to_be_clickable((By.XPATH,  "//button[@title='Search']")))
            search.click()
        except:
            print('Did not find search')

        time.sleep(5)

        # Click to the next page
        driver.find_element(By.XPATH, "/html//div[@id='main']/div[@class='ember-view']//nav[@class='ember-view']/ul/li[6]/a[@href='#']")
        next = driver.find_element(By.XPATH, "//li/a[text()='»']")

        # Cycle of records
        while True:
            
            driver.refresh()
            driver.execute_script("window.scrollTo(0, -1000)")
            time.sleep(10)

        # Get count of video
            count = driver.find_elements(By.XPATH, "//i[@class='fa fa-lg fa-film']")
            # print(len(count))
            for i in range(1, len(count)):
                elem = driver.find_element(By.XPATH, f"(//i[@class='fa fa-lg fa-film'])[{i}]")

                # Try get error
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-lg fa-film']")))
                    elem.click()
                except:
                    print('Element is not clickable')


                # Switch to the IFRAME of Error
                driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='embed-responsive-item']"))

                # Get error
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Reload player']")))
                    count_of_errors += 1
                    print('Error with loading')
                    driver.save_screenshot("Error" + str(count_of_errors) + ".png")
                except:
                    count_of_good += 1
                finally:
                    driver.switch_to.default_content()
                driver.find_element(By.XPATH, "//i[@title='Close']").click()
            next = driver.find_element(By.XPATH, "//a[text()='»']/ancestor::li")

            # Stop cycle
            if next.get_attribute("class") == 'next disabled':
                break

            # Void first page
            if driver.find_element(By.XPATH, "//a[text()='1']/ancestor::li").get_attribute('class') != 'active':
                next.find_element_by_xpath('a').click()

        # Result
        count_of_video += int(count_of_errors) + int(count_of_good)
        print('Count of record: ' + str(count_of_video))
        print('Errors: ' + str(count_of_errors))
        print('Passed: ' + str(count_of_good))

    #document.getElementsByClassName('fa-film').length
    #console.log($('.fa-film').length)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
