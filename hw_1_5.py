'''
5-Напишите программу, которая принимает на вход координаты двух точек и
находит расстояние между ними в 2D пространстве.

*Пример:*

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''


def distance():
    a = input("Enter integer coord (X and Y) separated by space for point A: ").split()
    b = input("Enter integer coord (X and Y) separated by space for point B: ").split()
    print("Distance between A and B is: ",
          round(((int(b[0]) - int(a[0]))**2 + (int(b[1]) - int(a[1]))**2)**0.5, 2))


distance()
