import requests
import lxml
import csv
from bs4 import BeautifulSoup
from twilio.rest import Client
import twilio_info

if __name__ == "__main__":
    url = input("Enter the product Link: ")
    mobile_num = input("\nEnter your Phone number to recieve Alerts: +91-")
    price_set = input("\nEnter the Target Price: ")

    with open('track.csv', mode='w') as tracker:
        tracker_writer = csv.writer(tracker, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tracker_writer.writerow(['Product', 'Number', 'TargetPrice'])
        tracker_writer.writerow([url, mobile_num, price_set])

    HEADERS = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(req.content, 'lxml')
    price = (soup.find(id='priceblock_ourprice').text)
    product = soup.find(id='productTitle').text.strip()
    message = twilio_info.send(product,price,mobile_num)
    print('Your Price Alert Has Been Set.'+'\n'+message.sid)
