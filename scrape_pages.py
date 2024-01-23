import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('urls.json','r') as urls: 
    content = urls.read()
    urls_dict = json.loads(content)

urls = urls_dict['tutorials']
pattern = 'day-[0-9]+'

for url in urls:
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    contents = soup.find("div", class_="article__main")
    day = re.search(pattern, url)

    if day:

        file_name = "./pages/" + day.group() + ".html"
        with open(file_name, 'w') as tut:
            tut.write(str(contents))
    else: 
        raise Exception("Regex Failed")
