import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from parsel import Selector 


#data = f.read()

#data = data.split("*")

data =["https://ml.wikipedia.org/wiki/%E0%B4%85%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%81_%E0%B4%A8%E0%B5%86%E0%B4%9F%E0%B5%81%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B4%BE%E0%B4%9F%E0%B4%BF"]
def getWebpage_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup =  BeautifulSoup(webpage, 'html.parser')
    return soup
links = []
all = []
for x in data:
    if x != "":
        #print(x)
        try:
                soup = getWebpage_soup(x)
                #text = soup.find_all(text=True)
                #print(text)
                #break
                data = []
                for p in soup.find_all('p'):
                        #print(p.text)
                        data.append(p.text)
                all.append(data)
                #link = soup.find_all('a', href=)
                for a in soup.find_all('a', href=True):
                        if "/wiki/%" in a['href']:
                                #print(a['href'])
                                #print("\n\n")
                                if "https://ml.wikipedia.org"+a['href'] not in links:
                                        links.append("https://ml.wikipedia.org"+a['href'])
        except:
                pass

f = open("demofile2.txt", "a")
for x in links:
    if x != "":
        print(x)
        #print(x)
        soup = getWebpage_soup(x)
        #text = soup.find_all(text=True)
        f.write("Now the file has more content!")
        f.close()
        #print(text)
        #break
        data = []
        for p in soup.find_all('p'):
                #print(p.text)
                data.append(p.text)
        all.append(data)
print(links)