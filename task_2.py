# 2
# a) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# b) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# a)
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y , z, end='\t'*3+'' , sep='\t')
            print((not(x or y or z)) == (not(x) and not(y) and not(z)))



# b)

x = int(input('Choose a number for x: '))
y = int (input('Choose a number for y: '))


if x > 0 and y > 0:
    print('You are on the I-quarter')
elif x < 0 and y > 0:
    print('You are on the II-quarter')
elif x < 0 and y < 0:
    print('You are on the III-quarter')
elif x > 0 and y < 0:
    print('You are on the IV-quarter')
else:
    print("The dots shouldn't be 0!")