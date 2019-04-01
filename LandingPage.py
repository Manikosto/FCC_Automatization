import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random


# driver.find_element(By.XPATH(''))
class LP_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')  # Обьявление драйвера

    def test_SignUp(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        login = str(random.randint(10000,100000))+ '@mail.ru'
        password = random.randint(100000,500000)
        driver.find_element_by_xpath('//*[@id="main_email"]').send_keys(login)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="signupButton"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ember1215"]/div[3]/div[1]/div[1]/h1')
        print(driver.title)
        driver.save_screenshot("LandingPageScreenShotsResult/Login/SignUp.png")  # ScreenShot
        print('>>> Sign Up is Passed')

    # def test_login(self): #Validated login
    #     driver = self.driver
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     driver.get("https://www.freeconferencecall.com/en/us")
    #     driver.find_element_by_xpath('//*[@id="login-desktop"]').click()
    #     driver.find_element_by_xpath('//*[@id="login_email"]').clear()
    #     driver.find_element_by_xpath('//*[@id="login_email"]').click()
    #     email.send_keys('smcallacc@gmail.com')
    #     driver.find_element_by_xpath('//*[@id="password"]').send_keys('pereriv123')
    #     driver.find_element_by_xpath('//*[@id="loginformsubmit"]').click()
    #     driver.find_element_by_xpath('//*[@id="document-top"]/div[12]')
    #     ErrorLogin = driver.find_element_by_xpath('//*[@id="document-top"]/div[12]')
    #     if ErrorLogin.text == ErrorLogin.text:
    #         print(ErrorLogin.text)
    #     else:
    #         driver.save_screenshot("LandingPageScreenShotsResult/Login/login.png")  # ScreenShot
    #         print('>>> Login is Passed')


    def test_JoinMeeting(self): #Join meeting from landing

        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/a').click()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="meeting_id"]').send_keys('123')
        driver.find_element_by_xpath('//*[@id="join_popup_submit"]').click()
        time.sleep(1)
        driver.save_screenshot("LandingPageScreenShotsResult/Join_Meeting/joinmeeting.png")  # ScreenShot
        print('>>> Join Meeting is Passed')

    def test_HostMeeting(self): #Host meeting from landing
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/a').click()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/ul/li[1]/a').click()
        driver.find_element_by_xpath('//*[@id="online_meeting_email"]').send_keys('manikosto@gmail.com')
        driver.find_element_by_xpath('//*[@id="online_meeting_password"]').send_keys('pereriv123')
        driver.find_element_by_xpath('//*[@id="fccModal"]/div/div/div[3]/div/button').click()
        # try:
        #     driver.find_element_by_xpath('//*[@id="online_meeting_password"]')
        # except NoSuchElementException:
        #     print('I cant find element')
        host = driver.find_element_by_xpath('//*[@id="ember632"]/div/div/div/div[1]/div/div/div[1]/h4[1]')
        print(driver.title + host.text)
        print('>>> Host Meeting is Passed')


    def test_SupportNumber(self):  #Number of support
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        number = driver.find_element_by_xpath('//*[@id="navMain"]/div[3]/div/p/span')
        print('>>>' + number.text)
        print('>>> Support number is Passed')

    def test_SignUpAfterScrolling(self):  #SignUp test on visible
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        sign = driver.find_element_by_xpath('//*[@id="nav-signup-btn"]')
        sign.click()
        print('>>> ' + sign.text)
        print('>>> Sign Up After Scrolling is Passed')

    def test_TopBar(self):  #Top tollbar links
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[2]/a').click() #Features
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[3]/a').click() #Support
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/a[1]').click() #More
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/ul/li[3]/a').click() #Apps
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/a[1]').click() #More
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/ul/li[4]/a').click() #Abou us
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/a[1]').click() #More
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/ul/li[5]/a').click() #Contact us
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/a[1]').click() #More
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[4]/ul/li[6]/a').click() #Partner program
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/a').click() #Online meetings
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/ul/li[1]/a').click() #Host meeting
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fccModal"]/div/div/div[1]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/a').click() #Online meetings
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/ul/li[2]/a').click() #Join meeting
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fccModal"]/div/div/div[1]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/a').click()  #Free online meetings
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[5]/ul/li[4]/a').click()
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[6]/a').click()
        print(driver.title)
        driver.back()
        print('>>> Top bar navigation is Passed')

    def test_LogoLink(self):  #Top tollbar links
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.freeconferencecall.com/en/us")
        driver.find_element_by_xpath('//*[@id="navMain"]/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="document-top"]/div[2]/div[2]/div[1]/a[1]').click()
        print('>>> ' + driver.title)
        print('>>> Logo link is Passed')



    def test_FacebookAutorization(self):
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

    def test_BottomToolbar(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[1]/ul/li[1]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[1]/ul/li[2]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[1]/ul/li[3]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[1]/ul/li[4]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[2]/ul/li[1]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[2]/ul/li[1]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[2]/ul/li[3]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[2]/ul/li[4]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[3]/ul/li[1]/a').click() #
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[3]/ul/li[2]/a').click() #
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[3]/ul/li[3]/a').click() # Download
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="download-app"]/a').click()  # Get Descktop
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[4]/ul/li[1]/a').click()  # AboutUs
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[4]/ul/li[2]/a').click()  # Executives
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[4]/ul/li[3]/a').click()  # Careers
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[4]/ul/li[4]/a').click()  # ContactUs
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[5]/ul/li[1]/a').click()  # Press Center
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[5]/ul/li[2]/a').click()  # Reviews
        print(driver.title)
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[1]/div/div[5]/ul/li[3]/a').click()  # Blog
        print(driver.title)
        driver.back()
        print('>>> Bottom bar is Passed')

    def test_SocialLinks(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div/div/ul/li[1]/a').click()
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div/div/ul/li[2]/a').click()
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div/div/ul/li[3]/a').click() #YouTube
        print(driver.title)
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div/div/ul/li[4]/a').click()
        print(driver.title)
        driver.back()
        driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div/div/ul/li[5]/a').click()
        print(driver.title)
        driver.back()
        print('>>> Social links is Passed')


    def test_PrivacyPolicy(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="sitelegend"]/ul/li[1]/a').click()
        print(driver.title)
        print('>>> Privacy Policy is Passed')

    def test_SiteMap(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="sitelegend"]/ul/li[2]/a').click()
        print(driver.title)
        print('>>> Sitemap is Passed')


    def test_TermsAndConditions(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.freeconferencecall.com/en/us')
        driver.find_element_by_xpath('//*[@id="sitelegend"]/ul/li[3]/a').click()
        print(driver.title)
        print('>>> Terms And Conditions is Passed')


def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()