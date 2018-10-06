import datetime
from random import randint


def another_file(path_another_file):
    new_file = open(path_another_file)
    lis = []
    for line in new_file:
        lis.append(line)
    new_file.close()
    return lis


my_file = open("Files/File1.txt")
lis = []
for line in my_file:
    lis.append(line)
my_file.close()

d1 = 0
d2 = lis.__len__() - 1
silent = False
while True:
    s = input()
    if s == "silent":
        silent = True
    elif s == "change":
        path_another_file = input("Введите путь нового файла: ")
        lis = another_file(path_another_file)
        d2 = lis.__len__() - 1
    elif s == "get up" and silent == False:
        pass
    elif s == "get up" and silent == True:
        silent = False
    elif s == "date":
        print(datetime.date.today())
    elif s == "time":
        print(datetime.datetime.now().strftime('%H:%M:%S'))
    elif s == "quit":
        print("Покасики!")
        break
    elif s != "silent" and silent == True:
        pass
    else:
        print(lis[randint(d1, d2)])




