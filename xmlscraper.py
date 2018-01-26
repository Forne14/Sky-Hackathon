import urllib.request
from imdbpie import Imdb
from bs4 import BeautifulSoup
from xml.dom import minidom

imdb = Imdb()
url = "http://www.xmltv.co.uk/feed/7147"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
xml = response.read().decode('utf-8')

beauty = BeautifulSoup(xml)
data = []

i=0
titles = beauty.find_all('title')
descs = beauty.find_all('desc')
channels = beauty.find_all('channel')
print(channels[0].get_text())
print(channels[1].get_text())
for i in range(len(titles)):
    data.append([titles[i].get_text(), descs[i].get_text(), channels[i].get_text().replace("\n", "")])
    print(data[i])
    if(i==10):
        print(data)
        quit()
print(data)
