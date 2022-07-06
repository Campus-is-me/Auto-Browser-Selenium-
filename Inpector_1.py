import KuAnh
import asyncio, os, random, string, csv, traceback
import array as arr
from ntpath import join
from multiprocessing import Process
import time, urllib.request
from email.message import Message
from pyexpat.errors import messages
from telethon.tl.types import InputMessagesFilterPhotos
from telethon import TelegramClient
from time import sleep
from anticaptchaofficial.imagecaptcha import *
from telethon.tl.functions.messages import StartBotRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient, connection, sync, functions

def Captcha_imanage(Client, botid): 
    try:
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("dien key vao day")
      
        messages = Client.get_messages(botid)
        msg = messages[0]
        imageLink = "files/" + Client.get_me().phone 
        imageFile =  Client.download_media(msg.media, imageLink )
        captcha_text = 0 
        captcha_text = solver.solve_and_return_solution(imageFile)   #nhận captcha từ anticaptcha
        os.remove(imageFile)
        
        if captcha_text != 0:
            print("captcha text "+captcha_text)
            Client.send_message(botid, captcha_text)          #Send captcha từ anticaptcha vào con bot
            sleep(random.randint(3,5))
            messages =  Client.get_messages(botid)             # Sau khi sent, nhận kết quả từ con bot 
            if messages[0].text.find('Wrong captcha') != -1:   #Kiểm tra xem captcha đúng chưa
                return False
            return True        
        else:
            print("task finished with error "+solver.error_code)
            return False 
    except: print("Loi khong xac dinh")



def Task(Clients,botid,ref,group,tw,wall): 
    try: 
        Client = TelegramClient(Clients['session'], Clients['api'], Clients['hash'], proxy=Clients['proxy'])
        Client.connect()
        Client(StartBotRequest(botid, botid,ref))

        for i in range(0, len(group)): 
            KuAnh.JoinGroup(Client,group[i])  

        Check = False
        for i in range (0,3): 
            if Captcha_imanage(Client, botid):
                Check = True 
                break
        if not Check: 
            try: 
                Client.disconnect()
                return False 
            except: pass 
         
        if not KuAnh.waite(Client,botid,"Airdrop Bot"): return False
        Client.send_message(botid,'Continue')

        if not KuAnh.waite(Client,botid,"Complete the tasks below!"): return False
        Client.send_message(botid,'Submit Details')

        if not KuAnh.waite(Client,botid,"After joined"): return False
        Client.send_message(botid,'✅Done')

        if not KuAnh.waite(Client,botid,"Submit your Twitter profile link"): return False
        Client.send_message(botid,tw)

        if not KuAnh.waite(Client,botid,"Please join our advertiser telegram channel"): return False
        Client.send_message(botid,'✅Done')

        if not KuAnh.waite(Client,botid,"Follow our advertiser"): return False
        Client.send_message(botid,'✅Yes')

        if not KuAnh.waite(Client,botid,"wallet address"): return False
        Client.send_message(botid,wall)       
        
        if KuAnh.waite(Client, botid, "Thank you"):print(Client.get_me().phone, " :hoan thanh nhiem vu")
        Client.disconnect()
    except: 
        try: 
            Client.disconnect()
        except: pass
         

  
    

















