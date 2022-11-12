import XMLGererator

class Director:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def show_me_json_info(self):
        print("{" + "\"name\":" + "\"" + self.name + "\"},")


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

    def show_me_json_info(self):
        print("{" + "\"Movie\":[")
        print("{" + "\"title\":" + "\"" + self.title + "\"},")
        print("{" + "\"genre\":" + "\"" + self.genre + "\"},")
        # print("\"director\":" + "\"" + self.director + "\",")
        print("{" + "\"Director\":[")
        if type(self.director) == list:
            for i in self.director:
                i.show_me_json_info()
        else:
            self.director.show_me_json_info()
        print("]},")
        print("{" + "\"studio\":" + "\"" + self.studio + "\"},")
        print("{" + "\"year\":" + self.year + "},")
        print("]},")


# 定义一个函数去读取文本数据
# 定义一个电影对象,属性就是名称,类型,导演,制片厂,年份
# 定义一个导演对象,包括姓名
# 电影对象中的导演是list类型的对象列表
# 然后使用分隔符,将其分开存到不同的属性中

# 最后输出的时候,使用遍历,将其拼接到一起

# 2022年11月12日17:16:38，json输出已经完成，项目说明中给出的json格式是有问题的

def main():
    movies = []
    with open("movies.txt", encoding="utf-8") as f:
        for line in f:
            title, genre, director, studio, year = line.split(";")
            director_temporary = director.split("Director:")[1]
            if "," in director_temporary:
                Directors = []
                names = str(director_temporary).split(",")
                for i in names:
                    director_demo = Director(i)
                    Directors.append(director_demo)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], Directors, studio.split(":")[1],
                          year.split(":")[1])
            else:
                d = Director(director_temporary)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], d, studio.split(":")[1], year.split(":")[1])
            movies.append(m)
    # 打印当前的电影列表，排序
    movies.sort(key=lambda movie: movie.title)
    for m in movies:
        m.show_me_json_info()

    f.close()


if __name__ == '__main__':
    main()
