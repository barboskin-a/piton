import time

sizes = [10_000, 100_000, 1_000_000]

for size in sizes:
    numbers = list(range(size))
    print(f"Размер списка {size}")

    times = []
    for _ in range(7):
        start = time.time()
        res = []
        for x in numbers:
            if x % 2 == 0:
                res.append(x ** 2)
        times.append(time.time() - start)

    times_comp = []
    for _ in range(7):
        start = time.time()
        res_comp = [x ** 2 for x in numbers if x % 2 == 0]
        times_comp.append(time.time() - start)

    print("Цикл (7 замеров)", [round(t, 5) for t in times])
    print("Среднее (цикл)", round(sum(times) / 7, 5), "сек")

    print("LC (7 замеров)", [round(t, 5) for t in times_comp])
    print("Среднее (LC)", round(sum(times_comp) / 7, 5), "сек")