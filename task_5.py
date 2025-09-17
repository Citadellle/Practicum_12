#5
s1, s2, s3 = input(), input(), input()

for i in range(len(s1)):
    if s1[i] not in s2 and s1[i] not in s3:
        print(s1[i])

for i in range(len(s2)):
    if s2[i] not in s1 and s2[i] not in s3:
        print(s2[i])
        
for i in range(len(s3)):
    if s3[i] not in s1 and s3[i] not in s2:
        print(s3[i])