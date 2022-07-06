import discum

bot = discum.Client(token="Njg0MDY0ODEzNDc5MTAwNDIz.Yk24NQ.ka-Dg-eJVgjisE4EO2CgHo0g998") #########Thay token của acc mình .

def close_after_fetching(resp,guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params' : {'guild_id' : guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id,channel_id, keep= 'all' , wait=1)
    bot.gateway.command({'function' : close_after_fetching , 'params' : {'guild_id' : guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members




members = get_members('933038825180123197','933038825679233039') ############ Vô channel mình muốn craw, nhìn lên link. nó sẽ có 2 dãy số cách nhau bởi dấu /, copy vô theo thứ tự
memberslist = []

for member in members:
    memberslist.append(members)
    
with open('user.txt', 'a',encoding = 'utf-8') as file:
    file.write(str(memberslist) +"\n")


