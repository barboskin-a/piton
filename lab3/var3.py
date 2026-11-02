# Вариант 3. Запись в медицинскую клинику
appointment = ("16.10.2026", 312, "Смирнова")
registration = [2104, 2121, 2140, 2158, 2173, 2190]
visited = {2104, 2140, 2158, 2190}
patients = {
    2104: "Мария Волкова",
    2121: "Алексей Ким",
    2140: "Иван Иванов",
    2158: "Петр Петров",
    2173: "Кто-то Кто-то",
    2207: "НП"
}

print(f"Прием: {appointment[0]}, кабинет {appointment[1]}, врач {appointment[2]}")

registration_str = ", ".join(map(str, registration))
print(f"Запись пациентов: {registration_str}")

visited_str = ", ".join(map(str, sorted(visited)))
print(f"Пациенты, посетившие врача: {visited_str}")

patients_str = "; ".join(f"{card} - {name}" for card, name in patients.items() if card != 2207)
print(f"Пациенты: {patients_str}; ...")

new_patient_card = 2207
registration.append(new_patient_card)
new_registration_str = ", ".join(map(str, registration))
print(f"После добавления пациента: {new_registration_str}")

visit_card = 2140

is_visited = visit_card in visited
if is_visited:
    answer = "Да"
else:
    answer = "Нет"
print(f"Пациент {visit_card} посетил врача: {answer}")

get_name_card = 2121
patient_name = patients[get_name_card]
print(f"ФИО пациента {get_name_card}: {patient_name}")