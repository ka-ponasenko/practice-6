position = input("Введите клетку на шахматном поле (буква, цифра): ")

if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
    print("Некорректный ввод. Попробуйте снова.")
else:
    letter = position[0]
    number = int(position[1])

    if (letter in 'aceg' and number % 2 != 0) or (letter in 'bdfh' and number % 2 == 0):
        print("Чёрный")
    else:
        print("Белый")