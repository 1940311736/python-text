import requests
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
host ='https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])
#文件上传
#files = {'file':open('text.txt','rb')}
#文件修改内容
#files = {'file':('text.txt','lld')}
#多个文件上传
#files =[
  #('field1',('text.txt',open('text.txt','rb'))),
  #('field2',('text.txt',open('text.txt','rb'))),
 # ('field3',('text.txt',open('text.txt','rb'))),
#]
#流式上传
with open('text.txt') as f:
  r = requests.post(url,data=f)
data = {
  "info":{"code":1,"sex":"女","id":6666,"name":"lld"},
  "code":1,
  "name":"lld","sex":"女",
  "data":[{"code":1,"sex":"女","id":6666,"name":"lld"},{"code":1,"sex":"女","id":6666,"name":"lld"}],
  "id":6666
}

#r = requests.post(url,data=json.dumps(data))
#r = requests.post(url,files=files,json=data)
print(r.status_code)
print(r.text)

#res = r.json()
#print(res['form'])
#print(res['headers']['Content-Length'])