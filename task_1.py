# Task_1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

days = [1, 2, 3, 4, 5, 6, 7]

num = int(input("Choose a number of day: "))


if num in days:
    if num == 6 or num == 7:
        print('no')
    else:
        print('yes')
else:
    print('not a correct number of day')


