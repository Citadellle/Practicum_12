#18
text = input().split()
necessary_length = int(input())

string = ''
i = 0

for e in text:
    if len(string) + 1 + len(e) <= necessary_length and e != text[-1]:
        if i != 0:
            string += ' '

        string += e
        i += 1

    else:
        if len(string) < necessary_length:
            string_as_list = string.split()
            string_as_list_c = string_as_list.copy()
            q_words = len(string_as_list)

            j = 1

            while len(''.join(string_as_list)) < necessary_length:
                if q_words > 1:
                    string_as_list.insert(string_as_list.index(string_as_list_c[j]), ' ')

                    j += 1
                    if j >= len(string_as_list_c):
                        j = 1
                        
                else:
                    q_space = necessary_length - len(string_as_list[0])
                    string_as_list.append(' ' * q_space)


            print(''.join(string_as_list))
            string = e
            i = 1

        else:
            print(string)
            string = e
            i = 1