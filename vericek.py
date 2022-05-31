import requests
from bs4 import BeautifulSoup
#import pandas as pd
#import re
#liste = list()


#arama sayfası sayısı benim örneğimde 150 idi
#sitede kale kelimesini arattım çıkan 150 sayfa ve sayfalardaki
#archive-image classlı divlerin içlerindeki a taglarındaki linkleri aldım.
for x in range(150):
    url = "https://site.com/page/"+str(x)+"/?s=kale"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    veriler = soup.find_all("div",{"class":"archive-image"})
    for taglar in veriler:
        aTags = taglar.find_all("a",href=True)
        for tag in aTags:        
            #liste.append(tag['href'])
            #print(str(x)+": "+tag['href']+"\n")
            #elde edilen her linki tekrardan açarak içinde idsi content-area olan
            #divlerin içeriğini aldım
            response2 = requests.get(tag['href'])
            html_icerigi2 = response2.content
            soup2 = BeautifulSoup(html_icerigi2,"html.parser")
            veriler2 = soup2.find("div",{"id":"content-area"})
            content = str(veriler2)
            #gelen veri html tagları ile dolu, aşağıdaki kod ile temizledik.
            tmp = BeautifulSoup(content, "lxml").text.strip()
            #print(tmp) #metinleri ekrana bastık
            print(str(x)+"\n") 
            #çekilen her metni txt dosyasına kaydettik
            f = open("demofile2.txt", "a")
            f.write(tmp)
            f.close()

            
