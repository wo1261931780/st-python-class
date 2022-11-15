import json


class Movie:
    def __init__(self, title, genre, director, studio, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.studio = studio
        self.year = year

    def show_info(self):  # 简单看一下基本信息
        print("this movie 《{}》,genre -- {},director -- {},studio -- {},year -- {}".format(self.title, self.genre,
                                                                                          self.director, self.studio,
                                                                                          self.year))


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
            title, genre, director, studio, year = line.split(";")  # 分割字符串
            director_temporary = director.split("Director:")[1]  # 分割字符串，保留需要的信息
            # 判断是否有多个导演
            if "," in director_temporary:
                multiple_director = []
                names = str(director_temporary).split(",")
                for i in names:
                    director_demo = dict(Name=i)
                    multiple_director.append(director_demo)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], multiple_director, studio.split(":")[1],
                          year.split(":")[1])
            else:
                single_director = dict(Name=director_temporary)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], single_director, studio.split(":")[1],
                          year.split(":")[1])
            movies.append(m)
    # 打印当前的电影列表，排序
    movies.sort(key=lambda movie: movie.title)
    movie_aspect = []  # 创建一个空列表，保存所有电影的信息
    # 将对象转换为字典
    for m in movies:
        movie_information = dict()  # 整合单个电影信息
        movie_information["title"] = m.title
        movie_information["genre"] = m.genre
        movie_information["director"] = m.director
        movie_information["studio"] = m.studio
        movie_information["year"] = m.year
        movie_aspect.append(movie_information)  # 保存每一部电影
        # 将字典转换为json格式
        # movies_json = json.dumps(movie_dict, ensure_ascii=False)
        # print(movies_json) #测试效果
    # --------------------------------------------------------------------------------
    movie_list_aspect = [] # 将每个电影整合到一个列表中
    for i in movie_aspect:
        movie_inspect = dict(Movie=i)
        movie_list_aspect.append(movie_inspect)
    movies_collection = dict(Movies=movie_list_aspect)
    print(movies_collection)  # 打印最终的字典
    # --------------------------------------------------------------------------------

    with open("C:\\Users\\64234\PycharmProjects\\st-python-class.github.io\\2022年11月11日demo004\movie\\result.json",
              "w") as f:
        json.dump(movies_collection, f)
        print("加载入文件完成...")
    f.close()


if __name__ == '__main__':
    main()
