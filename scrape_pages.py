import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('urls.json','r') as urls: 
    content = urls.read()
    urls_dict = json.loads(content)

urls = urls_dict['tutorials']
test_url = urls[0]

page = urlopen(test_url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

contents = soup.find("div", class_="article__main")

with open("test.html", 'w') as test:
    test.write(str(contents))



