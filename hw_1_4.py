'''
4- Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
'''


def value_range(quarter):
    match quarter:
        case 1:
            print("X ∈ (0, +∞), Y ∈ (0, +∞)")
        case 2:
            print("X ∈ (-∞, 0), Y ∈ (0, +∞)")
        case 3:
            print("X ∈ (-∞, 0), Y ∈ (-∞, 0)")
        case 4:
            print("X ∈ (0, +∞), Y ∈ (-∞, 0)")
        case _:
            print("Not a quarter number")


value_range(1)
value_range("a")
value_range(5)
