#Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# Третий вариант кода (оригинальный + уход от вспомогательных переменных help_var использовавшихся
# в первом варианте

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


s = '''
for i in range(1, SIZE):
    if array[i] >= max_number:
        max_number = array[i]
        imax = i
    elif array[i] <= min_number:
        min_number = array[i]
        imin = i
        
array[imax], array[imin] = array[imin], array[imax]
'''

#print(f'\nМаксимум массива {max_number}, Индекс в массиве: {imax}')
#print(f'Максимум массива {min_number}, Индекс в массиве: {imin}')

array[imax], array[imin] = array[imin], array[imax]

print('\nПолученный массив с замененными максимумом и минимумом:', array)

delta = time.time() - start
print(delta)

# 0.00014829635620117188
# 0.00010180473327636719
# 0.00015425682067871094
# 0.0003008842468261719
# 0.0001373291015625
# 0.000225067138671875
# 0.00010013580322265625
# 0.00036406517028808594
# 0.00011396408081054688
# 0.0020339488983154297

cProfile.run(s)

# 3 обращения