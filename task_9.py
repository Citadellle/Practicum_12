#9
s = input().split()

for e in s:
    if s.count(e) == 2:
        print(e)
        break