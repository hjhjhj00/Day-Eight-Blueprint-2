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
    places = tbody.find_all("td",{"class":"local first"})
    place=[]
    for i in places:
        place.append(i.get_text())
    titles = tbody.find_all("td",{"class":"title"})
    title=[]
    for i in titles:
        title.append(i.find("a").find("span",{"class":"company"}).string)
    times = tbody.find_all("td",{"class":"data"})
    time=[]
    for i in times:
        time.append(i.get_text())
    pays=tbody.find_all("td",{"class":"pay"})
    pay=[]
    for i in pays:
        pay.append(i.get_text())
    dates=tbody.find_all("td",{"class":"regDate last"})
    date=[]
    for i in dates:
        date.append(i.get_text())

    return place,title,time,pay,date

for i in c:
    ahref=i.find("a")
    link=ahref.attrs["href"]
    print(link)
    span = ahref.find("span",{"class":"company"}).string
    file = open(f"{span}.csv", mode="w",encoding="UTF-8")
    writer = csv.writer(file)

    code = get_link(link)
    writer.writerow(["place","title","time","pay","date"])
    writer.writerow(code)
