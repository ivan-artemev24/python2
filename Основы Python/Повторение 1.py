'''
#ввод вывод
a=int(input())#int - целые числа, float - 6.346, str - текст, bool True False


#форматирование строки
print(f"Ваша сдача: {a} рублей, {40} копеек")
print(f"{a:b}")
print(f"{10432135:,}")


#математические операции, корень
c=a%5#остаток  17%5=2 17%10=7
c=a//5#целочисленное деление 17//5=3
c=a**2#возведение в степень
c=a**(0.5)#извлечение корня

#условия
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)


#умножение строки
print("*"*5)#*****

#строки, срезы
s = "Мама мыла раму"
print(s[0])#М
print(s[-1])#у
print(s[0:4])#Мама
print(s[-4:])#раму
print(s[:])#Мама мыла раму
print(s[::-1])#переворот
print(s[::2])#переворот

#функция len
s = "sgdhfhdfg"
s2 = [1,3,6,9]
print(len(s), len(s2))

'''

#фиксированно число повторений
for i in range(5):
    print("Привет")


#параметры цикла
for i in range(5): #от 0 до 4 с шагом 1
    print(i)

for i in range(5,11): #от 5 до 10 с шагом 1
    print(i)

for i in range(2,11,2): #от 2 до 10 с шагом 2
    print(i)   

for i in range(10,1,-2): #от 10 до 2 с шагом 2
    print(i)

    
for i in range(5,0,-1):
    print(i)


