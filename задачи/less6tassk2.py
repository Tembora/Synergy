x = int(input())
cnt = 0
for i in range(1, x+1):
    if x % i == 0 and x <= 2*10**9:
        cnt += 1
print(cnt)
