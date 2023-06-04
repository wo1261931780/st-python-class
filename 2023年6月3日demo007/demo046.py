import json

# Python 字典类型转换为 JSON 对象
data1 = [
  {
    "Category": "Kiddie Rides\r",
    "avg(t2.num)": 3841.909090909091,
    "max(t2.num)": 4062,
    "min(t2.num)": 3597
  },
  {
    "Category": "Rides for Everyone\r",
    "avg(t2.num)": 6998.25,
    "max(t2.num)": 25074,
    "min(t2.num)": 4935
  },
  {
    "Category": "Thrill Rides\r",
    "avg(t2.num)": 18306.555555555555,
    "max(t2.num)": 27747,
    "min(t2.num)": 14415
  }
]

json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("JSON 转换过来的字典：", data2)
