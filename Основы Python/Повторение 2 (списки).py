#срезы работают также как в строках
a = [1,5,3,5,4]
print(a[1])#
print(a[-3])#
print(a[1:4])#
print(a[1:4:2])#
print(a[::-1])#


#вывод 1
a = [5,3,5,4,3]
print(*a)
#вывод 2
for i in range(len(a)):
    print(a[i])
#вывод 3
for el in a:
    print(el)


#сложение и умножение списков
a = [1,2,3]
print(a*3)
print(a+[1,2])


#удаление элементов
del a[2]
a.remove(5)#удаление по значению
a.pop(2)#удаление по индексу


#пользователь вводит число n, затем n чисел, нужно сделать список из чисел
n = int(input())
a=[]
for i in range(n):
    el = int(input())
    a.append(el)
print(a)

#пользователь вводит числа в одну строку через пробел
#6 34 2 5
a = input().split()
a = int(a)
for i in range(len(a)):
    a[i] = int(a[i])


#тоже самое коротко
a = [int(x) for x in input().split()]




#увеличить все чётные числа на 1
from random import *

a = [randint(1,10) for i in range(5)]
print(*a)
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i]+=1
print(*a)








