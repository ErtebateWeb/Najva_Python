
import datetime
import json ,requests , config
from time import sleep
import time
# from timeloop import Timeloop
from datetime import timedelta
url = "https://app.najva.com/api/v1/notifications/"
# print(url)
currentDT = datetime.datetime.now()
now_plus_10s = currentDT + timedelta(seconds=+180)
now = now_plus_10s.strftime("%Y-%m-%dT%H:%M:%SZ")




data = {"api_key": config.apikey,
                "title": f"Screenerplus.ir",
                "body": f"سایت با امکانات جدید بروز شد",
                "subscriber_tokens": config.subscriber_token,
                "onclick_action": "open-link",
                "url": f"https://screenerplus.ir/",
                "content": f"سایت با امکانات جدید بروز شد",
                # "content":"image should be ۳۶۰×۷۲۰ or 720x300",
                "icon": f"https://screenerplus.ir/static/dist/img/AdminLTELogo.jpg",
                # "image":"https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@9ab8d6934b83a4aa8ae5e8711609a70ca0ab1b2b/128/icon/bnb.png",
                "sent_time": now,
                "one_signal_enabled": "false"
                }
payload = json.dumps(data)
headers = {
        'authorization': f"Token {config.token}",
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.json())
