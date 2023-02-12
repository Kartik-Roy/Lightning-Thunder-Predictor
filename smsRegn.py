import urllib.request
import urllib.parse
import json
import pickle
import requests
import urllib
import mysql
import datetime
import time

def getMessages(apikey, inboxID):
    params = {'apikey': 'ZpPu6fA9IgY-AuxN59AFKYRJdHFrEL9c99xDzpLBIe', 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)

def load(file_name):
    with open(file_name, 'rb') as fobj:
        return pickle.load(fobj)


pickle_j = load('pickle_i.pickle')
resp, code = getMessages('ZpPu6fA9IgY-AuxN59AFKYRJdHFrEL9c99xDzpLBIe', '10')
x = resp.decode()
j = json.loads(x)
dic = dict()
url = 'http://13.126.31.37:8000/sms-signup'
for i in range(pickle_j, j['num_messages']):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    temp = j['messages'][i]['message']
    l_temp = temp.split()
    l_temp[4] = l_temp[4].lower()
    dic['name'] = l_temp[1]
    print(type(l_temp[1]))
    dic['phone'] = l_temp[2]
    dic['pincode'] = l_temp[3]
    dic['lang'] = l_temp[4]
    js = json.dumps(dic)
    pickle_j += 1
    requests.post(url, json=dic, headers={'Content-Type': 'application/json'})

with open('pickle_i.pickle', 'wb') as fobj:
    pickle.dump(pickle_j, fobj)
