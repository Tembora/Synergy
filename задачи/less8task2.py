n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    a.insert(0, a.pop())
    print(a)
