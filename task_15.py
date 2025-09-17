#15
n = int(input())

for _ in range(25):
    print()


for _ in range(10):
    choice = int(input())
    bull, cow = 0, 0

    for i in str(choice):
        if i in str(n):

            if str(n).index(i) == str(choice).index(i):
                bull += 1

            else:
                cow += 1
                
    print(f'Быков: {bull} Коров: {cow}')
    

    if bull == 4:
        print('Победа!')
        break


else:
    print('Проигрыш!')