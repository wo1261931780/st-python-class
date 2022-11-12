class Director:
    def __init__(self, name):
        self.name = name


class Movie:
    def __init__(self, title, genre, director, studio, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.studio = studio
        self.year = year

    def show_info(self):
        print("this movie {},genre is {},director is {},studio is {},year is {}".format(self.title, self.genre,
                                                                                        self.director, self.studio,
                                                                                        self.year))
