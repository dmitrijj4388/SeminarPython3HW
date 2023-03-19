# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

import random

def InputDigits():
    
    while True:
        a = input()
        if a.isdigit() == False:
            print('Вы ввели не число')
        else: 
           break
    return int(a)

print('Введите количество элементов: ')
n = InputDigits()
print('Введите искомое число: ')
x = InputDigits()

array = [random.randint(1, n/2) for i in range(n)]
print(array)
count = 0
for i in array:
    if i == x:
        count +=1
print(f'Искомое число встпечается {count} раз')

  


