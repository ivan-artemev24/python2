#Списочные выражения
#создание списка от 0 до 4
a = [i*i for i in range(5)]
print(a)

#создания списка случайных чисел
from random import *

a = [randint(1,10) for i in range(5)]
print(a)
#создания списка квадратов от 1 до 5
a = [x*x for x in range(1,6)]
print(a)


#создание списка квадратов из другого списка
a = [2,5,3,4,7]
b = [a[i]*a[i] for i in range(len(a))]
#b = [el for el in a]
print(b)

#условие создание списка чётных чисел
a = [x for x in range(21) if x % 2 == 0]
print(a)


#преобразовать все элементы списка к типу int
a = ['1','2','3']
a = [int(a[i]) for i in range(len(a))]
print(a)


#ввод пользователя
n = int(input())
a = [int(input()) for i in range(n)]
print(a)


#вложенные циклы (таблица умножения)
text = [f"{i}х{j}={i*j}" for i in range(1, 11) for j in range(1,11) ]
print(*text, sep="\n")









