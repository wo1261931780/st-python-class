import json
from json import loads
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


class Movie:
    # 电影类
    def __init__(self, title, genre, director, studio, year):
        self.title = title
        self.genre = genre
        self.director = director
        self.studio = studio
        self.year = year

    # 用来打印类属性的方法
    def print_movie(self):
        print("《{", self.title, "}》,genre : ", self.genre, ",director : ", self.director, ",studio : ",
              self.studio, ",year : ", self.year, "。")


def main():
    movies = []
    with open("Movies.txt", encoding="utf-8") as dict2json:
        for line in dict2json:
            # print(line)
            # Title:Oldboy;Genre:Mystery;Director:Spike Lee,Joe Russo;Studio:Marvel Comics;Year:2013
            title, genre, director, studio, year = line.split(";")  # 读取每一行的数据
            movie_information = dict()  # 新建一个字典，然后将每一行的数据作为键值存进去
            movie_information["year"] = year.split("Year:")[1]
            movie_information["title"] = title.split("Title:")[1]
            movie_information["genre"] = genre.split("Genre:")[1]
            movie_information["studio"] = studio.split("Studio:")[1]
            # movie_information["director"] = director.split("Director:")[1] # 需要考虑多导演的问题
            director_origin = director.split("Director:")[1]
            directors = []
            # 判断是否有多个导演
            if "," in director_origin:
                names = str(director_origin).split(",")
                for i in names:
                    single_director = dict(Name=i)  # 对每个导演使用Name包装一次
                    directors.append(single_director)
            else:
                single_director = dict(Name=director_origin)
                directors.append(single_director)

            movie_information["director"] = directors
            movies.append(movie_information)  # 将得到的字典插入上面的数组中

    print(movies)  # 先打印一次默认顺序的电影片单
    movies.sort(key=lambda movie: movie["title"])  # 对字典中的数据进行排序
    print(movies)  # 打印排序好的json

    # --------------------------------------------------------------------------------
    movie_list_aspect = []  # 将每个电影整合到一个列表中

    for i in movies:
        movie_inspect = dict(Movie=i)  # 用Movie包装一次
        movie_list_aspect.append(movie_inspect)
    movies_collection = dict(Movies=movie_list_aspect)  # 再包装一次
    print(movies_collection)  # 打印结果
    # --------------------------------------------------------------------------------
    with open(
            "Movies.json",
            "w") as dict2json:
        json.dump(movies_collection, dict2json)
    print("将字典传输到文件...")
    dict2json.close()
    # --------------------------------------------------------------------------------


def json2xml(json_p, xml_p):
    # 打开路径
    with open(json_p, 'r', encoding='UTF-8') as open_file:
        load_dict = loads(open_file.read())
    # 设置临时标签
    movie_item = lambda x: 'temporary'
    # 将其作为一个需要写入的xml
    xml = dicttoxml(load_dict, custom_root='Movies', item_func=movie_item, attr_type=False)
    # 打开写入的内容
    with open(xml_p, 'w', encoding='UTF-8') as write_file:
        write_file.write(parseString(xml).toprettyxml())
    print("将xml传输到文件...")


if __name__ == '__main__':
    # 执行代码
    main()
    # 如果在本地运行，需要修改对应的路径，否则可能报错
    json = "Movies.json"
    xml = "Movies.xml"
    json2xml(json, xml)
