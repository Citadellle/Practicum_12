#10
s = input().split()
for i in range(1, len(s)):
    if s[i] != s[0] and len(set(s[i])) == len(s[i]):
        print(s[i])