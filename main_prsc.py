import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1563396336&s=gateway&sr=8-3'

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup = BeautifulSoup(soup1.prettify(), "html.parser")

    price = soup.find(id="priceblock_ourprice").get_text()

    conv_price = float(price[0:5])
    print(conv_price)

    if (conv_price > 1.000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('paras.gupta986745@gmail.com', 'ejfliftjkezhnsjg')

    sub = 'Price fell down mate!'
    body = 'Check The Link \n https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1563396336&s=gateway&sr=8-3'

    msg = f"Subject: {sub}\n\n{body}"

    # insert the appropriate emails here     
    server.sendmail('sender', 'receiver', msg)

    print('Mail Sent')

    server.quit()


check_price()











