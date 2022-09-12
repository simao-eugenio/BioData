
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

print(r.status_code)
print(r.headers['content-type'])
#print(r.text)
