"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число."""


def equality_first(n):
    """Функция для формирования 1+2+...+n, где n - любое натуральное число."""
    if n == 1:
        return n
    elif n > 0:
        return n + equality_first(n-1)


def equality_second(n):
    """Функция для формирования n(n+1)/2, где n - любое натуральное число."""
    return n * (n + 1) // 2


n = 1
while n < 500:      # while True:   # для проверки без ограничений
    if equality_first(n) == equality_second(n):
        print(f'Для n = {n} - True')
    else:
        print(f'Для n = {n} - False')
        break
    n += 1
