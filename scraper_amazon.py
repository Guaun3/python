"""
An app that tracks amazon prices
"""

import requests  # access URL and pull out actual data from website
from bs4 import BeautifulSoup  # parse the data and pull out individual items
import smtplib  # sending emails using the Simple Mail Transfer Protocol (SMTP)
from email.mime.text import MIMEText
import time

# seiko prospex us special edition ocean conservation turtle diver
URL = 'https://www.amazon.ca/dp/B09QFXW7QB/?coliid=I1L281EGDAEKXN&colid=7IL60ZIC7Q8C&psc=1&ref_=lv_ov_lig_dp_it.html'

# Headers for request
# Issue1 : cannot fetch the webpage!!
HEADERS = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
           'Accept-Language': 'en-US'}
HEADERS1 = {"User-Agent":
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def get_title(soup):
    try:
        # Tag Object
        title = soup.find("span", attrs={'id': 'productTitle'})
        # print(type(title))

        # NavigatableString Object
        value = title.string
        # print(type(value))

        # string value
        strip_result = value.strip()
        # print(type(strip_result))
    except AttributeError:
        strip_result = ""

    return strip_result


def get_price(soup):
    # get the price
    try:
        price = soup.find(id='priceblock_ourprice').string.strip()

    except AttributeError:  # i.e. 'NoneType' object has no attribute 'string'

        try:
            price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip()
        except:
            price = ""

    return price


def send_email():
    # set up gmail account for development
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()   # encrypt and secure the connection
    # server.ehlo()

    sender = 'gyequalgy@gmail.com'
    password = 'tctluqatguucatxd'   # generated app password on google
    receiver = 'guanyunshan@qq.com'

    # build message
    msg = MIMEText('Secured test mail')
    msg['Subject'] = 'Test mail'
    msg['From'] = sender
    msg['To'] = receiver

    # connect to SMTP server and send message
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # encrypt and secure the connection

        # authenticate with an email server
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("mail successfully sent")


if __name__ == '__main__':

    # want to check every day
    # while True:
        # HTTP request
        webpage = requests.get(URL, headers=HEADERS)  # get all data from web

        if webpage.status_code != 200:
            print("Error fetching page")
            exit()
        else:
            # Soup Object containing all data
            # soup = BeautifulSoup(webpage.content, "lxml") OR
            soup = BeautifulSoup(webpage.content, 'html.parser')
            title = get_title(soup)
            price = get_price(soup)
            print(f"product title: {title}")
            print(f"product price: {price}")

            if price != "":
                int_price = float(price[1:])
                print(int_price)
                if int_price < 650:
                    send_email()

        # pause execution for 1 day
        # time.sleep(60*60*24)