# Способ 1

time_list = [0.00035309791564941406, 0.0001800060272216797, 0.00037598609924316406, 0.00012993812561035156, 0.00011396408081054688, 0.0001480579376220703, 0.00014591217041015625, 0.00012111663818359375, 0.0003409385681152344, 0.0001251697540283203]
avg_time_1 = sum(time_list) / len(time_list)

print('Способ 1 (цикл и вспомогательная переменная: ', avg_time_1)

# Способ 2

time_list = [0.00016689300537109375, 0.0002770423889160156, 0.00013971328735351562, 0.00013113021850585938, 0.0004181861877441406, 0.0002009868621826172, 0.00011920928955078125, 0.0001850128173828125, 0.000164031982421875, 0.0001659393310546875]
avg_time_2 = sum(time_list) / len(time_list)

print('Способ 2 - всроенные функции min и max: ', avg_time_2)

# Способ 3

time_list = [0.00014829635620117188, 0.00010180473327636719, 0.00015425682067871094, 0.0003008842468261719, 0.0001373291015625, 0.000225067138671875, 0.00010013580322265625, 0.00036406517028808594, 0.00011396408081054688, 0.0020339488983154297]
avg_time_3 = sum(time_list) / len(time_list)

print('Способ 3 - Цикл и уход от вспомогательных переменных: ', avg_time_3)

if avg_time_1 < avg_time_2 and avg_time_1 < avg_time_3:
    print('Выполнение алгоритма 1 занимает меньше всего времени')
elif avg_time_2 < avg_time_1 and avg_time_2 < avg_time_3:
    print('Выполнение алгоритма 2 занимает меньше всего времени')
elif avg_time_3 < avg_time_1 and avg_time_3 < avg_time_2:
    print('Выполнение алгоритма 3 занимает меньше всего времени')

# В по времени выполнения 2 способ со встроенными функциями занимает меньше времени
# Я полагаю, что при большей выборке результаты могут меняться, с 3-мя был 3-й
# В нем нет доп. переменных и количество прогонов массива меньше чем у встроенных функций


