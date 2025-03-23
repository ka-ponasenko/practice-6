import math

def circle_position(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    
    match distance:
        case d if d > r1 + r2:
            return "Окружности лежат одна вне другой, не касаясь"
        case d if d == r1 + r2:
            return "Окружности имеют внешнее касание"
        case d if abs(r1 - r2) < d < r1 + r2:
            return "Окружности пересекаются"
        case d if d == abs(r1 - r2):
            return "Окружности имеют внутреннее касание"
        case d if d < abs(r1 - r2):
            return "Одна окружность лежит внутри другой, не касаясь"
        case _:
            return "Ошибка: невозможно определить расположение"

x1, y1 = map(float, input("Введите координаты центра первой окружности (x1 y1): "))
r1 = float(input("Введите радиус первой окружности: "))
x2, y2 = map(float, input("Введите координаты центра второй окружности (x2 y2): "))
r2 = float(input("Введите радиус второй окружности: "))


result = circle_position(x1, y1, r1, x2, y2, r2)

print(result)