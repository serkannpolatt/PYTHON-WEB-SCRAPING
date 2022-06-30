from cgi import print_exception
from email import header
import smtplib
import time
from django.dispatch import receiver
from matplotlib.pyplot import title
from pywhatkit import send_mail
import requests
import imp
from wsgiref import headers
from bs4 import BeautifulSoup
from requests import head, request

url="https://www.hepsiburada.com/apple-watch-seri-6-44mm-gps-product-red-aluminyum-kasa-ve-kirmizi-spor-kordon-m00m3tu-a-pm-HB00000XBQMJ"

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}


def check_price():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='product-name').get_text().strip()
    title=title[0:18]
    print(title)
    span=soup.find(id='offering-price')
    content=span.attrs.get('content')
    price=float(content)
    print(price)
    if(price<9500):
        send_mail(title)

def send_mail(title):
    sender='.....@gmail.com'
    receiver='.....@gmail.com'
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'cbusqteyomhzmczq')
        subject=title+'price down'
        body='Bu linkten gidebilirsin ->' + url
        mailContent=f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailContent)
        print('mail gonderildi')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while(1):
    check_price()
    time.sleep(60*60)
