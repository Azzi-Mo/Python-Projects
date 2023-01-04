# import necessary libraries 
import requests 
import json 

# set the Facebook Graph API URL 
url = 'https://graph.facebook.com/v2.6/{}?fields=likes.summary(true),comments.summary(true)&access_token={}'

# set the access token for the Graph API call 
access_token = 'YOUR_ACCESS_TOKEN' 

# set the post id to fetch data from 
post_id = 'POST_ID' 

# make a GET request to the Graph API URL 
response = requests.get(url.format(post_id, access_token)) 
if response.status_code == 200: 

    # convert response to JSON format  
    data = json.loads(response.content)

    # get the number of likes and comments from JSON response  
    likes = data['likes']['summary']['total_count']  
    comments = data['comments']['summary']['total_count']  

    # print the results  
    print('Likes: {}'.format(likes))  
    print('Comments: {}'.format(comments))