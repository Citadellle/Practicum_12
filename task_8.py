#8
s = input().split()
s = sorted(s, key = len)
print(*s, sep='\n')