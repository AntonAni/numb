a = input('Введите первое слово').strip().lower()
b = input("Введите второе слово").strip().lower()
a = list(a)
b = list(b)
a.sort()
b.sort()
if a == b:
    print("Введенные слова анаграммы")
else:print("Введенные слова не являются анаграммами")
