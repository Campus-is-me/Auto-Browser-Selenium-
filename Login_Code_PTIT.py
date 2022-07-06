#Made by Campus <33333
#Telegram: @Campus_Real 
#Phone: 0337176055
from argparse import Action
import logging
from select import select
from typing_extensions import Self
from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver.v2 as uc
import time, urllib.request, shutil,random,urllib, jsons, requests, string,subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox import firefox_profile
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select

#logging by info
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def _Solution_():
    try:
        options = uc.ChromeOptions()
        options.binary_location = r'C:\Users\PC\OneDrive\Documents\Selenium\GoogleChromePortable\App\Chrome-bin\chrome.exe'
        options.add_argument('--user-data-dir=C:\\Users\\PC\\OneDrive\\Documents\\Selenium\\GoogleChromePortable\\Data\\profile')
        options.add_argument('--window-size=800,800')
        options.add_argument("--disable-web-security")
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        chromedriver_exe = r'D:\chromedriver_win32\chromedriver.exe'
        driver = uc.Chrome(executable_path=chromedriver_exe, options=options)
        time.sleep(random.randint(2, 4))

        #creat ActionChain & WebdriverWait
        Wait = WebDriverWait(driver, 10)
        Action = ActionChains(driver)

        #load website
        driver.get("https://code.ptit.edu.vn/login")
        time.sleep(random.randint(2, 4))

        #scroll to 0, 400:
        logging.info("Scroll to 400!")
        driver.execute_script('window.scrollTo(0, 400)')
        time.sleep(random.randint(2, 4))
            
        #Login Username
        logging.info("Login Username!")
        username = Wait.until(EC.presence_of_element_located((By.ID,"login__user")))
        Action.move_to_element(to_element= username).click().send_keys("MikeScrapi").perform()
        time.sleep(2)

        #Login Password
        logging.info("Login Password!")
        password = Wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        Action.move_to_element(to_element= password).click().send_keys("10052002").perform()
        time.sleep(2)

        #submit 
        logging.info("Submit!")
        submit = Wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
        Action.move_to_element(to_element= submit).click().perform()
        time.sleep(10)

        driver.quit()
        
    except TimeoutError:
        logging.info("Execution Error!")
        
#Main
if __name__ == "__main__":
    _Solution_()
