from task3 import calculate_overdue_fine


data = [
    ['Matrix', 5, 1.5],
    ['Inception', 'пять', 2.0],
    ['Avatar', 0, 2.5],
    ['Interstellar', [3, ], 3.0]
]


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
for film in data:
    results = calculate_overdue_fine(*film)
    if results:
        print(f"Фильм: '{film[0]}' | Итоговый штраф: {results[0]}$ | Индекс: {results[1]}")
    print()
