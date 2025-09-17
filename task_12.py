#12
import keyword

s = input()
keywords = keyword.kwlist
number_errors = 0

if s[0].isdigit() or s in keywords:
    number_errors += 1

for i in s:
    if 'A' <= i <= 'Z' or 'a' <= i <= 'z' or i.isdigit() or i == '_':
        pass
    else:
        number_errors += 1

if number_errors == 0:
    print('Может')

else:
    print('Не может')