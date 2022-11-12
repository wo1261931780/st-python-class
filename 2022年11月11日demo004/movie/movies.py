class Director:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Movie:
    def __init__(self, title, genre, director, studio, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.studio = studio
        self.year = year

    def show_info(self):
        print("this movie 《{}》,genre -- {},director -- {},studio -- {},year -- {}".format(self.title, self.genre,
                                                                                          self.director, self.studio,
                                                                                          self.year))


# 定义一个函数去读取文本数据
# 定义一个电影对象,属性就是名称,类型,导演,制片厂,年份
# 定义一个导演对象,包括姓名
# 电影对象中的导演是list类型的对象列表
# 然后使用分隔符,将其分开存到不同的列表中

# 最后输出的时候,使用遍历,将其拼接到一起

def main():
    movies = []
    Directors = []
    with open("movies.txt", encoding="utf-8") as f:
        for line in f:
            print("我是读取的数据：", line)
            title, genre, director, studio, year = line.split(";")
            print("我是分割后的数据：", title, genre, director, studio, year)
            d = Director(director.split(":")[1])
            Directors.append(d)
            print("我是导演对象：", d.name)
            m = Movie(title.split(":")[1], genre.split(":")[1], d, studio.split(":")[1], year.split(":")[1])
            print("我是电影对象：", m.title, m.genre, m.director, m.studio, m.year)
            movies.append(m)
    for m in movies:
        m.show_info()

    f.close()


# def Iterator():

if __name__ == '__main__':
    main()
