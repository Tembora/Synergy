word = str((input().lower()))
res = word[::-1]
if word == res:
    print('yes')
else:
    print('no')
