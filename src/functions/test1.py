from task1 import calculate_rental_batch


print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

batches = {
    1: ["Academy Dinosaur", 30, 2.99],
    2: ["Affair Prejudice", 40, 4.99, 0.1],
    3: ["Agent Truman", 10, 1.99],
    4: ["African Egg", 50, 3.50, 0.2]
}

for number, batch in batches.items():
    batch_results = calculate_rental_batch(*batch[1:])
    print(f"Партия {number} ({batch[0]}): Сумма {batch_results[0]}$. Превышение лимита: {batch_results[1]}")
