import matplotlib.pyplot as plt


# 这是画图的成功案例
# 用来画饼图的

topic = ['VirginAmerica', 'UnitedAirline', 'SouthWestAirline', 'USAirline', 'AmericanAirline', 'SpiritAirline',
         'DeltaAirline']
Postive_percentage = [3.917525773195876, 10.0, 6.666666666666667, 10.0, 3.0, 5.0, 5.0]

sizes = Postive_percentage
print(sizes)
labels = list(topic)
# makeitastring = ''.join(map(str, labels))
print(labels)
colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
plt.pie(sizes, explode=None, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)  # line 240
# plt.pie(sizes, labels, colors)
plt.axis('equal')
plt.legend()
plt.show()
