students = [
    {"name": "Анна", "score": 22, "attempts": 1},
    {"name": "asd", "score": 74, "attempts": 3},
    {"name": "qwr", "score": 90, "attempts": 4},
]

passed = []
for student in students:
    if student["score"] >= 60 and student["attempts"] <= 3:
        passed.append(student["name"])

passed_comp = [
    student["name"]
    for student in students
    if student["score"] >= 60 and student["attempts"] <= 3
]

print("Обычный цикл", passed)
print("List comprehension", passed_comp)
print("Результаты совпадают", passed == passed_comp)