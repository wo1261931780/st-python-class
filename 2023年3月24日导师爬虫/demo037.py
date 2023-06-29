import requests
from bs4 import BeautifulSoup

url = 'https://ma.sjtu.edu.cn/szdw/jsml.htm'
response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, 'html.parser')
teachers = soup.select('.teacher-list li')

print(teachers)

<<<<<<< Updated upstream:2023年3月24日导师爬虫/demo037.py
with open('demo20230324.txt', 'w', encoding='utf-8') as f:
	for teacher in teachers:
		name = teacher.select_one('h3').text.strip()
		title = teacher.select_one('.teacher-title').text.strip()
		research = teacher.select_one('.teacher-research').text.strip()
		f.write(f'{name}\t{title}\t{research}\n')
=======
with open('demo.txt', 'w', encoding='utf-8') as f:
    for teacher in teachers:
        name = teacher.select_one('h3').text.strip()
        title = teacher.select_one('.teacher-title').text.strip()
        research = teacher.select_one('.teacher-research').text.strip()
        f.write(f'{name}\t{title}\t{research}\n')
>>>>>>> Stashed changes:2023年3月24日导师爬虫/demo.py
