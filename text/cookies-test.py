import requests
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
host ='https://httpbin.org/'
endpoint = 'cookies'
url = ''.join([host,endpoint])
url1='http://www.baidu.com/'
r = requests.get(url)
print(r.cookies)
#把jar包转换成字典
d = requests.utils.dict_from_cookiejar(r.cookies)
print(d)

print({a.name:a.value for a in r.cookies})
#发送cookies到服务器
cookies = {'cookies-name':'text'}
r1 = requests.get(url,cookies=cookies)
print(r1.text)

#复杂的写法
s = requests.session()
c =requests.cookies.RequestsCookieJar()
c.set('cookies-name','cookies-value',path='/',domain='.test.com')
s.cookies.update(c)
print(s.cookies)