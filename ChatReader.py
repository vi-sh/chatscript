import json
import requests
import time
import colorama
from colorama import Fore, Back, Style
url = 'https://chatwithyou.cloudant.com/chat/1'
headers = {
    'cache-control': "no-cache"
    }
colorama.init()
deletederror='{"error":"not_found","reason":"Database does not exist."}'
#uname=input('Enter your username to continue\n')
#print('Welcome '+uname+' for VISHs CHATROOM')
print(Fore.RED + 'If your message is not displayed here please send again !!!')
print(Fore.WHITE +'!!!............Reader Window............!!!\n')

#username='.........{'+uname+'}'

def readagain():
    while True:
        objdata=requests.request("GET", url, headers=headers)
        textdata=str(objdata.text)
        jsondata=json.loads(textdata.encode())
        _id=jsondata['_id']
        _rev=jsondata['_rev']
        message=jsondata['message']
        if message != None:
            print(message)
            message=''
            payload = {'_id': _id, '_rev':_rev, 'message':None}
            putresponse = requests.request("PUT", url, data=json.dumps(payload))
            #print(putresponse.text)
readagain()
