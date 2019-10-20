#Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import time
import cProfile

#Способ 1 - Решето Эратосфена

start = time.time()

n = int(input('Введите число, до которого нужно найти простые числа: '))
ind = int(input('Введите индекс простого числа: '))

def erathosphen(n):
    lst = []
    for i in range(n + 1):
        lst.append(i)

    lst[1] = 0
    for i in lst:
        if i > 1:
            for j in range (i + i, n + 1, i):
                lst[j] = 0
    return lst

lst = erathosphen(n)

lst = [number for number in lst if number != 0] # убираем нули

if ind < len(lst):
    print(f'{ind}-е по счёту простое число: ', lst[ind - 1])
    print(f'\nПростые числа до: {n}\n', lst)
else:
    print(f'Вне диапазона')

delta = time.time() - start
print('\nВремени затрачено на выполнение задачи: ', delta)

#13-е по счёту простое число:  41
#Простые числа до: 100
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Вычисления времени:
#3.1989758014678955
#3.5337159633636475
#3.2095890045166016

cProfile.run('erathosphen(n)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_2_Erst.py:16(erathosphen)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      101    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
