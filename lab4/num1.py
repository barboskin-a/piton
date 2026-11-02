grades = [5, 4, 3, 5, 2, 4]
print("Вариант 1")
counter = 1
for grade in grades:
    print(f"Номер: {counter}, Оценка: {grade}")
    counter += 1

print("Вариант 2")
for number, grade in enumerate(grades, start=1):
    print(f"Номер: {number}, Оценка: {grade}")