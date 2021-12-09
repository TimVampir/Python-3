"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def sum_numbers(number):
    """Функция для суммирования цифр числа"""
    total = 0
    for f in number:
        total += int(f)
    return total


list_number = [i for i in input('Введите числа через пробел: ').split()]
max_number = 0
max_sum = 0
for i in list_number:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'Число {max_number} имеет наибольшую сумму цифр - {max_sum}')
