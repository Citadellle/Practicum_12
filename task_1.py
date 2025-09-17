#1
s = input()

for i in range(len(s), 0, -1):
    if s.count(' ' * i):
        print(i)
        break