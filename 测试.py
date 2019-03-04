__author__ = 'Administrator'
import requests
import json

uel1='http://192.168.1.200/manager/login'
url='http://192.168.1.200/manager/customer/customerGroupList'
sata={'loginName':'client',
      'password':'abc123'}

data={

        'pageNo':1,
      'pageSize':'15'
}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Content-Type':'application/json;charset=UTF-8'}

a=requests.post(uel1,headers=headers,data=json.dumps(sata))
s=a.json()
print(s)
print(s['data']['token'])
headers['X-ZX-TOKEN']=s['data']['token']
resp=requests.post(url,headers=headers,data=json.dumps(data),)
print(resp.text)
