import sys

vois = {
    1: "Гав",
    2: "Мяу",
    3: "Хрю",
    4: "Му"
}

key = 2
name = vois.get(key)
print(f"Поиск по ключу {key}: {name}\n")

my_range = range(5)

my_list = list(my_range)
my_tuple = tuple(my_range)
my_set = set(my_range)
my_dict = {i: str(i) for i in my_range}

print(f"Список:   {sys.getsizeof(my_list)} байт")
print(f"Кортеж:  {sys.getsizeof(my_tuple)} байт")
print(f"Множество: {sys.getsizeof(my_set)} байт")
print(f"Словарь:  {sys.getsizeof(my_dict)} байт")
