import json
import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
writeurl = 'https://chatwithyou.cloudant.com/chat/1'
readurl='https://chatwithyou.cloudant.com/chat/1'
headers = {
    'cache-control': "no-cache",
    }

uname=input('Enter your username to continue\n')
print(Fore.WHITE +'Welcome '+uname+' for VISHs CHATROOM')
print(Fore.RED +'!!!............Writer Window............!!!\n')
username='.........{'+uname+'}'

while True:
    data = requests.request("GET", readurl, headers=headers)
    data_in_text=str(data.text)
    data_in_json=json.loads(data_in_text.encode())
    old_id=data_in_json['_id']
    old_rev=data_in_json['_rev']
    message=data_in_json['message']
    spaces='                          '
    #print(spaces+message)
    message=input()
    newmessage=(Fore.WHITE+spaces+message+username)
    payload = {'_id': old_id, '_rev':old_rev, 'message':newmessage}
    putresponse = requests.request("PUT", writeurl, data=json.dumps(payload))
    #print(putresponse.text)
    #print(newmessage+username)
    #data = requests.request("GET", readurl, headers=headers)
    #data_in_text=str(data.text)
    #data_in_json=json.loads(data_in_text.encode())
    #new_id=data_in_json['_id']
    #new_rev=data_in_json['_rev']
    #message=data_in_json['message']
