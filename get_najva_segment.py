import requests
import config
url = f"https://app.najva.com/api/v1/websites/{config.apikey}/segments/"

headers = {
    'content-type': "application/json",
    'authorization': f"Token {config.token}",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, headers=headers)

print(response.text)