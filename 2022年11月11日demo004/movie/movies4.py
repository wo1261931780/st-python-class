import json


class Director2:
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
                    director_demo = dict(Name=i)
                    Directors.append(director_demo)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], Directors, studio.split(":")[1],
                          year.split(":")[1])
            else:
                # d = Director2(director_temporary)
                Directors2 = dict(Name=director_temporary)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], Directors2, studio.split(":")[1],
                          year.split(":")[1])
            movies.append(m)
    # 打印当前的电影列表，排序
    movies.sort(key=lambda movie: movie.title)
    # for m in movies:
    #     m.show_me_json_info()
    # 添加一个固定格式的字典，然后将其转换为json格式
    movie_list = []  # 创建一个空列表，保存所有电影的信息
    for m in movies:
        movie_dict = dict()  # 创建一个空字典，保存单个电影的信息
        movie_dict["title"] = m.title
        movie_dict["genre"] = m.genre
        movie_dict["director"] = m.director
        movie_dict["studio"] = m.studio
        movie_dict["year"] = m.year
        print(movie_dict)
        print(type(movie_dict))
        movie_list.append(movie_dict)  # 添加到列表中
        # 将字典转换为json格式
        movies_json = json.dumps(movie_dict, ensure_ascii=False)
        print(movies_json)
        print(type(movies_json))
    f.close()


if __name__ == '__main__':
    main()
