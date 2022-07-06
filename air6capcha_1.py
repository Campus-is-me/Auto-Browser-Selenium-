from cgi import test
from cgitb import text
from multiprocessing.connection import Client
from turtle import right
from telethon.tl.functions.messages import StartBotRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
import time, random ,requests , os
from anticaptchaofficial.imagecaptcha import * #đây này
import multiprocessing # muốn xài đa luồng thì import thằng này
def Captcha_imanage(Client,phone,botid): 
    try:
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("key") #giờ chỗ này điền key vào là nó tự giải capcha ảnh phỏng ?. ừ capthca kiểu nhìn hình gõ ra chữ đó , còn capcha điện thoại , radio thì sao, không biết nó giải được không chưa thử
      
        messages = Client.get_messages(botid)
        msg = messages[0]
        
       
        imageLink = "files/" + phone 
        imageFile =  Client.download_media(msg.media, imageLink ) #còn chỗ nào lạ nữa k nhỉ. hàm captcha này copy chứ có sửa gì đâu m
        captcha_text = 0 
        captcha_text = solver.solve_and_return_solution(imageFile)   #nhận captcha từ anticaptcha
        os.remove(imageFile)
        
        if captcha_text != 0:
            print("captcha text "+captcha_text)
            Client.send_message(botid, captcha_text)          #Send captcha từ anticaptcha vào con bot
            time.sleep(random.randint(3,5))
            messages =  Client.get_messages(botid)             # Sau khi sent, nhận kết quả từ con bot 
            if messages[0].message.find('Wrong captcha') != -1:   #Kiểm tra xem captcha đúng chưa
                return False
            return True        
        else:
            print("task finished with error "+solver.error_code)
            return False 
    except: print("Loi khong xac dinh")

def gettxt(filetxt):
    with open(filetxt , 'r') as file:
        list = file.readlines()
    list_strip = []
    for i in list:
        list_strip.append(i.strip())
    return list_strip

def wait(Client,botID,check):

    time.sleep(random.randint(2,5))
    for i in range(0,10):
        tmp = Client.get_messages(botID)
        if str(tmp[0].message).find(check) != -1:
            return True
        else:time.sleep(5)

    Client.disconnect()
    return False


def task(phone,api_id,api_hash,botid,tentw,wall,ref):
   
    Client = TelegramClient("C:\\Users\\vutha\\Downloads\\Telegram Desktop\\session\\"+phone+".session", api_id, api_hash) #dang test con bot đây f5 đi
    Client.connect()
    print('CONNECT')

    if not Client.is_user_authorized(): 
        print('SS lỗi:',phone)
        return False
    else:

        try:
            print("Acc số {0} đang chạy".format(phone)) #mỗi lần chạy nó sẽ in số phone ra trước nè. ok không , lằng nhằng phết nhỉ. chứ m muốn hiện gì
            
            Client(StartBotRequest(botid, botid, ref))
            print('START')
            #Client.send_message(botid,"/start")

            if not wait(Client,botid,"Click on Continue before typing the code"): return False
            ######################### solve captcha math#############
            mess = Client.get_messages(botid)
            list = mess[0].text.strip().split(":")
            print(list)

            newlist = list[1].strip().split("=")
            print(newlist)
            newlist0 = newlist[0].strip()
            print(newlist0)

            try:
                list_int = newlist0.split("+")
                cal = int(list_int[0]) + int(list_int[1])
                print(cal) 
                mess[0].click()
                if not wait(Client, botid, "Great, please enter the code."): return False 
                Client.send_message(botid,str(cal))
            except:
                list_int = newlist0.split("-")
                cal = int(list_int[0]) - int(list_int[1])
                print("Ket qua captcha: ",cal)
                mess[0].click() 
                if not wait(Client, botid, "Great, please enter the code."): return False 
                Client.send_message(botid,str(cal))           
            ######################### solve captcha math#############
           

            if not wait(Client, botid, "✅Thats correct!"): return False 
            Client(JoinChannelRequest("Gotg_Group"))
            Client(JoinChannelRequest("Gotg_Channel"))
            time.sleep(random.randint(1,5))
            mess = Client.get_messages(botid)
            mess[0].click()
            print('1')

            if not wait(Client, botid, "🔘Please join"): return False
            mess = Client.get_messages(botid)
            mess[0].click()
            print('2')

            if not wait(Client, botid, "🔘Now please follow"): return False
            Client.send_message(botid, tentw)
            print('3')

            # if not wait(Client, botid, "Please Follow our"): return False
            # Client.send_message(botid, medium)
            # print('3')

           


            # if not wait(Client, botid, "🔘Please Join our "): return False
            # mess = Client.get_messages(botid)
            # mess[0].click()
            # print('4')

            # if not wait(Client, botid, "Please visit"): return False
            # mess = Client.get_messages(botid)
            # mess[0].click()
            # print('5')

            

           

            if not wait(Client,botid,"Optional + 0.5 GOTG"): return False
            Client(JoinChannelRequest("airdrop6officialchannel"))
            time.sleep(random.randint(1,3))
            mess = Client.get_messages(botid)
            print(mess[0].text)
            mess[0].click()
            print('6')

            if not wait(Client,botid,"Please submit your"): return False
            Client.send_message(botid,wall)
            print('7')

            Client.disconnect()
            print('XONGGGGGGGGGGGGGGGG')

        except: 
            try: 
                Client.disconnect()
            except:pass
            print('TẠCHHHHHHHHHHHHHHHH')

def main():

    listtw = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\tw.txt")
    listwall = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\wall.txt")
    listphone = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\test.txt")
    listemail = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\mail.txt")
    listinstagram = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\ins.txt")
    listmedium = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\medium.txt")
    listquote = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\quote.txt")
    listtentw = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\tentw.txt")
    listtenmedium = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\tenmedium.txt")
    listtrx = gettxt("C:\\Users\\vutha\Downloads\\Telegram Desktop\\session\\trx.txt")
    



    api_id = 16084692
    api_hash = 'd2854dd168da24ae3805cc6450488425'
    botid = "GOTGNewAirdropBot"#thay tên
    
    ref = "5098202230"#phải thay ref
    for i in range(0,250,5): #vòng forr này nè. ví dụ m chạy 5 luồng thì nó chạy từ 0,1,2,3,4 là hết 5 cái. nên sau khi chạy xong thì i nó phải tăng thêm 5 tức là i + 5 nên m phải set step cho nó
        try: #đó step = 5 nghĩa là mỗi vòng for chạy xong thì i tăng lên 5 . vòng 2 nó sẽ chạy 5,6,7,8,9 . ok không , ok good đấy. good clq . chạy đi

            #trong hàm này sẽ tạo đa luồng ok

            # #tạo biến đa luồng
            # p1 = multiprocessing.Process(target=task,args=(listphone[i],api_id,api_hash,botid,listtentw[i],listtenmedium[i],listwall[i],ref)) #đấy à, ừ mà m coi tham số i. truyền vô phải tăng dần không nó trùng nhau
            # p2 = multiprocessing.Process(target=task,args=(listphone[i+1],api_id,api_hash,botid,listtentw[i+1],listtenmedium[i+1],listwall[i+1],ref)) #không hiểu :)) hiểu rồi. vậy là hiểu chưa , rồi đó
            # p3 = multiprocessing.Process(target=task,args=(listphone[i+2],api_id,api_hash,botid,listtentw[i+2],listtenmedium[i+2],listwall[i+2],ref)) #kiểu gì m, đó , thế ớ hở
            # p4 = multiprocessing.Process(target=task,args=(listphone[i+3],api_id,api_hash,botid,listtentw[i+3],listtenmedium[i+3],listwall[i+3],ref)) # ừm . chỗ này có nghĩa là ví dụ cái list phone bắt đầu từ 0 thì luồng 1 chạy 1, luồng 2 nó lấy dòng số điện thoại thứ 2, luồng 3 lấy số số thứ 3 . mà trong lập trình thì dòng 1 nó bắt đầu từ 0 nên i lúc đầu bằng 0 chứ k phải bằng 1 hiểu k
            # p5 = multiprocessing.Process(target=task,args=(listphone[i+4],api_id,api_hash,botid,listtentw[i+4],listtenmedium[i+4],listwall[i+4],ref)) #đây là 1 luồng, hàm này có 2 tham số, 1 là cái hàm cần chạy target, 2 là các biến truyền vô hàm đó args
            
            p1 = multiprocessing.Process(target=task,args=(listphone[i],api_id,api_hash,botid,listtentw[i],listwall[i],ref)) #đấy à, ừ mà m coi tham số i. truyền vô phải tăng dần không nó trùng nhau
            p2 = multiprocessing.Process(target=task,args=(listphone[i+1],api_id,api_hash,botid,listtentw[i+1],listwall[i+1],ref)) #không hiểu :)) hiểu rồi. vậy là hiểu chưa , rồi đó
            p3 = multiprocessing.Process(target=task,args=(listphone[i+2],api_id,api_hash,botid,listtentw[i+2],listwall[i+2],ref)) #kiểu gì m, đó , thế ớ hở
            p4 = multiprocessing.Process(target=task,args=(listphone[i+3],api_id,api_hash,botid,listtentw[i+3],listwall[i+3],ref)) # ừm . chỗ này có nghĩa là ví dụ cái list phone bắt đầu từ 0 thì luồng 1 chạy 1, luồng 2 nó lấy dòng số điện thoại thứ 2, luồng 3 lấy số số thứ 3 . mà trong lập trình thì dòng 1 nó bắt đầu từ 0 nên i lúc đầu bằng 0 chứ k phải bằng 1 hiểu k
            p5 = multiprocessing.Process(target=task,args=(listphone[i+4],api_id,api_hash,botid,listtentw[i+4],listwall[i+4],ref)) #đây là 1 luồng, hàm này có 2 tham số, 1 là cái hàm cần chạy target, 2 là các biến truyền vô hàm đó args







            p1.start()
            time.sleep(random.randint(2,5))
            p2.start()
            time.sleep(random.randint(2,5))
            p3.start()
            time.sleep(random.randint(2,5))
            p4.start()
            time.sleep(random.randint(2,5))
            p5.start()
            time.sleep(random.randint(2,5)) #hàm này để gọi luồng chạy
            p1.join() #cái này chạy xong thì nó tự tắt hay sao . thì bản chất nó là chạy như bình thường đó , nhưng mà chạy nhiều cái cùng lúc thôi. lưu ý
            p2.join()
            p3.join()
            p4.join()
            p5.join()
             #hàm này để đóng luồng khi chạy xong

            #m muốn tạo bao nhiêu luồng thì cứ tạo bấy nhiêu cái p, ví dụ p1,p2,p3 và truyền tham số vô cho nó.5 cái. tạo đi

            # print("Acc "+ str(i) + " " + str(listphone[i])) #tưởng ném cái này lên là xong cơ. m chạy thử là biết , ok để kiếm con bot chạy thử
            # task(listphone[i],api_id,api_hash,botid,listtentw[i],listtrx[i],ref)
        except:pass #bật cái hiện acc chạy đi m



if __name__ == '__main__':main()