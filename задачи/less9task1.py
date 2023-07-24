n = int(input())
res = []
for i in range(n):
    a = list(map(int, input().split()))
    res = set(a)
    print(len(res))
