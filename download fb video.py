
import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/video_url' # replace with the video URL you want to download
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
video_tag = soup.find('video', {'class': 'video-stream'})
video_url = video_tag['src']
print('Video URL:', video_url)  # print the video URL to the console

# Download the video in different qualities 
qualities = ['hd', 'sd', 'low']  # list of qualities for downloading 
for quality in qualities:  # iterate through each quality in the list 

    # construct the download URL with the given quality and print it to console 
    download_url = video_url + '&quality=' + quality 
    print('Download URL for ' + quality + ' quality:', download_url)  

    # use the requests library to download the file from the constructed URL 
    r = requests.get(download_url, allow_redirects=True)  

    # save the downloaded file with a meaningful name  
    open('facebook-video-' + quality + '.mp4', 'wb').write(r.content)