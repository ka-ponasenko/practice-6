A = int(input("Введите длину ковра: "))
B = int(input("Введите ширину ковра: "))
D = 6.5*2
hypotenus = A**0.5 + B**0.5
if hypotenus<=D:
    print("Да")
else:
    print("Нет")