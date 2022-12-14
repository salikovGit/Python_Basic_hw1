'''
3- Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

*Пример:*

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''


def coord_quarter():
    while True:
        a = input("Enter integer coord (X and Y) separated by space: ").split()
        try:
            x, y = int(a[0]), int(a[1])
            break
        except ValueError:
            print("X or Y is not an integer")
        except IndexError:
            print("Only one value found")
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print("not a coords")


coord_quarter()
