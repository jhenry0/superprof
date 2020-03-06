import requests
import json
from tasks import getProfByCategory
from bs4 import BeautifulSoup


html = requests.get("https://www.superprof.com.br/todas-as-materias.html")
html = BeautifulSoup(html.content,features="html.parser")
classe = html.find_all(class_="subjects")
categories = []

for x in classe:
    x = x.find_all("a")

    for index,y in enumerate(x):
        print(f"{index}/{len(x)}-{y.contents[0]}")
        getProfByCategory.delay(y.contents[0])   

