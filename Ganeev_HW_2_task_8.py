"""8. Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры."""


user_range = input('Введите последовательность чисел: ')
user_number = input('Введите цифру которую необходимо посчитать: ')

count = 0
for i in user_range:
    if i == user_number:
        count += 1

print(f'Цифра {user_number} встречается в последовательности чисел: {user_range} - {count} раз')
