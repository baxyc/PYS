# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def uniq_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]
print(uniq_list(int(input())))