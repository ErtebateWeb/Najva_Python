import requests
import json as json_parser
from datetime import datetime, timedelta
import config
from requests.models import Response

class Najva:

    apikey = config.apikey
    token = config.token

    # api to send notification for all subscribers.
    def send_to_all(self,title, body, url, icon, onclick='open-link', image=None, 
        content=None,json=None,sent_time=None, segment_include=None,
        segment_exclude=None, one_signal_enabled=False, one_signal_accounts=None):
    
        url = "https://app.najva.com/api/v1/notifications/"

        if sent_time==None:
            sent_time = datetime.now() + timedelta(minutes=1)

        body = {
            'api_key': self.apikey,
            'title': title,
            'body': body,
            'onclick-action': onclick,
            'url': url,
            'content': content,
            'icon': icon,
            'image': image,
            'json' : '"%s"' %json,
            'sent_time': sent_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'segment_include': segment_include,
            'segment_exclude': segment_exclude,
            'one_signal_enabled': one_signal_enabled,
            # 'one_signal_accounts': one_signal_accounts,
        }

        headers = {
            'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request(method="POST", url=url, data=json_parser.dumps(body), headers=headers)

        return response.text


    ## api to send notification for specific users
    def send_to_users(self,title, body, url, icon,subscriber_tokens, onclick='open-link', image=None, 
        content=None,json=None,sent_time=None):
    
        url = 'https://app.najva.com/notification/api/v1/notifications/'

        if sent_time==None:
            sent_time = datetime.now() + timedelta(minutes=1)


        body = {
            'api_key': self.apikey,
            'title': title,
            'body': body,
            'onclick-action': onclick,
            'url': url,
            'content': content,
            # 'json': '"%s"' % json,
            'icon': icon,
            'image': image,
            'sent_time': sent_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'subscriber_tokens': subscriber_tokens,
      
        }

        headers = {
            'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request(method="POST", url=url, data = json_parser.dumps(body), headers= headers)

        return response.text



    # get segment ids.
    def get_segments(self):
        url = "https://app.najva.com/api/v1/websites/%s/segments/" % apikey
        headers = {
           'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
        response = requests.request("GET", url, headers=headers)
        return response.text


    # get created accounts ids.
    def get_onesignal_accounts(self):
        url = "https://app.najva.com/api/v1/one-signals/"
        headers = {
            'authorization': "Token %s" % self.token,
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers)
        return response.text


if __name__ == "__main__":
    najva = Najva()
    najva.apikey = config.apikey
    najva.token = config.token
    sub_token =config.subscriber_token

    response = najva.send_to_all(title="title", body="some test data", url="https://najva.com", 
                icon="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
                json={'key':'value'})
    print(response)

    response =  najva.send_to_users(title="salam moji", body="in faghat baraye chrome to hast", url="https://najva.com", 
                icon="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
                subscriber_tokens=sub_token)
    print(response)
