#Nguyen Hoang Viet (Campus)
#tool này mình test theo cách css, còn đối với form fcfs thì cách tốt nhất là xài xpath cho nhanh, còn chuẩn tối ưu và gọn nhất vẫn là css selector
#còn form thường thì cứ css mà xài auto ít lỗi, gọn code và nâng trình mình hơn 
from multiprocessing.connection import wait
import _Campus_
from argparse import Action
import logging
from select import select
from typing_extensions import Self
from selenium import webdriver
from bs4 import BeautifulSoup
#import undetected_chromedriver.v2 as uc
import undetected_chromedriver as uc
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


def _Solution_(tele, twit):
    try:
        #option 
        options = uc.ChromeOptions()
        options.binary_location = r'C:\Users\PC\OneDrive\Documents\Selenium\Chrome_Test\GoogleChromePortable_1\App\Chrome-bin\chrome.exe'
        options.add_argument('--user-data-dir=C:\\Users\\PC\\OneDrive\\Documents\\Selenium\\Chrome_Test\\GoogleChromePortable_1\\Data\\profile')
        options.add_argument('--window-size=300,800')
        options.add_argument("--incognito") 
        options.add_argument("--disable-web-security")
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        chromedriver_exe = r'D:\chromedriver_win32\chromedriver.exe'
        driver = uc.Chrome(executable_path=chromedriver_exe, options=options)

        time.sleep(random.randint(2, 4))

        #creat ActionChain & WebdriverWait
        Wait = WebDriverWait(driver, 10)
        Action = ActionChains(driver)   
        
        #creat loop
        i = 0
        while i < 100:
            driver.get("https://docs.google.com/forms/d/1nNUg2VDqAdU1ulPnYJWXxJYwrCUyadmo2sN5o2kXKRg")
            #Enter Twitter 
            time.sleep(2)
            Twit_element = Wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[aria-labelledby=i1]')))
            Action.move_to_element(to_element=Twit_element).click().send_keys(f"@{twit[i]}").perform()
            logging.info("Twitter entered successfully")

            #Enter Telegram 
            time.sleep(1)
            Tele_element = Wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[aria-labelledby=i5]')))
            Action.move_to_element(to_element=Tele_element).click().send_keys(f'@{tele[i]}').perform()
            logging.info("Telegram username entered successfully")
            #Click button 
            time.sleep(1)
            Click_element = Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div#i13.Od2TWd.hYsg7c')))
            Action.move_to_element(to_element=Click_element).click().perform()
            logging.info("Clicked successfully")

            #Submit Form 
            time.sleep(1)
            Submit = Wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'span.l4V7wb.Fxmcue')))
            Action.move_to_element(to_element=Submit[2]).click().perform()
            logging.info("Submitted successfully")

            time.sleep(2)
        time.sleep(1000)    

    except TimeoutError:
        logging.info("Execution Error!")
        
#Main
if __name__ == "__main__":
    Tele = _Campus_._open_file_(r'C:\Users\PC\OneDrive\Documents\Data\Full_Acc_Tele\Session\user_name.txt')
    Twit = _Campus_._open_file_(r'C:\Users\PC\OneDrive\Documents\Data\Full_Acc_Tele\Session\8979_Twitter.txt')
    _Solution_(Tele, Twit)
    logging.info('Successfully <3')
