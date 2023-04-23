from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
children = doc.select(('div.card-body'))[0].children
for child in children:
    print(child)