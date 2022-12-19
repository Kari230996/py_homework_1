# 3
# a) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в
#    этой четверти (x и y).
#
# b) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
#    между ними в 2D пространстве.


# a)

quarter = int(input('Choose a quarter from 1-4: '))

if quarter == 1:
    print('x > 0 and y > 0')
elif quarter == 2:
    print('x < 0 and y > 0')
elif quarter == 3:
    print('x < 0 and y < 0')
elif quarter == 4:
    print('You are on the IV-quarter')
else:
    print("Oops! This quarter does't exist")

# b)

from math import sqrt

x1 = int(input('Choose coordinate for x1: '))
y1 = int(input('Choose coordinate for y1: '))

x2 = int(input('Choose coordinate for x2: '))
y2 = int(input('Choose coordinate for y2: '))

print('%.2f'%(sqrt(((x2-x1)**2 + (y2-y1)**2))))
