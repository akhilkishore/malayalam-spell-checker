import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from parsel import Selector 

f = open("hrefFList.txt", "r")

data = f.read()

data = data.split("*")

def getWebpage_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup =  BeautifulSoup(webpage, 'html.parser')
    return soup

for x in data:
    if x != "/":
        print(x)
        soup = getWebpage_soup("https://www.mathrubhumi.com"+x)
        text = soup.find_all(text=True)
        print(text)
        break
