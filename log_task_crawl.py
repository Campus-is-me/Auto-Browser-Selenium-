from secrets import randbits
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json,random,python_socks, string, subprocess
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from multiprocessing.dummy import Process, Queue
import pyotp


def login_gmail(driver,username, pas, mail_recover): 
    try: 
        driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(random.randint(2,3))
        driver.find_element_by_xpath("//input[@type='email']").send_keys(username)
        sleep(random.randint(2,3))
        driver.find_element_by_css_selector('.zQJV3 [type=button]').click()
        sleep(random.randint(2,3))
        driver.find_element_by_xpath("//input[@type='password']").send_keys(pas)
        sleep(random.randint(2,3))
        driver.find_element_by_css_selector('.qhFLie [type=button]').click()
        sleep(random.randint(2,3))
        try: 
            driver.find_element_by_css_selector(".JDAKTe.cd29Sd.zpCp3.SmR8 [data-challengeindex='2']").click()
            sleep(random.randint(2,3))
            driver.find_element_by_xpath("//input[@type='email']").send_keys(mail_recover)
            sleep(random.randint(2,3))
            driver.find_element_by_css_selector('.qhFLie [type=button]').click()
            sleep(random.randint(2,3))
        except: pass 
        return True
    except: return False
def getcode2FA(key):
    return  pyotp.TOTP(key).now()


def login_tw(driver,username,pas,fa):    
    try: 
        driver.get('https://twitter.com/i/flow/login')
        sleep(random.randint(2,3))
        driver.find_element_by_css_selector('.r-1pn2ns4.r-ttdzmv [autocomplete=username]').send_keys(username)
        driver.find_element_by_xpath("//*[text()='Next']").click()
        sleep(random.randint(2,3))
        driver.find_element_by_css_selector('.r-rs99b7.r-18u37iz [name=password]').send_keys(pas)
        driver.find_element_by_xpath("//*[text()='Log in']").click()
        sleep(random.randint(2,3))
        try: 
            code = getcode2FA(fa)
            driver.find_element_by_css_selector('.r-mk0yit.r-1f1sjgu [inputmode=numeric]').send_keys(code)
            driver.find_element_by_xpath("//*[text()='Next']").click()
            sleep(random.randint(2,3))
            #Thuwr lai lan 2
            code = getcode2FA(fa)
            driver.find_element_by_css_selector('.r-mk0yit.r-1f1sjgu [inputmode=numeric]').send_keys(code)
            driver.find_element_by_xpath("//*[text()='Next']").click()
            sleep(random.randint(2,3))
            return True
        except: pass
        return True
    except: return False




def getusername(driver): 
    try: 
        driver.get("https://twitter.com/") 
        time.sleep(10)
        element = driver.find_element_by_css_selector(".r-oyd9sg.r-13qz1uu[data-testid=AppTabBar_Profile_Link]")
        linkprofile = element.get_attribute('href')
        username = linkprofile.replace('https://twitter.com/','')
        print("Done get username: ",username)
        return username
    except: return ""

def clicklike(driver,username_fl,id): 
    try: 
        driver.get(f'https://twitter.com/{username_fl}/status/{id}')
        time.sleep(6)
        driver.find_element_by_css_selector(".r-3qxfft.r-s1qlax div[data-testid=like]").click()
        time.sleep(1)
        print("Done Click Like: ", id)
        return True
    except: return False

def follow(driver,username_fl):
    try: 
        driver.get(f"https://twitter.com/intent/follow?region=follow_link&screen_name={username_fl}")
        time.sleep(6)
        driver.find_element_by_css_selector(".r-11c0sde.r-13qz1uu div[data-testid=confirmationSheetConfirm]").click()
        time.sleep(1)
        print("Done Click Follow: ", username_fl)
        return True
    except: return False

def retwitter(driver,id):
    try: 
        driver.get(f"https://twitter.com/intent/retweet?tweet_id={id}")
        time.sleep(6)
        driver.find_element_by_css_selector(".r-11c0sde.r-13qz1uu div[data-testid=confirmationSheetConfirm]").click()
        time.sleep(1)
        print("Done Click RT: ", id)
        return True
    except: return False
def quotetw(driver,id,tag,username_fl): 
    try: 
        driver.get(f"https://twitter.com/")
        time.sleep(6)
        driver.find_element_by_class_name('public-DraftStyleDefault-block.public-DraftStyleDefault-ltr').send_keys(f"{tag}   https://twitter.com/{username_fl}/status/{id}")
        driver.find_element_by_css_selector(".r-7qyjyx.r-1ftll1t div[data-testid=tweetButtonInline]").click()
        time.sleep(1)
        print("Done Click Quotetw: ", id)
        return True
    except: return False

def getlink_quotetw(driver,username):
    try:  
        driver.get(f"https://twitter.com/{username}/with_replies")
        time.sleep(6)
        element = driver.find_element_by_css_selector(f'a.r-qvutc0[href^="/{username}/status"]').get_attribute('href')
        print("Done getlink quotetw: ", element)
        time.sleep(1)
        return element
    except: return ""


def crawl_quotw(driver,number,link):
    a= []
    hight =0
    f = open("craw_data_quotes.txt", "w") 
    driver.get(link)
    for j in range(0,number):     
        try:      
            data = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-1d09ksm.r-18u37iz.r-1wbh5a2 [dir=auto][role=link]')))
            a.append(str(data.get_attribute('href')))
            print(str(data.get_attribute('href')))
            hight = hight +350
            driver.execute_script(f'window.scrollTo(0,{hight})')
            sleep(2)
           
        except: 
            hight = hight + 350
            driver.execute_script(f'window.scrollTo(0,{hight})')
            sleep(2)
        a = list(set(a))
        
        
    f.write("\n".join(a))
    f.close()


def crawl_rt(driver,number,usernameCrawl,id ): 
    hight =0 
    a=[]
    f = open(f"craw_data_reweets_{usernameCrawl}.txt", "w")
    link = f"https://twitter.com/{usernameCrawl}/status/{id}retweets/with_comments"
    driver.get(link)
    sleep(5)
    for j in range(0,number):
        try:              
            data = driver.find_element_by_css_selector('.r-18u37iz.r-1wbh5a2 [role=link]')
            print(str(data.text))
           # a.append(data.text)
            hight = hight +5
            driver.execute_script(f'document.querySelector(".r-1wbh5a2.r-1dqxon3").scrollTo(0,{hight})')
         
        except:
            hight = hight +5
            driver.execute_script(f'document.querySelector(".r-1wbh5a2.r-1dqxon3").scrollTo(0,{hight})')
           
        a = list(set(a))
           
    f.write("\n".join(a))
    f.close()   

if __name__ =='__main__' : 
    while True : 

   #  fdatagmail = open("C:\\Users\\84986\\Desktop\\datagmail.txt",'r',encoding = 'utf-8')
        linkprofile = ["C:\\Users\\84986\\Desktop\\Profile1\\concac","D:\\Chome\\concac"]
        link =["https://twitter.com/qenetex/status/1503817287832420366/retweets/with_comments","https://twitter.com/iSafePal/status/1507534047756517376/retweets/with_comments"]
        processes =[]
        for i in range(0,len(linkprofile)): 
            path_to_chromedriver = "D:\Chome\chromedriver.exe"
            options = uc.ChromeOptions()
            options.binary_location = r"C:\\Users\\84986\\.gologin\\browser\\orbita-browser\\chrome.exe"
            options.add_argument(f"--user-data-dir={linkprofile[i]}")
            driver = uc.Chrome( options=options,executable_path=path_to_chromedriver, version_main= 98)
            driver.maximize_window()
            driver.set_window_size(820,900)
           
            
          #  crawl_quotw(driver,30000,link)
            process = Process(target=crawl_quotw, args = (driver,30000,link[i],))
            processes.append(process)
        for process in processes: process.start()
        for process in processes: process.join()

   # driver.set_window_size(820,900)
   # driver.implicitly_wait(30)


   # datagmail = json.loads(fdatagmail.readline().strip())
   # username = datagmail['mail']
   # pas = datagmail['pas']
   # mail_recover = datagmail['mail_recover']
   # if login_gmail(driver,username,pas, mail_recover) : print("Loggin Gmail ------ True") 
    #else: print("Loggin Gmail ------ False")

   # driver.quit()
    link ='https://twitter.com/qenetex/status/1503817287832420366/retweets/with_comments'
    crawl_quotw(driver,30000,link)



    
    
   

       