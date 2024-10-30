import requests
url="http://google.com.ua"
r = requests.get(url)
print(r.status_code)
