from random import betavariate
from attr import attr, attrs
import requests
from bs4 import BeautifulSoup

toplamUrun=0 
for sayfaNo in range(1,3):
    url="https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg="+str(sayfaNo)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    urunler=soup.find_all("li",attrs={"class":"column"})

    for urun in urunler: 
        urunAdi=urun.a.get("title")
        urunLink=urun.a.get("href")
        print(urunAdi)
        try:
            urun_r=requests.get(urunLink)
            toplamUrun+=1
        except Exception:
            print("Ürün detayı alınamadı")
        urun_soup=BeautifulSoup(urun_r.content,"lxml")
        ozellikler=urun_soup.find_all("div",attrs={"class":"feaItem"})
        for ozellik in ozellikler:
            urun_label=ozellik.find("span",attrs={"class":"label"}).text
            try:
                urun_data=ozellik.find("span",attrs={"class":"data"}).text
            except Exception:
                urun_data=ozellik.find("a",attrs={"class":"data"}).find("span").text
            print("{}:{}".format(urun_label,urun_data)) 
        print("#"*60)   

print("Toplam {} kadar ürün bulundu".format(toplamUrun))