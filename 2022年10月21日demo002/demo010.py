testWord = "demo"
testWord = int(input("请输入字符串："))  # 如果在这里输入0.01之类的浮点型数据，会出现类型转换异常
print(testWord)  # 结果为0
print(type(testWord))  # <class 'int'>
# ==========================================================

testNum = 12.01
print(type(testNum))
testNum = int(testNum)  # <class 'float'>
print(type(testNum))  # <class 'int'>
