def get_digit(position):
    sequence = "0"
    for number in range(1, 201):
        sequence += str(number)
    return sequence[position - 1]

position = int(input("Введите порядковый номер: "))
digit = get_digit(position)
print(digit)
