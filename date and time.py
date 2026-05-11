# Функция для корректного ввода месяца
def get_month_input(prompt):
    while True:
        try:
            month = int(input(prompt).strip())  # Пробуем преобразовать ввод в целое число
            if month < 0:
                print("Месяц не может быть отрицательным. Пожалуйста, введите корректное число.")
            elif month > 12:
                print("Значение месяца не может быть больше 12-и")
            else:
                return month
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")
month = get_month_input(f"Введите месяц")
# Функция для корректного ввода года
def get_year_input(prompt):
    while True:
        try:
            year = str(input(prompt).strip())  # Пробуем преобразовать ввод в целое число
            if len(year) == 4:
                return year
            else:
                print("Значение года должно состоять из четырёх цифр")
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")
year = get_year_input(f"Введите год")
year = int(year)
import calendar
days = calendar.monthrange(year, month)
print(f"В {month} месяце {year} года {days} дней.")