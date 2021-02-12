import requests
import lxml
from bs4 import BeautifulSoup
from twilio.rest import Client
from termcolor import colored
import write_csv
import pandas
import track
import schedule
import time

if __name__ == "__main__":
    url = input(colored("Enter the product Link: ","blue"))
    mobile_num = input(colored("\nEnter your Phone number to recieve Alerts: +91-","blue"))
    price_set = input(colored("\nEnter the Target Price: ","red"))

    write_csv.save(url, mobile_num, price_set)

    HEADERS = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(req.content, 'lxml')
    price = (soup.find(id='priceblock_ourprice').text)
    product = soup.find(id='productTitle').text.strip()
    price_curr = float((price.split()[1]).replace(',',''))

    twilio_info = pandas.read_csv('twilio_info.csv')
    account_sid = str(twilio_info.loc[0,'account_sid'])
    auth_token = str(twilio_info.loc[0,'auth_token'])
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello! This is a WhatsAppPriceAlert. \n\nYour Price Alert Has Been Set.\n\nYour product *'+product+'* \n\nCurrent Price: *'+price+'*'+'\nTarget Price set: *'+price_set+'*',
                              to='whatsapp:+91' + mobile_num
                          )
    print(colored('\nYour Price Alert Has Been Set.'+'\n',"green")+message.sid)
    print(colored('\nChecking...','red'))
    track.check()
    schedule.every().hour.do(track.check)
    while True:
        schedule.run_pending()
        time.sleep(1)
