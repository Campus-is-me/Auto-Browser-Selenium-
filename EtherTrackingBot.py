from telethon.sync import TelegramClient
import time,GOD
import random

def wait(Client,botID,check):

    time.sleep(random.randint(1,2))
    for i in range(0,10):
        tmp = Client.get_messages(botID)
        if str(tmp[0].message).find(check) != -1:
            return True
        else:time.sleep(5)

    Client.disconnect()
    return False

def task(botid,wallet): 
    api_id = ""
    api_hash = ''
    phone = ""
    Client = TelegramClient("/session" +phone,api_id,api_hash)
   
  
    Client.connect()
    if not Client.is_user_authorized(): return False
    else:
        try:
            Client.send_message(botid,"/start")
            
            if not wait(Client,botid,"welcome on board!"): return False
            Client.get_messages(botid)[0].click(text = "➕ Add wallet")

            for i in range(0,len(wallet)):
               
                if not wait(Client,botid,"networks to add and press"):return False
                Client.get_messages(botid)[0].click(text = "☑️️ Done")

                if not wait(Client,botid,"Enter address to watch"):return False 
                Client.send_message(botid,wallet[i])

                if not wait(Client,botid,"Enter label for"):return False 
                Client.get_messages(botid)[0].click(text = "Skip")

                if not wait(Client,botid,"You can customize event types"):return False 
                Client.get_messages(botid)[0].click(text = "Add More to Main")

        except:
            Client.disconnect()
        

if __name__ == '__main__':

    wallet = GOD.get_wallet("metamask_wallet")
    botid = "@EtherDROPS1_bot"
    task(botid,wallet)