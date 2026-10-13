s = []
n = 3
for i in range(n):
    s.append([0]*n)
print(s)
s[0][0]=1
print(s)

for i in range(n):
    for j in range(n):
        print(s[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        if i==j:
            s[i][j]=1
            
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            s[i][j]=5


for i in range(n):
    for j in range(n):
        print(s[i][j], end=' ')
    print()
'''

#Задание 4.3
#ввод
n = int(input())
s=[]#матрица
for i in range(n):
    a=[int(el) for el in input().split()]
    s.append(a)
print(s)
    
#главная диагональ
for i in range(len(s)):
    for j in range(len(s[i])):
        if i == j:
            print(s[i][j])
        

#Задание 4.4
n = int(input())
s=[]#матрица
for i in range(n):
    a=[int(el) for el in input().split()]
    s.append(a)

k=0    
for i in range(len(s)):
    summa=0
    for j in range(len(s[i])):
        summa+=s[i][j]
    sr = summa/len(s[i])
    for j in range(len(s[i])):
        #дописать









