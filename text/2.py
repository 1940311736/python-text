import requests
host = 'https://httpbin.org/'
enpoint = 'cookies/set/sessioncookie/123456789'
url = ''.join([host, enpoint])
url1 = 'https://httpbin.org/cookies'

r = requests.get(url1)
print(r.text)

session = requests.Session()
session.get(url)
rl = session.get(url1)
print(rl.text)

hd1 = {'text1': 'aa'}
hd2 = {'text1': 'bb'}

session1 = requests.Session()
session1.headers.update(hd1)
r2 = session1.get('https://httpbin.org/headers', headers=hd2)
print(r2.text)

session1.headers['text1']=None
r3 = session1.get('https://httpbin.org/headers', headers=hd1)
print(r3.text)
