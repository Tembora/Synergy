a, b, c, d, e = map(int, input("введите целое, пятизначное число:"))
#возводим десятки в степень едениц
x = d ** e
#результат умножаем на сотни
y = x * c
# разность десятков тысяч и тысяч
z = a - b
f = y / z
print(f)