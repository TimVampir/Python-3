"""6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем
за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""


import random


rng = random.SystemRandom(0)
random_number = rng.randint(0, 100)

attempt = 1
while attempt <= 10:
    print(f'Попытка {attempt} из 10')
    user_try = int(input('Попробуйте угадать случайное число от 1 до 100: '))
    if user_try == random_number:
        print('Поздравляю, Вы угадали!')
        break
    elif user_try > random_number:
        print(f'Ваше число {user_try} больше загаданного')
    else:
        print(f'Ваше число {user_try} меньше загаданного')
    attempt += 1
if attempt > 10:
    print(f'Вы не угадали! Загаданное число {random_number}')
