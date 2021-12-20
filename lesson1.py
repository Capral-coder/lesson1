lists = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

#сортиовка списка по возростанию
for i in range(len(lists)):
    for x in range(len(lists)-1):
        if lists[x][1] > lists[x+1][1]:
            lists[x], lists[x+1] = lists[x+1], lists[x]
print(lists)
print(" ")

#создаем словарь
dist={}
for k in range(len(lists)):
    dist[lists[k][1]] = [lists[k][0],lists[k][2],lists[k][3]]
print(dist)
print(" ")

#сортируэм словарь
for key in dist:
    data=dist.get(key)
    for i in range(len(data)):
        for x in range(len(data)-1):
            if data[x] < data[x+1]:
                data[x], data[x+1] = data[x+1], data[x]
print(dist)
print(" ")

#получаем множество из всех значений
new=set()
for key in dist:
    data=dist.get(key)
    for number in range(len(data)):
        new.add(data[number])
print(new)
print(" ")

#преобразуем множество в строку
print(str(new).replace('{', '').replace('}', ''))