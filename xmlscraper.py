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

def searchGenre(genre):
    titles = beauty.find_all('title')
    descs = beauty.find_all('desc')
    channels = beauty.find_all('channel')
    print(channels[0].get_text())
    print(channels[1].get_text())
    for i in range(len(titles)):
        if(i == 10):
            print(data)
            quit()
        print(titles[i].get_text())
        search = imdb.search_for_title(titles[i].get_text())
        if(search != []):
            idno = search[0].get('imdb_id')
            try:
                genres = imdb.get_title_genres(idno).get('genres')
                print(genres)
            except:
                pass
            if genre in genres:
                rating = imdb.get_title_ratings(idno).get('rating')
                data.append([titles[i].get_text(), descs[i].get_text(), channels[i].get_text().replace("\n", ""), genre, rating])
print(data)
