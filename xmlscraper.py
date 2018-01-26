import urllib.request
from bs4 import BeautifulSoup
from xml.dom import minidom

url = "http://www.xmltv.co.uk/feed/7147"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
xml = response.read().decode('utf-8')

beauty = BeautifulSoup(xml)
mydoc = minidom.parse(beauty)
items = mydoc.getElementsByTagName('title')
print(items)

data = []

i=0
for title in beauty.find_all('title'):
    for desc in beauty.find_all('desc'):
        data.append([title, desc])
        i +=1
        print(i)
        if(i == 10):
            for i in range(len(data)):
                print(data[i])
            quit()
        
