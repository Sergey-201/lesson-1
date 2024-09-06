seconds = int(input("Введите кол-во секунд: "))

if seconds < 0 or seconds >= 8640000:
    print("Число должно быть больше или равно 0 и меньше 8640000.")
else:
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дня"
    else:
        day_word = "дней"

    print(days, day_word + ",", str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
