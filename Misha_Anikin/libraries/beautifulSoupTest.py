import requests
from bs4 import BeautifulSoup
url="http://google.com.ua"
r = requests.get(url)
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
ryadok1=page.text
ryadok2=page.body.text
words=ryadok1.split(' ')
print(words)
