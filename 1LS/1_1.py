# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
if a == b ** 2 or b == a ** 2:
    print('да')
else:
    print('Нет')