def valid(start, end):
    columns = 'abcdefgh'


    x1 = columns.index(start[0])
    y1 = int(start[1]) - 1
    x2 = columns.index(end[0])
    y2 = int(end[1]) - 1


    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

start_position = input("Введите начальную позицию (например, d4): ")
end_position = input("Введите конечную позицию (например, e5): ")

if valid(start_position, end_position):
    print("Конь может так ходить")
else:
    print("Конь не может так ходить")
