dates = ["01.05", "02.05", "03.05", "04.05"]
temperatures = [18, 23, 27, 21]
threshold = 22

print("Журнал")
for i, (date, temp) in enumerate(zip(dates, temperatures), start=1):
    print(f"{i}. {date} - {temp}°C")

hot_days = [date for date, temp in zip(dates, temperatures) if temp > threshold]
print("Дни с температурой выше порога", hot_days)

temp_dict = dict(zip(dates, temperatures))
print("Словарь температур", temp_dict)