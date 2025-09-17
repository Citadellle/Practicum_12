#4
s = input()

for i in range(len(s)):
    if s.count(s[i]) == 3:
        print(s[i])
        break