import requests
import lxml
from bs4 import BeautifulSoup
from twilio.rest import Client
import twilio_info

if __name__ == "__main__":
    url = input("Enter the product Link: ")
    mobile_num = input("\nEnter your Phone number to recieve Alerts: +91-")

    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(req.content, 'lxml')
    price = (soup.find(id='priceblock_ourprice').text)
    product = soup.find(id='productTitle').text.strip()
    message = twilio_info.send(product,price,mobile_num)
    print('Your Price Alert Has Been Set.'+'\n'+message.sid)
