words = ["яблоко", "asad", "кот", "asad", "собака", "asaad", "мяу"]

word_len = {}
for word in words:
    word_len[word] = len(word)

word_len_comp = {word: len(word) for word in words}
print("Словарь", word_len)
print("Словарь (dict comprehension)", word_len_comp)
print("Словари совпадают", word_len == word_len_comp)

print("Длина исходного списка:", len(words))
print("Количество элементов в словаре:", len(word_len))