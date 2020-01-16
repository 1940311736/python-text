import requests
import json
host ='https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])

r =requests.get(url)

print(r.url) #获取url
print(r.status_code,r.reason) #获取状态码
print(r.headers) #获取头部信息
print(r.text) #获取整个文本信息
print(r.content)

res = r.json()
print(res['headers']['Accept-Encoding'])