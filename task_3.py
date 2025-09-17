#3
s = input()
q = 0
i = 0

while s != len(s) * '*':
    if s[i] != '*':
        q += 1
        s = s.replace(s[i], '*')
    i += 1


print(q)
