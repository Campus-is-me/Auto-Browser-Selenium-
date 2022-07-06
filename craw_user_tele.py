from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest

api_id = 16084692
api_hash = 'd2854dd168da24ae3805cc6450488425'
phone = '+84988642302' #Thay phone
client = TelegramClient("C:\\Users\\Hieu\\Desktop\\seasion\\"+phone, api_id, api_hash)

async def main():
    
    userchanel = "Xlcapital" #Thay tên channel
    filetxt = "Xlcapital.txt" # lưu ý mỗi lần chạy phải sửa lại tên file nếu không nó sẽ thêm vào file cũ.

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))


    channel = await client(ResolveUsernameRequest(userchanel))
    async for _user in client.iter_participants(entity=channel):
        with open(filetxt,'a') as file:
            file.writelines("@" + str(_user.username) + "\n")


with client:
    client.loop.run_until_complete(main())