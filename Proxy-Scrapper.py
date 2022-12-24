import requests
import urllib3
import random
from bs4 import BeautifulSoup as bs
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException






# 'US' : 'https://www.us-proxy.org/',
links = {

'SSL' : 'https://www.sslproxies.org/',
'GOOGLE' : 'https://www.google-proxy.net/',
'ANANY' : 'https://free-proxy-list.net/anonymous-proxy.html',
'UK' : 'https://free-proxy-list.net/uk-proxy.html',
'NEW' : 'https://free-proxy-list.net/',
'SPYS_ME' : 'http://spys.me/proxy.txt',
'PROXYSCRAPE' : 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
'PROXYNOVA' : 'https://www.proxynova.com/proxy-server-list/',
'PROXYLIST_DOWNLOAD_HTTP' : 'https://www.proxy-list.download/HTTP',
'PROXYLIST_DOWNLOAD_HTTPS' : 'https://www.proxy-list.download/HTTPS',
'PROXYLIST_DOWNLOAD_SOCKS4' : 'https://www.proxy-list.download/SOCKS4',
'PROXYLIST_DOWNLOAD_SOCKS5' : 'https://www.proxy-list.download/SOCKS5',
'ALL':'ALL'

# SSL = 'https://www.sslproxies.org/',
# GOOGLE = 'https://www.google-proxy.net/',
# ANANY = 'https://free-proxy-list.net/anonymous-proxy.html',
# UK = 'https://free-proxy-list.net/uk-proxy.html',
# US = 'https://www.us-proxy.org/',
# NEW = 'https://free-proxy-list.net/',
# SPYS_ME = 'http://spys.me/proxy.txt',
# PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
# PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
# PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
# PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
# PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
# PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'
# ALL = 'ALL'

}

for key, value in links.items():
    # print( value)
    scrapper = Scrapper(category=value, print_err_trace=False)
    data = scrapper.getProxies()
    # proxies = []
    # Print These Scrapped Proxies
    print("Scrapped Proxies:")
    for item in data.proxies:
        proxies = '{}:{}'.format(item.ip, item.port)
        # print(proxies)
        # print(item)

    def get_session(proxies):
            # construct an HTTP session
            session = requests.Session()
            # choose one random proxy
            proxy = random.choice(proxies)
            session.proxies = {"http": proxy, "https": proxy}
            return session
    for i in range(5):
            s = get_session(proxies)
            try:
                print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
            except Exception as e:
                continue

# # Print the size of proxies scrapped
# print("Total Proxies")
# print(data.len)

# # Print the Category of proxy from which you scrapped
# print("Category of the Proxy")
# print(data.category)