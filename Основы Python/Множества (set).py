#В множестве нет копий! 
#Встроенные функции len(), sum(), min(), max()
#Оператор принадлежности in
#создание пустого можества
a = {} #не сработает! будет словарь
a = set() #пустое множество
#создание
fruits = {"banana", "apple", "orange"}
color_list = ["red", "green", "green", "blue", "purple", "purple"]
print(set(color_list))#множество из списка
print(set("hello"))#множество из строки
print(set((9,23543,3,5345,8,36456456,7)))#множество из кортежа

#print(fruits[0])#ошибка

#Перебор множеств
color_list = {"red", "green", "green", "blue", "purple", "purple"}
for x in color_list:
    print(x)

#методы множеств
a = {2,3}
a.add(4)#добавление в множество
#a.remove(1)#удаление по значению
a.discard(1)#безопасное удаление по значению
a.pop()#удалить случайный элемент
a.clear()#очистить множество
print(a)


#получить уникальные буквы строки
a = {5,8,7,6,1,3,4,2,201000}
#вариант 1
a = list(a)
a.sort()
print(a)
#вариант 2
print(*sorted(a))

#ввод множества
#1 2 3 2 1
a = input().split()
b = set(a)
print(b)

a = {1,2,3}
b = {3,4,5,6}
#пересечение
#and
print(a&b)
#объединение
#or
print(a|b)




