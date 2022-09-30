# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample


def num_in_list(count, number):
    if count < 0:
        return 'Error'
    my_list = sample(range(1, count * 2), count)
    print(my_list)
    if number in my_list:
        return 'Yes'
    return 'No'


print(num_in_list(int(input()), int(input())))
