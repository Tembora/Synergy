m = int(input())
n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))

for j in range(len(a)):
    if a[j] + min(a) <= m:
        b += [[a[j], min(a)]]
        a[j] += m
        a[a.index(min(a))] += m
    else:
        if a[j] > m:
            continue
        else:
            b += [[a[j]]]
print(len(b))

