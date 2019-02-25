import twython as tw
import json
from linkedin_v2 import linkedin
#token_twitter=tw.Twython()

client_id="7879dvv96ek1sk"
client_secret="4KC8s5TWnmedxBzN"
host="http://localhost:8000"


authentication = linkedin.LinkedInAuthentication(client_id,client_secret,host,linkedin.PERMISSIONS.enums.values())
print(authentication.AUTHORIZATION_URL)
application = linkedin.LinkedInApplication(authentication)

authentication.get_access_token()