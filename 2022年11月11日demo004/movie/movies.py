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


# 定义一个函数去读取文本数据
# 定义一个电影对象,属性就是名称,类型,导演,制片厂,年份
# 定义一个导演对象,包括姓名
# 电影对象中的导演是list类型的对象列表
# 然后使用分隔符,将其分开存到不同的列表中

# 最后输出的时候,使用遍历,将其拼接到一起

def main():
    movies = []
    with open("movie.txt", encoding="utf-8") as f:
        for line in f:
            title, genre, director, studio, year = line.split(",")
            d = Director(director)
            m = Movie(title, genre, d, studio, year)
            movies.append(m)
    for m in movies:
        m.show_info()
with open("movies.txt") as f:
    text_data = f.readlines()
    # while not data is None: # 避免重复调用
    print("我是读取的数据：", text_data)
    print(type(text_data))  # list

    for d in text_data:
        print("我是当前行：", d)
        if d == "[\n":
            print("我是if：", d)
            new_movie = Movie()
            while d != "]\n":
                print("我是while：", d)
                new_movie.title = d
            print("我是if结束：", d)

f.close()

# def Iterator():

if __name__ == '__main__':
    main()
