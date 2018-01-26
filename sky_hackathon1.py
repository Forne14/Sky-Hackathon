from tkinter import *

class window(Tk):
    def __init__(self, main):
        Tk.__init__(self)
        main.geometry('{}x{}'.format(800, 600))
        self.var_states(main)
        self.movies = ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5']
        self.labels = []
        self.renderFilms(main)

    master = Tk()

    def var_states(self, main):

        Label(main, text='Choose your favourite movies').grid(row=0, sticky=W)
        self.var = IntVar(main)

        Radiobutton(main, text='action', variable = self.var, value=1).grid(row=1, sticky=W)


        Radiobutton(main, text='comedy', variable = self.var, value =2).grid(row=2, sticky=W)


        Radiobutton(main, text='horror', variable = self.var, value = 3).grid(row=3, sticky=W)


        Radiobutton(main, text='thriller', variable = self.var, value = 4).grid(row=4, sticky=W)


        Radiobutton(main, text='animation', variable = self.var, value = 5).grid(row=5, sticky=W)
        Radiobutton(main, text='foreign', variable = self.var, value = 6).grid(row=6, sticky=W)
        Radiobutton(main, text='kids', variable = self.var, value = 7).grid(row=7, sticky=W)

        Button(main, text='Submit', command = self.mock_scraper).grid(row=8, sticky=W, pady=4)

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

    def mock_scraper(self):
        value = self.var.get()
        if value == 0:
            self.movies = ['Lord of the Rings', 'The Accountant', 'Taken', 'John Wick']
        elif value == 1:
            self.movies = ['Rush Hour', 'Meet Dave', 'Thor Ragnarok', 'The Hangover']
        elif value == 2:
            self.movies = ['Saw', 'Insidious', 'Purge', 'Scream']
        elif value == 3:
            self.movies = ['Get Out' ]
        elif value == 4:
            self.movies = ['Howls Moving Castle']
        elif value == 5:
            self.movies = ['The Blue One']
        elif value == 6:
            self.movies = ['Lion King']
        self.setMovies()



    def setMovies(self):
        self.labels[0].config(text=self.movies[0])
        self.labels[1].config(text=self.movies[1])
        self.labels[2].config(text=self.movies[2])
        self.labels[3].config(text=self.movies[3])
        self.labels[4].config(text=self.movies[4])



if __name__ == '__main__':
    root = Tk()
    root.title("Sky Questionnaire")
    window=window(root)
    root.resizable(width = False, height= False)
    root.configure(background= 'white')
    root.mainloop()


