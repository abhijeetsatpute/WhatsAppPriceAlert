# WhatsAppPriceAlert
Whatsapp Price Drop Alert on Amazon Products.
<br/>
[repl](https://repl.it/@Stan69/WhatsAppPriceNotifier)
<br/>
 The following python Dependencies are required.
```
pip install lxml beautifulsoup4 requests twilio schedule termcolor
```

 Usage:
```
python main.py
```
Saves the product details into a csv file.

<b>
Use a task scheduler to run the track.py script at specific intervals to check for price drops and notify.
</b>

<br><br>

Use [Schedule](https://pypi.org/project/schedule/) to Schedule track.check to execute every hour/seconds/minutes.
```
import schedule
import time

def check():
    Check for current price
    if current price < price_set:
      Send notification and exit()

schedule.every(10).seconds.do(track.check)
schedule.every(10).minutes.do(track.check)
schedule.every().hour.do(track.check)
schedule.every().day.at("10:30").do(track.check)
schedule.every(5).to(10).minutes.do(track.check)
schedule.every().monday.do(track.check)
schedule.every().wednesday.at("13:15").do(track.check)
schedule.every().minute.at(":17").do(track.check)

while True:
    schedule.run_pending()
    time.sleep(1)
```
