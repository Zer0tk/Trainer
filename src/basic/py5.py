from random import randint


hidden_number: int = randint(1, 20)
attempts: int = 5

print(f'Я загадал число от 1 до 20. У тебя {attempts} попыток!')
while attempts > 0:
    input_number = int(input(f'Попытка {5 - attempts + 1}. Введите число: '))

    if input_number > hidden_number:
        print('Слишком много!', end=' ')
    elif input_number < hidden_number:
        print('Слишком мало!', end=' ')
    else:
        print('Ты угадал! Отличная работа.')
        break

    attempts -= 1
    if attempts == 0:
        print('\nПоражение! Вам не удалось угадать число.\n')
        break
    
    print(f'Осталось попыток: {attempts}\n')

