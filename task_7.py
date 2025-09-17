#7
s = input().split()
min_count = 0

for i in range(len(s)):
    min_count = min(min_count, len(s[i]))
    
print(min_count)