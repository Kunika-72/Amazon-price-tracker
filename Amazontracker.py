from email import header
import bs4
import requests
from bs4 import BeautifulSoup 

def PriceTracker(url):
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept Lang":"en"
    }
    r=requests.get(url,headers=header)
    soup=BeautifulSoup(r.text,"lxml")
    #Finding name
    pname = soup.find("span",id="productTitle").text
    pname =pname.strip()
    #Finding price
    price = soup.find("span",class_="a-offscreen").text
    temp = price[1:].replace(",","")
    price = float(temp)
    return pname, price

urls = []
with open("Amazon_tracker/Amazon_URL.txt") as furl:
    t = furl.read()
    urls = t.split("\n")

rows=[]
for url in urls:
    pname, price = PriceTracker(url)
    rows.append([pname,price])

print(rows)

import csv
with open("Amazon_Prices.csv","w") as fp:
    csvw = csv.writer(fp)
    csvw.writerow(["Name","Price"])
    csvw.writerows(rows)

#print("Amazon_prices.csv")





