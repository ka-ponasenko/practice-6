brick_size = input("Введите размеры кирпича (длину, ширину,высоту): ").split( )
hole = input("Введите размеры отверстия (длину, ширину): ").split( )
hole_size = int(hole[0])*int(hole[1])
sort_bricks = sorted(brick_size)
if int(sort_bricks[0])*int(sort_bricks[1])<=hole_size:
    print("Да")
else:
    print("Нет")