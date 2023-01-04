import requests 

# Account details 
APP_ID = 'EMAIL' 
APP_SECRET = 'PASSWORD' 

# Get short-lived access token 
url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id={APP_ID}&client_secret={APP_SECRET}".format(APP_ID, APP_SECRET) 
r = requests.get(url) 
access_token = r.json()['access_token'] 
print(access_token) 