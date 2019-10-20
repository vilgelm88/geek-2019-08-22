# Оригинальный написанный код

import random

import time
import timeit
import cProfile

start = time.time()


SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_number = array[0] #Изначально задаем максимум первым элементом массива
min_number = array[0] #Изначально задаем минимум первым элементом массива
imax = 0 #По умолчанию ставим индекс максимального элемента массива первым
imin = 0

print('Сгенерированный массив случайных натуральных чисел:', array)

#Перебираем массив (со 2-го элемента (1-й в python) до 10 го включительно (9-й в python)):

for i in range(1, SIZE):
    if array[i] >= max_number:
        max_number = array[i]
        imax = i
    elif array[i] <= min_number:
        min_number = array[i]
        imin = i

#print(f'\nМаксимум массива {max_number}, Индекс в массиве: {imax}')
#print(f'Максимум массива {min_number}, Индекс в массиве: {imin}')

help_var = array[imax]
array[imax] = array[imin]
array[imin] = help_var

s = '''
for i in range(1, SIZE):
    if array[i] >= max_number:
        max_number = array[i]
        imax = i
    elif array[i] <= min_number:
        min_number = array[i]
        imin = i

help_var = array[imax]
array[imax] = array[imin]
array[imin] = help_var
'''

print('\nПолученный массив с замененными экстремумами:', array)

delta = time.time() - start
print(delta)

# 0.00035309791564941406
# 0.0001800060272216797
# 0.00037598609924316406
# 0.00012993812561035156
# 0.00011396408081054688
# 0.0001480579376220703
# 0.00014591217041015625
# 0.00012111663818359375
# 0.0003409385681152344
# 0.0001251697540283203

cProfile.run('s')