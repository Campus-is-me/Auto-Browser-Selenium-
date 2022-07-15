#Made by Campus <33333
#Telegram: @Campus_Real 
#Phone: 0337176055

def _open_file_(link_file):
    with open(link_file,'r') as f:
        list = f.readlines()
    list_file = []
    for i in list:
        list_file.append(i.strip())
    return list_file
