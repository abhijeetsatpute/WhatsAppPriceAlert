# WhatsAppPriceAlert
Whatsapp Price Drop Alert on Amazon Products.
<br/>
[repl](https://repl.it/@Stan69/WhatsAppPriceNotifier)
<br/>
 The following python Dependencies are required.
```
pip install lxml
pip install beautifulsoup4
pip install requests
pip install twilio
pip install pandas
pip install schedule
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

Use [hickory](https://github.com/maxhumber/hickory) to Schedule track.py to execute every 60 minutes
```
hickory schedule track.py --every=60minutes
```
