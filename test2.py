import csv
import json

def f1(x):
    return x/(x+100)

def f2(x):
    return 1/x

def f3(x):
    return 20*(f1(x) + f2(x))/x

def mygenerator(start, stop):
    for i in range(start, stop):
        yield i

dictonary={}
for y in mygenerator(5, 91):
    dictonary[y] = [f1(y), f2(y), f3(y)]

with open('sin.csv', 'w', newline='') as my_file:
    fieldnames = ['x', 'f1', 'f2', 'f3']
    filetable = csv.DictWriter(my_file, fieldnames=fieldnames)
    filetable.writeheader()
    for y in mygenerator(5, 91):
        filetable.writerow({'x': y, 'f1': f1(y), 'f2': f2(y),'f3': f3(y)})

my_data = []

with open('sin.csv', 'r') as my_file:
    filetable=csv.reader(my_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in filetable:
        my_data.append(row)
        
print(my_data)

with open('my_data.json', 'w') as fp:
    json.dump(my_data, fp, indent=5)