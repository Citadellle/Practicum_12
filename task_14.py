#14
hint = input()
word = input()
guess = ['*' for _ in range(len(word))]

for _ in range(25):
    print()

print(hint)

for i in range(10):
    for x in guess:
        print(x, end = '')
    print()

    choice = int(input('Буква или слово (0 - буква, 1 - слово)?'))

    match choice:
        case 0:
            letter_pick = input()
            
            if letter_pick in word:
                for i in range(word.count(letter_pick)):
                    guess[word.index(letter_pick, i)] = letter_pick

        case 1:
            word_pick = input()

            if word_pick == word:
                print('Победа!')
                break

            else:
                print('Проигрыш!')
                break

else:
    print('Проигрыш!')