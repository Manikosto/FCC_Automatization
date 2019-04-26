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
        self.driver = webdriver.Chrome('chromedriver.exe')  # Обьявление драйвера

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
        # Логинимся на странице
        driver.get('https://qa-www.freeconferencecall.com/login#login')
        driver.find_element(By.XPATH, "/html//input[@id='login_email']").send_keys('mkrtkv@gmail.com')
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys('qwe123321ewq')
        driver.find_element(By.XPATH, "/html//button[@id='loginformsubmit']").click()

        # Перешли в H&R
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id='logged-in']/div/div[2]/ul/li[2]/a[1]").click()
        driver.find_element(By.XPATH, "//div[@id='logged-in']/div/div[2]/ul/li[2]/ul[@role='menu']//a[@href='/profile/history']").click()

        # Выбрали тип конференции
        element = driver.find_element(By.XPATH, "/html//div[@id='main']/div[@class='ember-view']/div[@class='history-record wall-section']//div[@class='col-xs-12']/div[@class='ember-view']/div/div/div[4]/div[@class='form-group']/div[@class='ember-view']/select")
        drp = Select(element)
        drp.select_by_index(1)
        search = driver.find_element(By.XPATH, "//button[@title='Search']")
        try:
            wait_elem.until(EC.element_to_be_clickable((By.XPATH,  "//button[@title='Search']")))
            search.click()
        except:
            print('Не нашел поиск')

        time.sleep(5)

        # Переход по странице
        driver.find_element(By.XPATH, "/html//div[@id='main']/div[@class='ember-view']//nav[@class='ember-view']/ul/li[6]/a[@href='#']")
        next = driver.find_element(By.XPATH, "//li/a[text()='»']")

        # Перебор записей
        while True:
            count_of_video += int(count_of_errors) + int(count_of_good)
            driver.refresh()
            driver.execute_script("window.scrollTo(0, -1000)")
            time.sleep(10)

        # Получаем число видео-конференций
            count = driver.find_elements(By.XPATH, "//i[@class='fa fa-lg fa-film']")
            # print(len(count))
            for i in range(1, len(count)):
                elem = driver.find_element(By.XPATH, f"(//i[@class='fa fa-lg fa-film'])[{i}]")

                # Ловим возможную ошибку по перекрытию иконки
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-lg fa-film']")))
                    elem.click()
                except:
                    print('Элемент перекрыт')


                # Переключаемся на IFRAME ошибки
                driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='embed-responsive-item']"))

                # Ловим ошибку
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Reload player']")))
                    count_of_errors += 1
                    print('Error with loading')
                    driver.save_screenshot("Error" + str(count_of_errors) + ".png")
                except:
                    count_of_good += 1
                finally:
                    driver.switch_to.default_content()
                # time.sleep(5)
                driver.find_element(By.XPATH, "//i[@title='Close']").click()
            next = driver.find_element(By.XPATH, "//a[text()='»']/ancestor::li")
            # print(next.get_attribute('class'))

            # Стопим цикл если страницы кончились
            if next.get_attribute("class") == 'next disabled':
                break

            # Обходим первую страницу
            if driver.find_element(By.XPATH, "//a[text()='1']/ancestor::li").get_attribute('class') != 'active':
                next.find_element_by_xpath('a').click()

        # Отчет
        print('Всего записей: ' + str(count_of_video))
        print('Ошибок: ' + str(count_of_errors))
        print('Выполнено: ' + str(count_of_good))

    #document.getElementsByClassName('fa-film').length
    #console.log($('.fa-film').length)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()