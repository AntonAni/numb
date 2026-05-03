# задаем переменные с количеством дней
month_1 = "31 день"
month_2 = "этот месяц может состоять из 28 или 29 дней"
month_3 = "31 день"
month_4 = "30 дней"
month_5 = "31 день"
month_6 = "30 дней"
month_7 = "31 день"
month_8 = "31 день"
month_9 = "30 дней"
month_10 = "31 день"
month_11 = "30 день"
month_12 = "31 день"
# задаем запрос на ввод месяца
inp_month = input("Введите месяц: ").strip().lower()
# сравниваем введенное значение и ввыводим результат
if inp_month == "январь":
    print(month_1)
elif inp_month == "февраль":
    print(month_2)
elif inp_month == "март":
    print(month_3)
elif inp_month == "апрель":
    print(month_4)
elif inp_month == "май":
    print(month_5)
elif inp_month == "июнь":
    print(month_6)
elif inp_month == "июль":
    print(month_7)
elif inp_month == "август":
    print(month_8)
elif inp_month == "сентябрь":
    print(month_9)
elif inp_month == "октябрь":
    print(month_10)
elif inp_month == "ноябрь":
    print(month_11)
elif inp_month == "декабрь":
    print(month_12)
else:print("Неправильно введен месяц")