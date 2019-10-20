#Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
import random

import time
import timeit
import cPro

start = time.time()


SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Сгенерированный массив случайных натуральных чисел:', array)

# Ищем максимум и минимум массива с помощью встроенных функций

min_num = min(array)
max_num = max(array)
imax = array.index(max_num)
imin = array.index(min_num)

s = '''
min_num = min(array)
max_num = max(array)
imax = array.index(max_num)
imin = array.index(min_num)
'''

print(f'\nМаксимум массива {max_num}, Индекс в массиве: {imax}')
print(f'Максимум массива {min_num}, Индекс в массиве: {imin}')

array[imax], array[imin] = array[imin], array[imax]

print('\nПолученный массив с замененными максимумом и минимумом:', array)

delta = time.time() - start
print(delta)

# 0.00016689300537109375
# 0.0002770423889160156
# 0.00013971328735351562
# 0.00013113021850585938
# 0.0004181861877441406
# 0.0002009868621826172
# 0.00011920928955078125
# 0.0001850128173828125
# 0.000164031982421875
# 0.0001659393310546875

cProfile.run('s')

# три обращения
