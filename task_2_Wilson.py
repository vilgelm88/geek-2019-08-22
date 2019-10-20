#Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import math
import timeit
import time
import cProfile

#Способ 2 - Теорема Вильсона

start = time.time()

n = int(input('Введите число, до которого нужно найти простые числа: '))
ind = int(input('Введите индекс простого числа: '))

def wilson(n):
    lst = []

    for i in range(2, n + 1):
        if (math.factorial(i-1)+1) % i != 0:
            i += 1
        else:
            lst.append(i)
            i += 1
    return lst

lst = wilson(n)

if ind < len(lst):
    print(f'{ind}-е по счёту простое число: ', lst[ind - 1])
    print(f'\nПростые числа до: {n}\n', lst)
else:
    print(f'Вне диапазона')

delta = time.time() - start
print('\nВремени затрачено на выполнение задачи: ', delta)

#Результат по Эратосфену
#13-е по счёту простое число:  41
#Простые числа до: 100
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Вычисления времени:
#3.682363748550415
#4.006144046783447
#3.4558818340301514

#По времени вычисления решето меньше, тут нет факториалов
#Количество обращений тоже меньше, это видно из профилированиВЯ

cProfile.run('wilson(n)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_2_Wilson.py:17(wilson)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       99    0.000    0.000    0.000    0.000 {built-in method math.factorial}
#       25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


