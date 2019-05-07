import unittest
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random


class Landing_Page(unittest.TestCase):
    def setUp(self):

        '''Fields of INIT'''
        self.driver = webdriver.Chrome('chromedriver.exe')  
        self.url = "https://qa-www.freeconferencecallhd.com/"
        self.logo_link = "//a[@title='FreeConferenceCallHD.com']"
        self.wait = WebDriverWait(self.driver, 10)

        # with open('fields.json', 'r') as conf:
        #     self.xpaths = json.load(conf)
        # self.xpaths['features']
        '''Fields of TopBar'''
        self.features = "//div[@class='navbar-collapse collapse']//a[@title='Features']"
        self.support = "//div[@class='navbar-collapse collapse']//a[@title='Support']"
        self.FAQ = "//div[@class='navbar-collapse collapse']//a[@title='FAQs']"
        self.about_us = "//div[@class='navbar-collapse collapse']//a[@title='About Us']"
        self.contact_us = "//div[@class='navbar-collapse collapse']//a[@title='Contact Us']"

        '''Fields of BottomBar'''
        self.b_features = "//div[@class='footernav']//a[@title='Features']"
        self.b_support = "//div[@class='footernav']//a[@title='Support']"
        self.b_FAQ = "//div[@class='footernav']//a[@title='FAQs']"
        self.b_about_us = "//div[@class='footernav']//a[@title='About Us']"
        self.b_contact_us = "//div[@class='footernav']//a[@title='Contact Us']"

        '''Terms'''
        self.terms = "//a[@id='termsofservice_link']"
        self.close = "//button[@class='close']"

        '''Login button'''
        self.LoginButton = "//a[@title='Log In']"

        '''Support number'''
        self.support_num = "//span[@class='phone-number']"

        '''Fields of Sign Up'''
        self.first_name = "//input[@name='first_name']"
        self.last_name = "//input[@name='last_name']"
        self.email = "//input[@name='email']"
        self.password = "//input[@name='password']"
        self.parsel_type = "//li[@class='parsley-type']"
        self.email_generator = str(random.randint(10000,100000))+ '@mail.ru'
        self.pass_generator = random.randint(100000,500000)

        '''Fields of HD Conferencing'''
        self.hd_link = "//a[@title='HD Conferencing']"
        self.setup_conf = "//a[@title='Setup Conference Call']"
        self.set_conf = "//a[@title='Set Conference Preferences']"
        self.get_call = "//a[@title='Get on the Call']"
        self.after_call = "//a[@title='After the Call']"
        self.back_to_top = "//a[@title='Back to top']"
        self.web_based = "//a[@title='Web-Based Commands']"
        self.phone_keypad = "//a[@title='Phone Keypad Commands']"
        self.trouble_ticket = "//a[@title='Trouble Ticket']"
        self.voip = "//a[@title='VoIP Dialer']"

        '''International'''
        self.international_button = "//a[@title='International']"

        '''Web Controls'''
        self.web_contrl_button = "//a[@title='Web Controls']"

        '''Store Field'''
        self.appStore = "//a[@title='Download FreeConferenceCallhd.com mobile app for iOS on the App Store']"
        self.googlePlay = "//a[@title='Download the FreeConferenceCallHD.com mobile app for Android on Google Play']"


    def test_LandingPageTest(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(self.url)

        ## LogIn test ###
        self.test_LogInButton()

        ### Support number test ###
        self.test_SupportNum()

        ### Top navigation test ###
        self.test_TopNav()

        ### Logo link test ###
        self.test_LogoLink()

        ### Bottom navigation test ###
        self.test_BottomNav()

        ### Terms test ###
        self.test_Terms()

        ### Negative Sign Up ###
        self.test_SignUpNegative()

        ### HD Links ###
        self.test_HDLink()

        ### International ###
        self.test_International()

        ### Web Controls ###
        self.test_WebControls()

        ### App Pages ###
        self.test_AppPages()


    def test_SupportNum(self):
        try:
            number = self.driver.find_element(By.XPATH, self.support_num)
            print("PASSED: Support number: " + number.text)
        except:
            print("FAILED: Support number")

    def test_LogInButton(self):
        try:
            self.driver.find_element(By.XPATH, self.LoginButton).click()
            self.driver.save_screenshot("LoginPage.png")
            self.driver.back()
            print("PASSED: Login button")
        except:
            print("FAILED: Login Button")

    def test_LogoLink(self):
        try:
            self.driver.find_element(By.XPATH, self.logo_link).click()
            print("PASSED: Logo link")
        except:
            print("FAILED: Logo link")

    def test_TopNav(self):
        try:
            self.driver.get(self.url)
            self.driver.find_element(By.XPATH, self.features).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.support).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.FAQ).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.about_us).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.contact_us).click()
            print("PASSED: Top navigation")
        except:
            print("FAILED: Top navigation")

    def test_BottomNav(self):
        try:
            self.driver.find_element(By.XPATH, self.b_features).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.b_support).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.b_FAQ).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.b_about_us).click()
            self.driver.back()
            self.driver.find_element(By.XPATH, self.b_contact_us).click()
            self.driver.back()
            self.driver.execute_script("window.scrollTo(0, 0)")
            print("PASSED: Bottom navigation")
        except:
            print("FAILED: Bottom navigation")

    def test_Terms(self):
        try:
            self.driver.find_element(By.XPATH, self.terms).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close)))
            self.driver.find_element(By.XPATH, self.close).click()
            print("PASSED: Terms")
        except:
            print("FAILED: Terms")

    def test_SignUpNegative(self):
        try:
            self.driver.find_element(By.XPATH, self.first_name).send_keys("Antonio")
            self.driver.find_element(By.XPATH, self.last_name).send_keys("Fernandos")
            self.driver.find_element(By.XPATH, self.email).send_keys(self.pass_generator)
            self.driver.find_element(By.XPATH, self.password).send_keys(self.email_generator)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.parsel_type)))
            print()
            print(("PASSED: Negative Sign Up (" + "ERROR: " + self.driver.find_element(By.XPATH, self.parsel_type).text) + ")")
        except:
            print("FAILED: Negative Sign Up")

    def test_HDLink(self):
        try:
            self.driver.find_element(By.XPATH, self.hd_link).click()
            self.driver.find_element(By.XPATH, self.set_conf).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.set_conf).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.get_call).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.after_call).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.back_to_top).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.web_based).click()
            self.driver.find_element(By.XPATH, self.phone_keypad).click()
            self.driver.find_element(By.XPATH, self.trouble_ticket).click()
            self.driver.find_element(By.XPATH, self.voip).click()
            self.driver.get(self.url)
            print("PASSED: HD Links")
        except:
            print("FAILED: HD Links")

    def test_International(self):
        try:
            self.driver.find_element(By.XPATH, self.international_button).click()
            self.driver.save_screenshot("international_page.png")
            self.driver.back()
            print("PASSED: International page")
        except:
            print("FAILED: International page")

    def test_WebControls(self):
        try:
            self.driver.find_element(By.XPATH, self.web_contrl_button).click()
            self.driver.save_screenshot("WebControlsPage.png")
            self.driver.back()
            print("PASSED: Web Controls Page")
        except:
            print("FAILED: Web Controls Page")

    def test_AppPages(self):
        try:
            self.driver.find_element(By.XPATH, self.appStore).click()
            time.sleep(5)
            hundles = self.driver.window_handles
            self.driver.switch_to.window(hundles[1])
            self.driver.save_screenshot("appstore.png")
            self.driver.switch_to.window(hundles[0])
            self.driver.find_element(By.XPATH, self.googlePlay).click()
            hundles = self.driver.window_handles
            self.driver.switch_to.window(hundles[2])
            self.driver.save_screenshot("playmarket.png")
            self.driver.switch_to.window(hundles[0])
            print("PASSED: App pages")
        except:
            print("FAILED: App pages")


def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
