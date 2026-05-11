# Задаем переменную для хранения возраста каждого человека
age_in_group = []

# Функция для получения корректного ввода возраста
def get_age_input(prompt):
    while True:
        try:
            age = int(input(prompt).strip())  # Пробуем преобразовать ввод в целое число
            if age < 0:
                print("Возраст не может быть отрицательным. Пожалуйста, введите корректный возраст.")
            else:
                return age
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")

# Количество людей в группе
num_group = get_age_input("Количество людей: ")

# Запрашиваем у пользователя ввод возрастов
for i in range(num_group):
    age = get_age_input(f"Введите возраст {i + 1}: ")
    age_in_group.append(age)

# Выводим количество людей в группе, введенные возрасты
print("В вашей группе", num_group, "людей")
print("Вы ввели следующие возрасты:", age_in_group)

# Цена билетов
total_price = 0

for age in age_in_group:
    if age < 3:
        # Дети до 2 лет допускаются бесплатно
        continue
    elif age <= 12:
        # Дети от 3 до 12 лет
        total_price += 200
    elif age <= 65:
        # Взрослый билет
        total_price += 500
    else:
        # Пенсионеры старше 65 лет
        continue

# Выводим общую стоимость билетов
print("Общая стоимость билетов:", total_price, "рублей")