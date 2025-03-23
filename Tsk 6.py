import math
N = int(input("Введите количесвто малышей: "))
K = int(input("Введите количесвто мест на карусели: "))
M = int(input("Введите время одного сеанса: "))
time = math.ceil((2*N)/K)*M
print(f"Минимальное время: {time}")