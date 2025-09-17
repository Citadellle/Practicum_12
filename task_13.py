#13
def is_happy(a):
    if len(a)%2 == 0:
            if sum(map(int, a[:(len(a)//2)])) == sum(map(int, a[(len(a)//2):])):
                return True

s = input()
i = 1

while s != '':
    if is_happy(s) == True:
        print(i)
        break
    
    s = input()
    i += 1