squares = []
for number in range(101):
    if number % 2 == 0:
        squares.append(number ** 2)

squares_comp = [number ** 2 for number in range(101) if number % 2 == 0]

print(f"Списки совпадают: {squares == squares_comp}")
print(f"Первые 5 элементов: {squares[:5]}")
print(f"Последние 5 элемента: {squares[-5:]}")