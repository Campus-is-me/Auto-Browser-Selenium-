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
