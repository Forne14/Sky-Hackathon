from tkinter import *
import urllib.request
from imdbpie import Imdb
from bs4 import BeautifulSoup
import datetime

class window(Tk):
    def __init__(self, main):
        Tk.__init__(self)
        main.geometry('{}x{}'.format(1600, 600))
        self.var_states(main)
        self.movies = ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5']
        self.genres = ['Action', 'Comedy', 'Horror', 'Thriller', 'Animation', 'Foreign', 'Kids']
        self.labels = []
        self.renderFilms(main)

        self.imdb = Imdb()
        url = "http://www.xmltv.co.uk/feed/7147"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        xml = response.read().decode('utf-8')

        self.beauty = BeautifulSoup(xml)
        self.data = []

        master = Tk()

    def var_states(self, main):

        Label(main, text='Choose your favourite movies').grid(row=0, sticky=W)
        self.var = IntVar(main)

        Radiobutton(main, text='Action', variable = self.var, value=0).grid(row=1, sticky=W)


        Radiobutton(main, text='Comedy', variable = self.var, value =1).grid(row=2, sticky=W)


        Radiobutton(main, text='Horror', variable = self.var, value =2).grid(row=3, sticky=W)


        Radiobutton(main, text='Thriller', variable = self.var, value = 3).grid(row=4, sticky=W)


        Radiobutton(main, text='Animation', variable = self.var, value = 4).grid(row=5, sticky=W)
        Radiobutton(main, text='Foreign', variable = self.var, value = 5).grid(row=6, sticky=W)
        Radiobutton(main, text='Kids', variable = self.var, value = 6).grid(row=7, sticky=W)

        Button(main, text='Submit', command = lambda:self.searchGenre(self.genres[self.var.get()])).grid(row=8, sticky=W, pady=4)

    def renderFilms(self, main):

        label1 = Label(main, text=self.movies[0])
        label1.grid(row=10, sticky=W)


        label2 = Label(main, text=self.movies[1])
        label2.grid(row=11, sticky=W)


        label3 = Label(main, text=self.movies[2])
        label3.grid(row=12, sticky = W)

        label4 = Label(main, text=self.movies[3])
        label4.grid(row=13, sticky = W)

        label5 = Label(main, text=self.movies[4])
        label5.grid(row=14, sticky = W)

        self.labels= [label1, label2, label3, label4, label5]
        
    def searchGenre(self, genre):
        self.data = []
        for i in range(len(self.labels)):
            self.labels[i].config(text = self.movies[i])
        titles = self.beauty.find_all('title')
        descs = self.beauty.find_all('desc')
        channels = self.beauty.find_all('channel')
        print(channels[0].get_text())
        print(channels[1].get_text())
        for i in range(len(titles)):
            if(i == 10):
                print(self.data)
                break
            print(titles[i].get_text())
            search = self.imdb.search_for_title(titles[i].get_text())
            if(search != []):
                idno = search[0].get('imdb_id')
                try:
                    genres = self.imdb.get_title_genres(idno).get('genres')
                    print(genres)
                except:
                    pass
                if genre in genres:
                    rating = self.imdb.get_title_ratings(idno).get('rating')
                    self.data.append([titles[i].get_text(), descs[i].get_text(), channels[i].get_text().replace("\n", ""), genre, rating])
                for j in range(len(self.data)):
                    if j>=5:
                        pass
                    self.labels[j].config(text=self.data[j])



if __name__ == '__main__':
    root = Tk()
    root.title("Sky Questionnaire")
    window=window(root)
    root.resizable(width = False, height= False)
    root.configure(background= 'white')
    root.mainloop()


