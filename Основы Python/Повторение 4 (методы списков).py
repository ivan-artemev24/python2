#срезы работают также как в строках
a = [1,5,3,5,4]
print(a[1])#5
print(a[-2])#5
print(a[1:4])#5 3 5 
print(a[1:4:2])#5 5
print(a[::-1])#4 5 3 5 1

#перебор элементов
for i in range(len(a)):
    print(a[i])#


#методы списков
a = [1,2,3]
a.append(21)# добавляем число 21 в конец списка
a.remove(1)#удаление по значению
a.pop(2)#удаление по индексу
a.extend([4,5])#расширения списка элементами другого списка 
a.extend('мама')#или строки
print(a)


#split
s = '5 34 23 1 33'
a = s.split()
print(a)
s = "8-908-015-65-16"
a = s.split("-")
print(a)

#join
a = ["Мама","мыла","раму"]
s = " ".join(a)
print(s)

a = "Привет"
s = "*".join(a)
print(s)

a = [1,2,5,2]
#Метод insert() - вставить элемент по индексу
a.insert(2,3)
print(a)

#Метод index() - найти индекс элемента
if 4 in a:
    print(a.index(4))
else:
    print("нет таких")

#Метод reverse() - перевернуть список
a.reverse()
print(a)
#Метод count() - количество элементов с таким значением
print(a.count(3))
#Метод sort() - сортировка по возрастанию
a.sort()
print(a)
#Метод sort() - сортировка по убыванию
a.sort(reverse=True)
print(a)
#Метод copy() - создать копию списка
b = a.copy()
print(b)
#Метод clear() - очистить список
a.clear()
print(a)

#вложенные списки
a = [1,2,3,[5,4]]
print(a[3][0])

a = [[1,2,3],[3,4,5],[6,7,8,9]]
#двойной цикл
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()















    






