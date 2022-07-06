from secrets import randbits
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
def crawl_medium(driver,number,linkcrawl,username ): 
    hight =0 
    a=[]
    f = open("craw_medium"+username+".txt", "w")
    link = linkcrawl
    driver.get(link)
    sleep(5) 
    # wait = WebDriverWait(driver,60)  
    # wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='acl y']//p[@class='bv b bw bx by']")))
    # driver.find_element(By.XPATH,"//div[@class='acl y']//p[@class='bv b bw bx by']").click()
    lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range (0,number):
        hight = hight +200
        if hight > lastHeight : break
        driver.execute_script(f'window.scrollTo(0,{hight})')
        time.sleep(1)       
        lastHeight = driver.execute_script("return document.documentElement.scrollHeight")
    data = driver.find_elements_by_css_selector('a[rel = "noopener follow"]')
    try:     
        for i in range (0, len(data)):
           a.append(str(data[i].get_attribute('href')))
    except: pass
    a = list(set(a))
    f.write("\n".join(a))
    f.close()

def __name__ == '__main__':
    