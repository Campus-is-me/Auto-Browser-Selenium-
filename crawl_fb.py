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

def crawl_fb(driver,number,link,usernameCrawl):
   
    a= []
    driver.set_window_size(1000,1000)
    driver.set_window_position(0,0)
    driver.get(link)
    sleep(5)
    
    driver.find_element_by_css_selector("div[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l lzcic4wl'] span[class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']").click()
    sleep(2)    
    driver.find_element_by_css_selector("div[class='__fb-light-mode'] div:nth-child(3) div:nth-child(1) div:nth-child(1) div:nth-child(2) span:nth-child(1)").click()
    
    
    sleep(5)
    while True:
        #data = driver.find_elements_by_css_selector("a[class*='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']") 
        try:
            data = driver.find_elements_by_css_selector("a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']")
            for i in range (0, len(data)):
                try:
                    a.append(str(data[i].get_attribute('href')))  
                except:pass
            driver.execute_script("window.scrollTo(0, 1080)")
            for i in range(2):
                data[1].send_keys(Keys.END)
                sleep(5)
            driver.find_element_by_css_selector("div[class='j83agx80 bkfpd7mw kvgmc6g5 wkznzc2l oygrvhab dhix69tm'] span[class='j83agx80 fv0vnmcu hpfvmrgz'] span:nth-child(1)").click()
        except:
            break
        if len(a) > number: break
        a = list(set(a))     
    with open(f"craw_fb_{usernameCrawl}.txt", "w") as file:
        file.write("\n".join(a))




#main
def Solution(profile, i):
    number = int(input("Nhap So Luong Step: "))
    linkcrawl = str(input("Nhap link crawl: "))
    username = str(input("Nhap username: "))
    options = uc.ChromeOptions()
    options.binary_location = r'D:\asd\GoogleChromePortable - Copy (1)\App\Chrome-bin\chrome.exe'
    options.add_argument('--user-data-dir=D:\\asd\\GoogleChromePortable - Copy (1)\\Data\\profile')
    options.add_argument('start-maximized')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    chromedriver_exe = r'D:\chromedriver_win32\chromedriver.exe'
    options.add_argument("--disable-web-security")
    # just some options passing in to skip annoying popups  
    driver = uc.Chrome(executable_path = chromedriver_exe,options=options)  # version_main allows to specify your chrome version instead of following chrome global version\
    crawl_fb(driver,number,linkcrawl,username)
    time.sleep(3)

if __name__ == '__main__':
    try:
        Solution(1,1)
    except: 
        for i in range(0, 100):
            print("Error <3 Don't Worryyy !!!!!")
        pass