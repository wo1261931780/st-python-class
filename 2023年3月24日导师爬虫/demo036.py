import requests
from bs4 import BeautifulSoup

url = 'https://ma.sjtu.edu.cn/szdw/jsml.htm'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

professors = []

for professor in soup.find_all('div', class_='teacher-info'):
    name = professor.find('h3').text.strip()
    title = professor.find('span').text.strip()
    research_area = professor.find('p', class_='teacher-info-desc').text.strip()
    professors.append({'name': name, 'title': title, 'research_area': research_area})

print(professors)

# 我需要一个完整的爬虫程序，请使用Python编写代码。然后将获得的数据保存到demo.txt文件中。爬虫地址为：https://ma.sjtu.edu.cn/szdw/jsml.htm
