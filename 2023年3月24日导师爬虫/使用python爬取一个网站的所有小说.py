""""""
"""
很多免费的资源只能看但是不提供下载，今天我们以小说为例
教你如何把互联网上只能看不能下载的东西给下载下来


课题：使用 python 爬取一个网站的所有小说
课程时间：20:00-22:00
讲师：正心老师

知识点：
    1. requests
    2. css选择器
    3. 全站小说爬取思路

开发环境：
    1. 版  本：anaconda5.2.0(python3.6.5)
    2. 编辑器：pycharm 社区版
"""
# 工具
import requests
import parsel

headers = {
    'User-Agent': 'gao fu shui'
}


# 定义函数，调用
def download_one_chapter(chapter_url, book_name):
    """1. 请求数据"""
    # 服务器返回的内容（对象）
    response = requests.get(chapter_url, headers=headers)
    # 设置文本的编码为 utf-8
    # response.encoding = 'utf-8'
    # 万能解码 99%的情况下都是对的
    # print(response.apparent_encoding)  # requests 自动识别的编码
    # print(response.encoding)  # 服务直接我们的编码
    response.encoding = response.apparent_encoding
    # print(response)
    html = response.text
    # print(html)
    # print(response.headers)
    # # 响应体.请求体.请求头信息
    # print(response.request.headers)
    # # 查看源码 ctrl + 鼠标左键
    # print(response.cookies)

    """3. 解析数据"""
    # css xpath
    # parsel = css + xpath + re
    # 把字符串变成可以解析的对象
    selector = parsel.Selector(html)

    # selector.css()
    # selector.xpath()
    # selector.re()
    # get 获取对象里面的文字内容
    # 属性提取器 attr
    h1 = selector.css('.reader h1::text').get()
    # print(h1)
    content = selector.css('.showtxt::text').getall()
    # print(content)
    # # xpath 路径提取器
    # h1 = selector.xpath('//h1/text()').get()
    # print(h1)
    # content = selector.xpath('//*[@class="showtxt"]//text()').getall()
    # print(content)
    # 去除每一个空白字符
    # 定义一个空列表，留待备用 {}
    lines = []

    for c in content:
        lines.append(c.strip())

    print(h1)
    # print(lines)

    # str join 字符串的合并方法
    text = '\n'.join(lines)
    # print(text)

    """3. 保存数据"""
    # mode 模式 w write 写入 a append 追加写入
    # h1 每一次都在变 所以会写成多个文件
    file = open(book_name + '.txt', mode='a', encoding='utf-8')
    file.write(h1)
    file.write('\n')
    file.write(text)
    file.write('\n')
    file.close()


# download_one_chapter('http://www.shuquge.com/txt/8659/2324752.html')
# download_one_chapter('http://www.shuquge.com/txt/8659/2324753.html')
# download_one_chapter('http://www.shuquge.com/txt/8659/2324754.html')
"""获取所有章节的下载地址"""


def download_one_book(index_url):
    index_response = requests.get(index_url, headers=headers)
    index_response.encoding = index_response.apparent_encoding
    sel = parsel.Selector(index_response.text)
    book_name = sel.css('h2::text').get()
    # 提取了所有章节的下载地址
    urls = sel.css('.listmain dl dd a::attr(href)').getall()
    # 不要最新的 12 章放在最前main
    for url in urls[12:]:
        chapter_url = index_url[:-10] + url
        print(chapter_url)
        download_one_chapter(chapter_url, book_name)


# download_one_book('http://www.shuquge.com/txt/8659/index.html')
# download_one_book('http://www.shuquge.com/txt/5809/index.html')
# download_one_book('http://www.shuquge.com/txt/63542/index.html')
"""下载玄幻类的第一页"""
# 2_1.html 控制类别页数 可以for in 生产类别 for in 生产 页数
for cate in ['1', '2', '4']:
    for page in range(1, 101):
        cate_url = 'http://www.shuquge.com/category/' + cate + '_' + str(page) + '.html'
        cate_response = requests.get(cate_url, headers=headers)
        cate_response.encoding = cate_response.apparent_encoding
        sel = parsel.Selector(cate_response.text)
        # 提取了所有章节的下载地址
        urls = sel.css('.l.bd > ul > li > span.s2 > a::attr(href)').getall()
        # 不要最新的 12 章放在最前main
        for url in urls:
            print(url)
            download_one_book(url)

"""

python 爬虫
python 全栈
python 数据分析
python 人工智能
.....

全套 6400 优惠价 5180
基础 + 进阶 + 爬虫 + 数据分析 代码量，会有大量的案例，作业

花钱学习 学习不是消费
学的是一门技术：
    找工作、当做副业、

投资失败
    
    
耐心
细心
恒心
    
花一年时间学习基础 
    时间、精力

公开课学了多久
3 6 9 12 24

循序渐进的学 学习是有加速的

自己没有系统学
只听课，很少敲代码

一定要坚持下来
"""