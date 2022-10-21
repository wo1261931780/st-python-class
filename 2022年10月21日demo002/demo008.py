str1 = "123456 demo run"
# 不能直接用str来表示，因为str是字符串的意思
print("我是str1[0]字符：" + str1[0])
print("我是str1[1]字符：" + str1[1])
print("我是str1[3:6]字符：" + str1[3:6])  # 456,结果不包括第三个字符
str2 = "01020304050607"
print("我是str2[3:6]字符：" + str2[3:6])  # 203，类似上面
# print(true and "A" not in str2)
str3 = "01020304050607--"
print(str3 * 3)  # 可以直接设置需要重复的次数
