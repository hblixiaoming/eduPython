listFruit = ['apple', 'orange', 'banana']

print('--------------------------')

print(listFruit)

print('--------------------------')

# 求列表的长度
print(len(listFruit))

print('--------------------------')

# 通过下标输出列表数据
print(listFruit[0])

print(listFruit[1])

print(listFruit[2])

print('--------------------------')

# 输出最后一个元素
print(listFruit[-1])

print('--------------------------')

# 遍历整个列表
for a in listFruit:
    print(a)

print("--------------------------")

# 添加一个元素
listFruit.append("grape")

print(listFruit)

# 在指定位置插入元素
listFruit.insert(1, "pear")

print(listFruit)

# 删除末尾的元素
listFruit.pop()

print(listFruit)

# 删除指定位置的元素
listFruit.pop(0)

print(listFruit)

# 元素的替换

listFruit[0] = 'water'

print(listFruit)

listColor = ['red', 'black', ['green', 'yellow'], 'blue']

print(listColor[2][0])

tupleSeasons = ('SPRING', 'SUMMER', 'AUTOMN', 'WINTER')

print("--------------------------")

listDict = {"lucy": 1, "jack": 2}
print(listDict["lucy"])

if "jack" in listDict:
    print("jack in listDict")

if listDict.get("lucy") != None:
    print("lucy in listDict")

listDict.pop("lucy")

print(listDict)
