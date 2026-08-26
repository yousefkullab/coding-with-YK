# Note 
# Coin Market Cap API: https://coinmarketcap.com/api
# Coin Market Cap API Documentation : https://coinmarketcap.com/api/documentation/v1
# Telegram >>> Bot Father
# Bot Father : https://core.telegram.org/bots/api
# Telegram >>> IDbot

import requests
import time

api_key = "*****************************************"   # Sensitive Data
bot_key = "*****************************************"   # Sensitive Data
chat_id = "*****************************************"   # Sensitive Data

price_limit = 22000   # Bitcoin Price if become less sent the message of price
time_interval = 10 * 60 # 10 minute * 60 second >>> time to sent request to api 

# get price for Coin Market Cap Method 
def get_price():
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',  # BTC Coin In The First Of The List
        'limit':'3',  # You can convert the limit of number of coins >>> You have over 5000 coin
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    
    response = requests.get(url, headers=headers, params= parameters).json()
    btc_price = response["data"][0]['quote']['USD']['price']  # Get only the price of Bitcoin
    return btc_price

# send message method
def send_update(chat_id, msg):
    
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    
# Driver Code 
def main():
    
    while True:
        price = get_price()
        if price < price_limit:
            print(price)
            send_update(chat_id, f"The Price Of BTC Now {price}")
        time.sleep(time_interval)

main()


# Software Engineer Joseph. 




