try:#попробовать
    a = int(input())
    b = a/0
except ValueError:#ошибка 1
    print('Вы ввели не число.')
except ZeroDivisionError:#ошибка 2
    print('Деление на 0.')
except Exception as e:#Другие ошибки
    print(f'Возникла ошибка: {e}')
else:#если ошибки не было
    print('Всё хорошо.')
finally:#сделать в конце
    print('Конец.')
