"""7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться."""


import random

r = [random.randint(0, 99) for i in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for n in r:
    if r[min_index_1] > n:
        min_index_2 = min_index_1
        min_index_1 = r.index(n)
    elif r[min_index_2] > n:
        min_index_2 = r.index(n)

print(f'Два минимальных значения: {r[min_index_1]} и {r[min_index_2]}')
