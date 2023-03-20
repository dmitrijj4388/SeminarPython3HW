# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

def InputDigits():
    
    while True:
        a = input()
        if a.isdigit() == False:
            print('Введите корректное число')
        
        else: 
           break
    return int(a)

print('Введите количество элементов: ')
n = InputDigits()
print('Введите число которое необходимо проверить: ')
x = InputDigits()

array = [random.randint(1, n) for i in range(n)]
print(array)
unicArray = set(array)
array1 = list(unicArray)
print(array1)
if x in array1:
    for i in range(len(array1)):
        if array1[i] == x:
            xPosition = i
            break
    if xPosition == 0:
        print(f'Ближайший элемент в массиве к числу {x} число - {array1[xPosition+1]}')
    else:
        if (array1[i] - array1[i-1]) > (array1[i+1] - array1[i]):
            print(f'Ближайший элемент в массиве к числу {x} число - {array1[xPosition+1]}')
        else:
             print(f'Ближайший элемент в массиве к числу {x} число - {array1[xPosition-1]}')
        
elif x <= 0:
            print('Вы ввели не натуральное число')
elif x > max(array1):
     print(f'Ближайший элемент в массиве к числу {x} число - {array1[-1]}')            
else:
    for i in range(len(array1)):
        if array1[i] > x:
            xPosition = i
            break
    if (x - array1[xPosition-1]) > (array1[xPosition] - x):
                print(f'Ближайший элемент в массиве к числу {x} число - {array1[xPosition]}')
    else:
                print(f'Ближайший элемент в массиве к числу {x} число - {array1[xPosition-1]}')
