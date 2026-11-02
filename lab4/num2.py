names = ["Анна", "Петр", "Иван", "Ольга"]
grades = [5, 4, 3, 5]

print("Цикл for")
for name, grade in zip(names, grades):
    print(f"{name}: {grade}")
print("Список строк")
result_strings = [f"{name}: {grade}" for name, grade in zip(names, grades)]
print(result_strings)