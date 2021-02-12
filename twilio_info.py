from twilio.rest import Client

account_sid = 'AC37a52affa939075892dd7aa4bb523561'
auth_token = '7eb64fe09b0afe4caa8b8fa101f1f7b0'
client = Client(account_sid, auth_token)

def send(product,price,mobile_num):
    client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello! This is a WhatsAppPriceAlert. \nYour Price Alert Has Been Set.\n\nYour product *'+product+'* \nhas a current Price of *'+price+'*',
                              to='whatsapp:+91' + mobile_num
                          )
