#20
#function for conjugating hundreds, tens, and ones
def convert_three_digits(num):
    result = []
    
    #hunders
    result.append(hundreds[num // 100])
    num %= 100
        
    #tens and units
    if num >= 20:
        result.append(tens[num // 10])
        result.append(units[num % 10])

    elif num >= 10:
        result.append(second_ten[num - 10])
        
    else:
        result.append(units[num])
        
    return ' '.join(result)


n = int(input())
result = []

units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 
         'девять']
second_ten = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 
              'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 
              'восемнадцать', 'девятнадцать']
tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 
        'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 
            'семьсот', 'восемьсот', 'девятьсот']


if n == 0:
    print('ноль')


#millions
if n >= 1000000:
    millions = n // 1000000
        
    if millions % 10 == 1 and  millions % 100 != 11:
        result.append(convert_three_digits(millions) + ' миллион')

    elif (millions % 10) in [2, 3, 4] and (millions % 100) not in [12, 13, 14]:
        result.append(convert_three_digits(millions) + ' миллиона')

    else:
        result.append(convert_three_digits(millions) + ' миллионов')

    n %= 1000000
    

#thousands
if n >= 1000:
    thousands = n // 1000
        
    if thousands % 10 == 1 and  thousands % 100 != 11:
        thousands_str = convert_three_digits(thousands)
        thousands_str = thousands_str.replace('один', 'одна')
        result.append(thousands_str + ' тысяча')

    elif (thousands % 10) in [2, 3, 4] and (thousands % 100) not in [12, 13, 14]:
        thousands_str = convert_three_digits(thousands)
        thousands_str = thousands_str.replace('два', 'две')
        result.append(thousands_str + ' тысячи')
            
    else:
        thousands_str = convert_three_digits(thousands)
        thousands_str = thousands_str
        result.append(thousands_str + ' тысяч')

    n %= 1000
    
    
#hundreds, tens, and ones
result.append(convert_three_digits(n))


print(' '.join(result))