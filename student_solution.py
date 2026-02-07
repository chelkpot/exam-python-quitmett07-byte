# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
s = input().strip()
substrings = s.split(',')
first, second = substrings[0], substrings[1]

# 1. Длина первой подстроки больше второй
print(len(first) > len(second))

# 2. Подстроки равны
print(first == second)

# 3. Вторая подстрока содержится в первой
print(second in first)


# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    s = input()

# 1. Строка без пробелов в начале и конце
stripped = s.strip()
print(stripped)

# 2. Количество символов в строке
print(len(s))

# 3. Количество букв a
print(s.count('a'))

# 4. Строка, где все буквы a заменены на @
print(s.replace('a', '@'))

# 5. True, если строка начинается с заглавной буквы
print(s.istitle())

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    s = input()

# 1. Строка без первого и последнего символа
print(s[1:-1])

# 2. Каждый второй символ строки
print(s[::2])

# 3. Строка в нижнем регистре, записанная в обратном порядке
print(s.lower()[::-1])


# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    numbers = list(map (int, input().split()))

# 1. Отсортированный список
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# 2. Сумма всех элементов
print(sum(numbers))

# 3. Минимальное и максимальное число
print(min(numbers), max(numbers))



# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    s = input()

# Проверка условий
is_palindrome = s.lower() == s.lower()[::-1]
no_spaces = ' ' not in s

# Вывод результата
print(is_palindrome and no_spaces)

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    num = int(input())

# Преобразование в 16-ричную систему
hex_str = hex(num)[2:]  # убираем префикс 0x

# Вывод результатов
print(hex_str)
print(len(hex_str))
print('a' in hex_str)

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_num = int(input())

# Получаем название месяца (индексация с 0)
print(months[month_num - 1])
