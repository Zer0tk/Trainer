first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

operator: str = ''
while operator not in ["+", "-", "*", "/"]:
    operator = input("Выберите оператор (+, -, *, /): ")

try:
    result: float = 0.0
    match operator:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case '/':
            if second_number == 0:
                raise ValueError('Деление на 0 неопределено\n')
            result = first_number / second_number

    print(f'Результат: {result}')

except ValueError as error:
    print(f'Ошибка: {error}')
