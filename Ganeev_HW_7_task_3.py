"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках"""

import random

MIN_ITEM = 0
MAX_ITEM = 100
MIN_SIZE = 5
MAX_SIZE = 20


def mid_search(lst, left_part, right_part):
    lst = lst.copy()
    mid = len(lst) // 2

    if left_part >= right_part:
        return lst[mid]

    meaning = lst[mid]
    i = left_part
    j = right_part

    while i <= j:

        while lst[i] < meaning:
            i += 1

        while lst[j] > meaning:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if mid < i:
        lst[mid] = mid_search(lst, left_part, j)

    elif j < mid:
        lst[mid] = mid_search(lst, i, right_part)

    return lst[mid]


def merge_sort(arr):
    def merge(fst, snd):
        res = []
        i, j = 0, 0
        while i < len(fst) and j < len(snd):
            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1
            else:
                res.append(snd[j])
                j += 1
        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))
    return div_half(arr)


m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

print(f'Массив из 2 * {m} + 1 = {size} элементов:', array, sep='\n')
median = mid_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')
print(f'Отсортированный массив из {size} элементов: ', merge_sort(array), sep='\n')

if median == merge_sort(array)[len(array) // 2]:
    print('Решение верно')
else:
    print('Решение НЕ верно')
