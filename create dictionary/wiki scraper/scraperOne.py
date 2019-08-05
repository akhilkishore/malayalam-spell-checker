import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from parsel import Selector 

#driver = webdriver.Chrome()  

def getWebpage_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup =  BeautifulSoup(webpage, 'html.parser')
    return soup

def main():
    url = "https://www.mathrubhumi.com/"
    #driver.get(url)
    #sleep(5)
    soup =  getWebpage_soup(url)
    f = open("hrefFList.txt", "a")
    hrefList = []
    for a in soup.find_all('a', href=True):
        #if a['href'].text[0] == "/":
        text = a['href']
        try:
            if text[0] == "/":
                hrefList.append(a['href'])
                f.write(a['href'])
                f.write("*")
                print(text)
        except:
            break
    for x in hrefList:
        soup = getWebpage_soup("https://www.mathrubhumi.com"+x)
        for a in soup.find_all('a', href=True):
            try:
                if text[0] == "/":
                    hrefList.append(a['href'])
                    f.write(a['href'])
                    f.write("*")
                    print(a['href'])
            except:
                pass    
main()