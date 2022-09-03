'''
2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
Предикату можно заменить на понятие "бит".
Должна получиться таблица истинности.
'''

def table_truth():
    booleans = (True, False)
    print("X     Y     Z     Result")
    for x in booleans:
        for y in booleans:
            for z in booleans:
                print(f"{str(x):5s} {str(y):5s} {str(z):5s} {str(not (x or y or z) == (not x and not y and not z)):5s}")

table_truth()
