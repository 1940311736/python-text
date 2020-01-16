import requests
import json
host ='https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])

params = {'show_env':1,'lld':'liuliandi'}
headers = {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

r = requests.get(url,params=params,headers=headers)
print(r.status_code)
print(r.headers)
print(r.text)