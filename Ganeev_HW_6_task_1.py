"""1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС."""

'''
x64 Windows 10
Python 3.10.1
'''

import sys
import random

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])

list_min = []
list_min.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < list_min[i]:
            list_min[i] = j
        i += 1

print()
print('list_min')
print(('{:4d} ' * len(list_min)).format(*list_min))
print()

list_min.sort(reverse=True)
print(
    'Максимальный элемент среди минимальных элементов столбцов матрицы равен: ',
    list_min[0]
)

sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(list_min)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size)
