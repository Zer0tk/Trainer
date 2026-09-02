from trainee import Trainee


trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)
print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")