import timeit
lst1 = [1,2,3]
set1 = {1,2,3}
lst2 = [1,2,3,4,5,6,3534]
set2 = {1,2,3,4,5,6,3534}
lst3 = [1,2,3,4,5,6,43,3445,3534]
set3 = {1,2,3,4,5,6,43,3445,3534}
a = 5
b = 0
timelst1 = timeit.timeit("a in lst1", globals=globals(), number=100_000)
timeset1 = timeit.timeit("a in set1", globals=globals(), number=100_000)
timelst2 = timeit.timeit("a in lst2", globals=globals(), number=100_000)
timeset2 = timeit.timeit("a in set2", globals=globals(), number=100_000)
timelst3 = timeit.timeit("a in lst3", globals=globals(), number=100_000)
timeset3 = timeit.timeit("a in set3", globals=globals(), number=100_000)

timelstno1 = timeit.timeit("b in lst1", globals=globals(), number=100_000)
timesetno1 = timeit.timeit("b in set1", globals=globals(), number=100_000)
timelstno2 = timeit.timeit("b in lst2", globals=globals(), number=100_000)
timesetno2 = timeit.timeit("b in set2", globals=globals(), number=100_000)
timelstno3 = timeit.timeit("b in lst3", globals=globals(), number=100_000)
timesetno3 = timeit.timeit("b in set3", globals=globals(), number=100_000)

print(f"List 1: {lst1}, List2: {lst2}, List 3: {lst3}")
print(f"Set 1: {set1}, Set 2: {set2}, Set 3: {set3}")
print(f"Timeit значение есть: 1: {timelst1}, {timeset1}")
print(f"Timeit значение есть: 2: {timelst2}, {timeset2}")
print(f"Timeit значение есть: 3: {timelst3}, {timeset3}")
print(f"Timeit значения нет: 1: {timelstno1}, {timesetno1}")
print(f"Timeit значения нет: 2: {timelstno2}, {timesetno2}")
print(f"Timeit значения нет: 3: {timelstno3}, {timesetno3}")

# вывод: список дольше обрабатывается