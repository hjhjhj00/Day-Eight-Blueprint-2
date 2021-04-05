import os
import csv
import requests
from bs4 import BeautifulSoup


os.system("clear")
alba_url = "http://www.alba.co.kr"

r=requests.get(alba_url)
alba_all=BeautifulSoup(r.text,"html.parser")
a=alba_all.find("ul",{"class":"goodsBox"}).find_next("ul",{"class":"goodsBox"})
c=a.find_all("li",{"class":"impact"})

def get_link(a):
    status=requests.get(a)
    bs=BeautifulSoup(status.text,"html.parser")
    tbody=bs.find("body").find("tbody")
    trs=tbody.find_all("tr")
    lists=[]
    for i in trs:
        try:
            places = i.find("td",{"class":"local first"}).get_text()
            titles = i.find("td",{"class":"title"}).get_text()
            times = i.find("td",{"class":"data"}).get_text()
            pays=i.find("td",{"class":"pay"}).get_text()
            dates=i.find("td",{"class":"regDate last"}).get_text()
            lists.append([places,titles,times,pays,dates])
        except:
            pass

    return lists

for i in c:
    ahref=i.find("a")
    link=ahref.attrs["href"]
    print(link)
    span = ahref.find("span",{"class":"company"}).string
    file = open(f"{span}.csv", mode="w",encoding="UTF-8")
    writer = csv.writer(file)

    code = get_link(link)
    writer.writerow(["place","title","time","pay","date"])
    for i in code:
        writer.writerow(i)