K = int(input("Введите количество суши: "))
if K%10==5 or K%10==7 or (K%10==2 and K>=12):
    print("Да")
else:
    print("Нет")