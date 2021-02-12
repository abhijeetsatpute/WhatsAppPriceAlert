import requests
import lxml
from bs4 import BeautifulSoup
from twilio.rest import Client
from termcolor import colored
import write_csv
import pandas

def check():
    #Product info
    csv_data = pandas.read_csv('track.csv')
    url = str(csv_data.loc[0,'Product'])
    mobile_num = str(csv_data.loc[0,'Number'])
    price_set = int(str(csv_data.loc[0,'TargetPrice']))

    HEADERS = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(req.content, 'lxml')
    price = (soup.find(id='priceblock_ourprice').text)
    product = soup.find(id='productTitle').text.strip()
    price_curr = int(float((price.split()[1]).replace(',','')))
    if (price_curr < price_set):
        twilio_info = pandas.read_csv('twilio_info.csv')
        account_sid = str(twilio_info.loc[0,'account_sid'])
        auth_token = str(twilio_info.loc[0,'auth_token'])
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='whatsapp:+14155238886',body='Hello! This is a WhatsAppPriceAlert. \n\nYour Price Drop Alert for *'+product+'* \n\nCurrent Price: *'+price+'*'+'\nBuy it ASAP !!\n\n'+url,to='whatsapp:+91' + mobile_num)
        print(colored("Price has been dropped to ","green") + price)
        exit()
    else:
        print("Price remains the same " + price)
        print("\n Rechecking in an hour again.")
