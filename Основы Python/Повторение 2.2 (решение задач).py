#Роскомнадзор запретил букву а 🚫🌶️🌶️

alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a = input()+" запретил букву"

for i in range(len(alf)):
    if alf[i] in a:
        print(a + " " +alf[i])
        a = a.replace(alf[i],"")
    a = a.replace("  "," ")
    a = a.strip()



#Кремниевая долина 🤖🌶️

alf = "anton"
a = "ssssaaaaatnoooontondhfg"
j = 0
k=0
for i in range(len(alf)):
    while j < len(a):
        if alf[i] == a[j]:
            j+=1
            k+=1
            break
        else:
            j+=1
if k == 5:
    print("YES")
else:
    print("NO")


#Орел и решка

a = "ОРРОРОРООРРРО"
k = 0
maxi = -1
for i in range(len(a)):
    if a[i] == "Р":
        k+=1
    else:
        k=0
    if k > maxi:
        maxi=k

            
