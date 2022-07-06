from secrets import randbits
from xml.dom.minidom import Element
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json,random, string, subprocess  
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing.dummy import Process, Queue
import os, pathlib
import time, urllib.request, requests
from selenium.webdriver.support.wait import WebDriverWait
def crawl_instagram(driver,number,linkcrawl,username ): 
    hight =0 
    a=[]
    f = open("crawl_instagram"+username+".txt", "w")
    link = linkcrawl
    driver.get(link)
    sleep(5) 
    wait = WebDriverWait(driver,60)     
    wait.until(EC.presence_of_element_located((By.XPATH,"//li[@class='Y8-fY ']//a")))
    driver.find_element(By.XPATH,"//li[@class='Y8-fY ']//a").click()

    sleep(5)

    #lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range (0,number):
        #hight = hight +200
        #if hight > lastHeight : break
        #driver.execute_script(f'window.scrollTo(0,{hight})')
        elements = driver.find_elements_by_css_selector("a[class='notranslate _0imsa ']")
        elements[1].send_keys(Keys.END)
        time.sleep(1)       
        #lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    data = driver.find_elements_by_css_selector("a[class='notranslate _0imsa ']")
    try:     
        for i in range (0, len(data)):
           a.append(str(data[i].get_attribute('href')))
    except: pass
    a = list(set(a))
    f.write("\n".join(a))
    f.close()

def crawl_youtube(driver,number,linkcrawl ): 
    hight =0 
    a=[]
    f = open(f"craw_data_youtube.txt", "w")
    link = linkcrawl
    driver.get(link)
    sleep(5)   

    lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range (0,number):
        hight = hight +200
        if hight > lastHeight : break
        driver.execute_script(f'window.scrollTo(0,{hight})')
        time.sleep(1)       
        lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    data = driver.find_elements_by_css_selector('.yt-simple-endpoint.style-scope.ytd-comment-renderer')
    try:     
        for i in range (0, len(data)):
           a.append(str(data[i].get_attribute('href')))
    except: pass
    a = list(set(a))
    f.write("\n".join(a))
    f.close()


#main
def Solution(profile, i):
    number = int(input("Nhap So Luong Instagram Can Crawl: "))
    linkcrawl = str(input("Nhap link crawl: "))
    username = str(input("Nhap username: "))
    options = uc.ChromeOptions()
    options.binary_location = r'D:\Chrome_P\GoogleChromePortable - Copy (1)\App\Chrome-bin\chrome.exe'
    options.add_argument('--user-data-dir=D:\\Chrome_P\\GoogleChromePortable - Copy (1)\\Data\\profile')
    options.add_argument('start-maximized')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    chromedriver_exe = r'D:\chromedriver_win32\chromedriver.exe'
    options.add_argument("--disable-web-security")
    # just some options passing in to skip annoying popups  
    driver = uc.Chrome(executable_path = chromedriver_exe,options=options)  # version_main allows to specify your chrome version instead of following chrome global version\
    #crawl_instagram(driver,number,linkcrawl,username)
    crawl_youtube(driver, number, linkcrawl)
    time.sleep(3)

if __name__ == '__main__':
    try:
        Solution(1,1)
    except: 
        for i in range(0, 100):
            print("Error <3 Don't Worryyy !!!!!")
        pass