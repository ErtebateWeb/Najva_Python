import requests
from datetime import timedelta
import datetime
import json
from time import sleep
import config
url = "https://app.najva.com/api/v1/notifications/"
#print(url)
currentDT = datetime.datetime.now()
now_plus_10s=currentDT+timedelta(seconds=+10)
now = now_plus_10s.strftime("%Y-%m-%dT%H:%M:%SZ")
#print(currentDT)
#print(now_plus_10s)
#time = datetime.datetime.now() + timedelta(minutes=10) # this time is an example. replace it with your own time.
#print(time)
#print("+++++++++++++")
#print(now_plus_5m.strftime("%Y/%m/%d - %H:%M:%S"))
symbol='BNBUSDT'
price =270
data={
  "api_key":config.apikey,
    "title":symbol,
    "body":f"{symbol} Triggered on {price}",
    "onclick_action":"open-link",
    "url":f"https://www.binance.com/en/trade/{symbol}?layout=pro",
    "content":f"{symbol} Price : {price}",
    # "content":"image should be ۳۶۰×۷۲۰ or 720x300",
    "icon":"https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/icon/bnb.png",
    # "image":"https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/icon/bnb.png",
    "sent_time": now ,
    "one_signal_enabled":"false"
}
#print(data)
payload = json.dumps(data)
headers = {
    'authorization': f"Token {config.token}",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.json())
#print(response.text)