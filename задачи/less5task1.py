a = int(input("Ведите число"))
if a >= 0 and a % 2 == 0:
    print("положительное четное число")
elif a <= 0 and a % 2 == 0:
    print("отрицательное четное число")
else:
    print("число не является четным")
