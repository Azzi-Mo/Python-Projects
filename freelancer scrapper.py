# import requests
# from bs4 import BeautifulSoup

# # set the URL you want to scrape from
# url = 'https://www.freelancer.com/jobs/'

# # download the URL and extract the content to the variable ‘html’
# response = requests.get(url)
# html = response.content

# # parse the html content 
# soup = BeautifulSoup(html, "lxml")  # choose lxml parser 

#  # find all job postings 
# scrapper_jobs = soup.find_all('div', {'class': 'JobSearchCard-item-inner'}) 

#  # extract job title, location and link for each posting 
# for job in scrapper_jobs:

#     # get job title 
#     job_title = job.find('a', {'class': 'JobSearchCard-primary-heading-link'}).text

#     # get job location 
#     job_location = job.find('span', {'class': 'JobSearchCard-primary-location'}).text

#     # get link to job posting page 
#     link = "https://www.freelancer.com" + job.find('a', {'class': 'JobSearchCard-primary-heading-link'})['href']

#     print("Job Title:",job_title,"\nLocation:",job_location,"\nLink:",link,"\n")

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
  
# creating new instance of chrome 
browser = webdriver.Chrome() 
  
# open freelancer website  
browser.get('https://www.freelancer.com/') 
  
# wait for page to load properly 
wait = WebDriverWait(browser, 10) 
  
# search for jobs related to scrapper jobs  
search_input = wait.until(EC.presence_of_element_located((By.NAME, "q"))) 
search_input.send_keys('scrapper jobs') 

 # click on the search button   
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[1]/div[2]/div[2]/div[2]/form/button')))    # click on the search button    search_button = wait .until(EC .element _to _be _clickable((By .XPATH , '//* [@id="page"] /div [1] /div [2] /div [2] /div [2] /form /button')))    search_button .click ()     # get the list of all jobs related to scrapper jobs    job _list = wait .until(EC .presence _of _all _elements _located ((By .CLASS _NAME , "JobSearchCard-primary-heading-link")))      # iterate over each job and print details     for job in job _list :        title = job .text        link = job .get _attribute("href")        print("Title: {}\nLink: {}\n".format (title , link))