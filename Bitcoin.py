# from inspect import Parameter
# from sqlite3.dbapi2 import _Parameters
from email.quoprimime import quote
from operator import le
import requests
import time

api_key = '651ff5cf-dcf3-4875-b633-3497b899e6ef'
bot_token = '5451528270:AAHuZ-e8sUDyNoGBSS4uxksE4AsUn-b4sO8'
chat_id = '5007476244'
limit  = 0.6298407534344672
time_interval = 1 * 60

# def get_price():
#     url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#     parameters = {
#         'start':'1',
#         'limit':'2',

#         }

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': api_key ,}


#     respose = requests.get(url ,headers=headers , params=parameters ).json()
#     btc_price = respose['data'][0]['quote']['USD']['price']
#     return btc_price
#     # return respose

# print(get_price())

def send_update(chat_id,msg):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}'  
    requests.get(url)
send_update(chat_id , 'hi Mo')
# def main():
#         while True:
#             price = get_price()
#             if price > limit:
#                send_update(chat_id,f'باشاااااا سعر البتكوين علي بقي ب {price}')
#             time.sleep(time_interval)
# main()