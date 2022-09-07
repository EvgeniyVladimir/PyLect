# print('hello world')
# типы данных и перемпенная
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))

# s = 'hello "world"'
# print(s) # вывод строки

# s = 'hello \n"world"'
# print(s) # вывод строки

# a = 123
# b = 1.23
# s = 'hello world'
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1, 2, 3]
# print(list)
# list = ['например 1', 'строка 2', 'число 3']
# print(list)

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# # print(a, b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')
# print (a, '+', b, '=', a+b)

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print (a, '+', b, '=', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# **, *, /, //, %, +, -
# (), Сокращенные операции
# a = 123
# b = 321
# c=a+b
# print(c)

# a = 12
# b = 8
# c = a // b # целые числа без остатка результат 1
# print(c)

# a = 12
# b = 8
# c = a / b # результат как для вещественных чисел  результат 1.5
# print(c)

# a = 12
# b = 8
# c = a % b # если требуется получить остаток от деления результат 4
# print(c)

# a = 2
# b = 8
# c = a ** b # возведение в степень результат 256
# print(c)

# a = 1.3
# b = 3
# c = round(a * b) # округление по математическим правилам результат 4
# print(c)

# a = 1.3
# b = 3
# c = round(a * b, 3) # округление по математическим правилам до 3х знаков после запятой результат 3,900 
#                     # естественно последние нули не выводятся
# print(c)

# a = 1.31245
# b = 3
# c = round(a * b, 5) # округление по математическим правилам до 5 знаков после запятой результат 3.93735
# print(c)

# a = 3
# a = a + 5 # тоже самое a +=5 результат 8
# print(a)

# a = 3
# a = a * 5 # тоже самое a *=5 результат 15
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, 
# is, is not, in, not in
# gen

# a = 1 < 3 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = 1 > 2 or 4<6
# print(f)

# f = [1, 2, 3, 4]
# print (f)
# print(2 in f)

# f = [1, 2, 3, 4]
# print (f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)

# f = [1, 2, 3, 4]
# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции 
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# # Логический оператор if, elif, else
# username = input ('Введите имя:')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', username)

# Управляющие контсрукции цикл While и for
#  Цикл While:

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# print(inverted)

#  Цикл While вместе с else:
# original = 23 
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

#  Цикл for:
# for i in enumeration:
# где i - переменная (счетчик), in - ключевое слово, enumeration - итерируемый объект (список) 

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 10 , 2):
#     print(i)

# for i in 'qwerty':
#     print(i)

# Строки
# Базовые API для работы со строками:

# text = 'съешь ещё этих мягких французских булок'

# print(len(text))                   # 39    - определение количества символов в строке
# print('ещё' in text)               # True  - проверка наличия подстроки в строке оператор  - in
# print(text.isdigit())              # False - проверка все ли символы в строке числа
# print(text.islower())              # True  - проверка все ли символы в строке символы нижнего регистра
# print(text.replace('ещё', 'ЕЩЁ'))  #       - что-то на что-то заменить

# for c in text:
#     print(c)


# # Срезы:
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                          # с
# print(text[1])                          # ъ
# #print(text[len(text)])                  # IndexError
# print(text[len(text)-1])                # к
# print(text[-5])                         # б
# print(text[:])                          # print(text)  
# print(text[:2])                         # съ
# print(text[len(text)-2:])               # ок
# print(text[2:9])                        # ешь ещё
# print(text[6:-18])                      # ещё этих мягких
# print(text[0:len(text):6])              # сеикакл
# print(text[::6])                        # сеикакл
# text = text[2:9] + text[-5] + text[:2]  # ...

#  Списки
numbers = [1,2,3,4,5]
# print(numbers)                             #   [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers)                             #  [1, 2, 3, 4, 5]

# ran = range(1, 6)                           #  приведениетипа range в тип list
# numbers = list(ran)                        #  приведение типа range --> list
# print(numbers)


# numbers[0] = 10
# print(numbers)                             #  [10, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'len(numbers) len')                 #  получить количество элементов списка   результат -> 5 len


# for i in numbers:
#     i *=2
#     print(i)                               #  [20, 4, 6, 8, 10]
# print(numbers)                             # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in color:
#     print(e)                                     # red green blue

# for e in colors:
#     print(e*2)                                   # redred greengreen blueblue

# colors.append('gray')                              # добавить в конец gray
# print(colors)

# print(colors == ['red', 'green', 'blue', 'gray'])  # True

# colors.remove('red') # del colors[0] тоже самое  # удалить нулевой элемент
# del colors[0]                                    # удалить нулевой элемент
# print(colors)

#  Функции в языке Python

# def function_name(x):     # где def - ключевое слово функции, function_name - имя функции, (x - аргументы):
    # body line 1         #  тело метода
    #...
    # body line n
    # optional return     #  может добавляться оператор возвращения значения

def f(x):
    if x == 1:
        return 'Целое'
    elif x ==2.3:
        return 23
    else:
        return
arg = 2
print(f(arg))
print(type(f(arg)))


