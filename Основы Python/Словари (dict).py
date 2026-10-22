
dict1 = {}#пустой словарь
dict2 = dict()#пустой словарь

users = {"admin": 0, "user":10} #создание словаря из двух элементов
print(users["admin"]) #вывод элемента по ключу

print(len(users))#2

for i in range(len(users)):
    print(users[i])

info = dict(name='Timur', age=28, job='Teacher')#создание словаря из 3 элементов
print(info)

info = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
print(dict(info))  # создаем словарь на основе списка кортежей

info = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
print(dict(info))  # создаем словарь на основе кортежа списков


#Создание словаря на основе двух списков (кортежей) 
keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']
info = dict(zip(keys, values))
print(info)


#перебираем значения
for user in users:
    print(user, users[user])

#перебираем значения с номером
for i, user in enumerate(users, 1):
    print(i, user, users[user])

#изменение или добавление(в зависимости от наличия)
users["petya"]=0
print(users)
#удаление по ключу
users.pop("petya")
print(users)

#получить ключи
print(list(users.keys()))
#получить значения
print(list(users.values()))
#очистить словарь
users.clear()
print(users)

#Метод get() возвращает значение для ключа key
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(x.get('two', 0))# 2
print(x.get('ten', 0))# 0
print(x.get('six'))# None

