from secrets import randbits
from ssl import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json,random, string, subprocess
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing.dummy import Process, Queue
import os, pathlib, time

def crawl_retwitter_tw(driver,number,link, username):
    a= []
    hight =0
    f = open(f"crawl_retwitter_{username}.txt", "w") 
    #link = f"https://twitter.com/{usernameCrawl}/followers"
    driver.set_window_size(600,1080)
    driver.get(link)
    sleep(5)
    lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    while True:     #css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0
        try:     
            data = driver.find_elements(by=By.CSS_SELECTOR, value=".css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 [role=link]")
            for i in range (0, len(data)):
                try: 
                    if len(str(data[i].get_attribute('href'))) > 50: 
                        a.append(str(data[i].get_attribute('href')))
                        print(str(data[i].get_attribute('href')))
                except: pass
            hight = hight + 70 # +20
            driver.execute_script(f'window.scrollTo(0,{hight})')
       
            lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
           
        except: 
            hight = hight + 50
            driver.execute_script(f'window.scrollTo(0,{hight})')
      
            lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
        a = list(set(a))
        if len(a) >= number: break  
        if hight > lastHeight : break      
        
    f.write("\n".join(a))
    f.close()


#main
def Solution(profile, i):
    number = int(input("Nhập số bước nhảy(thông thường 20, 30 bước nhảy là 1k link follow r): "))
    username = str(input("Nhap username: "))
    link = str(input("Nhap link: "))
    options = uc.ChromeOptions()
    options.binary_location = r'D:\Chrome_P\GoogleChromePortable - Copy (1)\App\Chrome-bin\chrome.exe'
    options.add_argument('--user-data-dir=D:\\Chrome_P\\GoogleChromePortable - Copy (1)\\Data\\profile')
    options.add_argument('start-maximized')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    chromedriver_exe = r'D:\chromedriver_win32\chromedriver.exe'
    options.add_argument("--disable-web-security")
    # just some options passing in to skip annoying popups  
    driver = uc.Chrome(executable_path = chromedriver_exe,options=options)  # version_main allows to specify your chrome version instead of following chrome global version\
    crawl_retwitter_tw(driver, number, link, username)
    #time.sleep(3)

if __name__ == '__main__':
    try:
        Solution(1,1)
    except: 
        for i in range(0, 100):
            print("Error <3 Don't Worryyy !!!!!")
        pass