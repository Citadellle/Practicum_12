#16
s = input()
t = 0

for i in range(len(s)):
    if s[i] == '(':
        t += 1
        
    elif s[i] == ')' and t > 0:
        t -= 1
    
    elif s[i] == ')' and t <= 0:
        print('Неправильно!')
        break
    
    if i == (len(s) - 1) and t != 0:
        print('Неправильно!')
        break

else:
    print('Правильно!')