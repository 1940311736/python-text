import requests
host = 'https://httpbin.org/'
enpoint = 'cookies'
url = ''.join([host, enpoint])
url1 = 'https://www.baidu.com/'

r = requests.get(url)
print(r.cookies)
print(r.text)

d = requests.utils.dict_from_cookiejar(r.cookies)
print(d)
print({a.name:a.value for a in r.cookies})

#发送cookies到服务器
cookies = {'cookies-name': 'lld'}
rl = requests.get(url, cookies=cookies)
print(rl.text)

#复杂的写法
s = requests.session()
c = requests.cookies.RequestsCookieJar()
c.set('name', 'value', path='/', domain='.test.com')
s.cookies.update(c)
print(s.cookies)


