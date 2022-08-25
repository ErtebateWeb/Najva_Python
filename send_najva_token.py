from najva_api_client.najva import Najva
import config

client = Najva()

client.apikey = config.apikey
client.token = config.token

str = client.send_to_users(title="Title",body="Some Description", url="https://google.com",
icon="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
image="https://www.ait-themes.club/wp-content/uploads/cache/images/2020/02/guestblog_featured/guestblog_featured-482918665.jpg",
onclick="open-link", 
subscriber_tokens=config.subscriber_token,)

print(str)
