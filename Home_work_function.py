"""Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
 Bill Gates"""

def bill_gates():
    name = 'Bill Gates'
    print("“Don't compare yourself with anyone in this world…\n"
          "if you do so, you are insulting yourself.”\n"
          f'{name.rjust(46)}')

print(bill_gates())


"""Напишите функцию, которая принимает два числа в качестве
параметра и отображает все четные числа между ними"""

def even_num(first_num, second_num):
    if first_num == second_num:
        print("Введены некорректные значения!")
        return
    if first_num > second_num:
        first_num, second_num = second_num, first_num
    for i in range(first_num, second_num + 1):
        if i % 2 == 0:
            print(i, end= " ")

print(even_num(15, 3))


"""Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата,
символ и переменную логического типа:
если она равна True, квадрат заполненный;
если False, квадрат пустой.
"""

def draw_square(side_lenght, symbol, filled):
    if side_lenght <= 0:
        print("Длина стороы квадрата должна быть больше 0!")
        return
    if filled:
        for i in range(side_lenght):
            print(symbol * side_lenght)
    else:
        for i in range(side_lenght):
            if i == 0 or i == side_lenght - 1:
                print(symbol * side_lenght)
            else:
                print(symbol + ' ' * (side_lenght - 2) + symbol)

print(draw_square(4, "*", True))
print(draw_square(4, "*", False))

"""Напишите функцию, которая возвращает минимальное из
пяти чисел. Числа передаются в качестве параметров."""

def min_num(one_num, two_num, three_num, four_num, five_num):
    return min(one_num, two_num, three_num, four_num, five_num)

print(f"Минимальное значение из введенных: {min_num(10, 5,13,1, 9)}")


"""Напишите функцию, которая возвращает произведение чисел в
указанном диапазоне. Границы диапазона передаются в
качестве параметров. Если границы диапазона перепутаны
(например, 5 - верхняя граница; 25 - нижняя граница), их нужно
поменять местами."""

def mul_num(start_num, finish_num):
    if start_num == finish_num:
        return "Введены некорректные значения диапозона!"
    if start_num > finish_num:
        start_num, finish_num = finish_num, start_num
    result = 1
    for i in range(start_num, finish_num + 1):
        result *= i
    return result

print(mul_num(int(input("Введите начало диапозона: ")), int(input("Введите конец дипозона: "))))



"""Напишите функцию, которая считает количество цифр в числе.
Число передаётся в качестве параметра. Из функции нужно
вернуть полученное количество цифр. Например, если
передали 3456, количество цифр будет 4."""

def digits_num(x):
    kol = 0
    for i in range(len(str(x))):
        kol += 1
    return kol

user_num = input("Введите число: ")
print(f"Количество цифр в числе {user_num}:", digits_num(user_num))


"""Напишите функцию, которая проверяет является ли число
палиндромом. Число передаётся в качестве параметра. Если
число палиндром нужно вернуть из функции true, иначе false.
«Палиндром» — это число, у которого первая часть цифр равна
второй перевернутой части цифр. Например, 123321—
палиндром(первая часть 123, вторая 321, которая после
переворота становится 123), 546645 — палиндром, а 421987 —
не палиндром."""


def palindrom(x):
    comp = ''.join(reversed(str(x)))
    return str(x) == str(comp)


num = int(input("Введите число: "))
if palindrom(num):
    print(f"Числo {num} - пaлиндром.")
else:
    print(f"Числo {num} - не пaлиндром.")











