import json
from urls import url_dict
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = url_dict['main']
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

contents = soup.find("div", class_="page-content__inner")
links = contents.find_all("a")
for link in links:
    post_link = link.get("href")
    if "day" in post_link:
        url_dict['tutorials'].append(post_link)

    
with open("urls.json", "w") as f:
    json.dump(url_dict, f)
