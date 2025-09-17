#11
s = input().split()
for i in range(1, len(s)):
    if s[i-1][-1] != s[i][0]:
        if i % 2 == 0:
            print('Вася')
        else:
            print('Петя')
        break
else:
    if len(s) % 2 == 0:
        print('Вася')
    else:
        print('Петя')