import time
from selenium import webdriver
from selenium.webdriver.common.by import By
##

from operator import imod

import webbrowser
import pyautogui

import requests
import csv
import os
import arabic_reshaper


from bidi.algorithm import get_display
from bs4 import BeautifulSoup
from itertools import zip_longest
from operator import imod
from turtle import title

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
"""
Selenium-Webdriver needs a browser driver to run, do not forget to download it before running the script!
Instructions on usage:
first things first:
run pip install selenium-webdriver
download geckodriver(if using firefox) or the driver of your preference(this code defaults to firefox, if you
want to use another browser, do not forget to replace the driver build)
For posting into facebook groups you will need to log in first, replace the fields on the code with
your personal data after downloading this source. do not run this code before replacing the data!!
the data on email and password fields are fictional, just for instructional purpouses!
How to replace data:
{1} - Email
{2} - Password
{3} - List of Groups URL 
{4} - Post Content
// Chrome Browser
"""
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    # 'C:\\ProgramFiles\\Google\\Chrome\\Application\\chrome.exe'))
# driver = webdriver.Chrome(ChromeDriverManager().install())

webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Mozilla Firefox\\firefox.exe'))
ser=Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=ser)



# driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.facebook.com")
emailInputField = driver.find_element(By.XPATH,  "//input[@name='email']")

""" {1} Your Email goes down below!"""

emailInputField.send_keys("email")
print('email is done')


passwordInputField = driver.find_element(By.XPATH,  "//input[@name='pass']")

"""{2} Your Password right here"""
passwordInputField.send_keys('password')
print('pass is done')


loginButton = driver.find_element(By.XPATH,  "//button[@name='login']")
loginButton.click()
print('login is done')
time.sleep(5)

"""
{3} - group url:
you must enter the groups URLs as such:
listOfGroups = ["https://linkone.com","https://linktwo.com","https://dontforgetthequotes.com"]
"""
listOfGroups = [ "https://web.facebook.com/groups/links",
                 "https://web.facebook.com/groups/links" ]

for group in listOfGroups:
    driver.get(group)
    time.sleep(2)
    print(group)
    """
    Generally you can't simply choose the posting input field by default because they do element hidding,
    but due to their UX design, once you choose one way of media sending 
    e.g. clicking the "photo/videos" option and then click manually on the "write post"
    the posting input field is triggered and you can finally select it!
    That's the basis for the code below.
    """
    postMediaOptions = driver.find_elements(
        By.CLASS_NAME, 'b6ax4al1 lq84ybu9 hf30pyar om3e55n1')
    time.sleep(5)
    # selecting the "photo/videos"
    postMediaOptions.click()
    time.sleep(5)
    postMediaOptions2 = driver.find_elements(
        By.CLASS_NAME, 'f5m7p0br iwso50tu ggolc4ur js4msrqk bdao358l pbevjfx6 rrjlc0n4 qntmu8s7 tes86rjd pytsy3co tq4zoyjo icdlwmnq d2hqwtrz oxkhqvkx r5g9zsuq nch0832m mfclru0v i6jx4p3a')
    time.sleep(5)
    postMediaOptions2.click()

    time.sleep(5)
    postMediaOptions2.sendkey()
    time.sleep(5)

    postMediaOptions3 = driver.find_elements(
        By.CLASS_NAME, 'om3e55n1 g4tp4svg alzwoclg jez8cy9q jcxyg2ei i85zmo3j sr926ui1 jl2a5g8c k7n6ui8p b41d885q hmqrhxox got7tec9 frfouenu bonavkto djs4p424 r7bn319e bdao358l aesu6q9g e4ay1f3w n75z76so ed17d2qt')
    time.sleep(5)
    postMediaOptions3.click()
    # selecting "write post" and trigger input field

    """{4} Post your text content between the quotes on the line below. protip: you can use "\n" for line breaking. """
    postInputField = driver.find_elements(
        By.CLASS_NAME, '_1p1v')
    postInputField.send_keys("""Hi! i'm your post text, edit meeeee please""")

    time.sleep(5)
    post_element = driver.find_element_by_css_selector(
        'button[data-testid="react-composer-post-button"]')
    time.sleep(5)
    post_element.click()
    time.sleep(2)

    """
    ps: I learnt very introdutory content on selenium, all those "time.sleeps" probably already told you that.
    if i ever need to develop real professional test cases, i'll learn about selenium best practices 
    and develop better, readable code.
    ps2: this script is made only for educational purpouses, do not sell or spam. For properly posting, please
    refer yourself to Facebook's very own API.
    """
