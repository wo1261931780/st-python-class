import json


# 首先分析一下对象的结构：
# 一个movie就是一个对象
# 一个movie中可以允许多个导演对象同时存在
# 一个导演内部又分别有不同的属性

# 整体的结构是：
#     movie对象
#         title片名属性+genre类型属性+studio制片厂属性+year年份属性+list<Director>导演列表属性
#     director
#         name姓名属性

# ========================================================
# 需求分析：
# 1.创建一个Movies.txt文件
# 2.文件中包含至少四种不同电影类型（题材）的至少 10 部电影
# 题材举例：动作(action)、动画(animation)、喜剧(comedy)、剧情(drama)、虚构(fiction)、恐怖(horror)
# 3.文件必须包含movie对象中的所有属性
# 4.所有电影片名都必须不同，以此为键对movie对象完成排序
# 5.以将文件放在程序的本地目录中
# 6.写一个python程序，能直接读取上面文件中的数据
# 7.读取完成后，生成 JSON 数据结构
# 8.字典结构存储 JSON 结构，结构必须和上面的要求一致
# 9.添加 Sort 函数,对名称排序
# 10.将排序后的json保存
# 11.添加 XmlGeneration 函数
# 12.读取排序后的json数据,将其生成xml树
# 13.XML 文件的根元素是”Movies”
# 14.将 XML 树保存至名为“Movies.xml”的文件中
# ========================================================

class Movie:
    def __init__(self, title, genre, director, studio, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.studio = studio
        self.year = year

    def print_movie(self):
        print("《{", self.title, "}》,genre : ", self.genre, ",director : ", self.director, ",studio : ",
              self.studio, ",year : ", self.year, "。")


def main():
    movies = []
    with open("movies_json.txt", encoding="utf-8") as read_file:
        for line in read_file:
            title, genre, director, studio, year = line.split(";")  # 分割字符串
            director_temporary = director.split("Director:")[1]  # 分割字符串，保留需要的信息
            # 判断是否有多个导演
            if "," in director_temporary:
                multiple_director = []
                names = str(director_temporary).split(",")
                for i in names:
                    director_demo = dict(Name=i)
                    multiple_director.append(director_demo)
                m = Movie(title.split("Title:")[1], genre.split(":")[1], multiple_director,
                          studio.split(":")[1],
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
    movie_list_aspect = []  # 将每个电影整合到一个列表中
    for i in movie_aspect:
        movie_inspect = dict(Movie=i)
        movie_list_aspect.append(movie_inspect)
    movies_collection = dict(Movies=movie_list_aspect)
    print(movies_collection)  # 打印最终的字典
    # --------------------------------------------------------------------------------

    with open(
            "/2023年2月10日项目2/Movies.json",
            "w") as read_file:
        json.dump(movies_collection, read_file)
        print("加载入文件完成...")
    read_file.close()


if __name__ == '__main__':
    main()
