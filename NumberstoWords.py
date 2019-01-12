# A program that uses the Inflect library to read numbers as words. The elusive place value program I have been looking for.
# Code for the inflect library from https://pypi.python.org/pypi/inflect
# Code for the Num 2 Words library from https://pypi.python.org/pypi/num2words
# Code for the Roman Numerals is from https://stackoverflow.com/questions/42875103/integer-to-roman-number
# Upper limit on the Roman Numerals is 3999. 
# I had to lose Arabic and Hebrew as they didn't print out in the console window, so only 13 languages available in the executable file.

from num2words import num2words
import inflect
p = inflect.engine()

def int_to_Roman(num):
   val = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   syb = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   roman_num = ""
   for i in range(len(val)):
      count = int(num / val[i])
      roman_num += syb[i] * count
      num -= val[i] * count
   return roman_num

while True:

    print("A Python Place Value Program")
    print()
    print("1. Cardinal number without a decimal point")
    print("2. A cardinal number with a decimal point")
    print("3. A cardinal number translated to one of 13 different languages to choose from")
    print("4. A cardinal number translated to Roman Numerals")

    print()

    # Take input from the user 
    choice = input("Enter choice(1/2/3/4): ",)
    print()

    if choice == '1':
        num1 = int(input("Enter your number in order to find out its place value: ", ))
        print()
        words = p.number_to_words(num1)
        print("Your number is: ", words)

    elif choice == '2':
        num1 = float(input("Enter your decimal number in order to find out its place value: ", ))
        print()
        words = p.number_to_words(num1)
        print("Your number is: ", words)

    elif choice == '3':
        print("Enter your choice of language to translate your number to:")
        print("""Here are your choices == 1-French/2-German/3-Spanish/4-Lithuanian/5-Latvian/6-British English/
7-Indian English/8-Norwegian/9-Polish/10-Russian/11-Danish/12-Brazilian Portuguese/13-Italian""")
        print()
        choice2 = input("(1/2/3/4/5/6/7/8/9/10/11/12/13): ",)
        print()
        if choice2 == '1':
            num1 = int(input("Enter your number in order to find out its place value in French: ", ))
            print()
            frenchNum = num2words(num1, lang='fr')
            print("Your number in French is: ", frenchNum)
        
        elif choice2 == '2':
            num1 = int(input("Enter your number in order to find out its place value in German: ", ))
            print()
            germanNum = num2words(num1, lang='de')
            print("Your number in German is: ", germanNum)

        elif choice2 == '3':
            num1 = int(input("Enter your number in order to find out its place value in Spanish: ", ))
            print()
            spanishNum = num2words(num1, lang='es')
            print("Your number in Spanish is: ", spanishNum)

        elif choice2 == '4':
            num1 = int(input("Enter your number in order to find out its place value in Lithuanian: ", ))
            print()
            lithuanianNum = num2words(num1, lang='lt')
            print("Your number in Lithuanian is: ", lithuanianNum)

        elif choice2 == '5':
            num1 = int(input("Enter your number in order to find out its place value in Latvian: ", ))
            print()
            latvianNum = num2words(num1, lang='lv')
            print("Your number in Latvian is: ", latvianNum)

        elif choice2 == '6':
            num1 = int(input("Enter your number in order to find out its place value in British English: ", ))
            print()
            britishNum = num2words(num1, lang='en_GB')
            print("Your number in British English is: ", britishNum)

        elif choice2 == '7':
            num1 = int(input("Enter your number in order to find out its place value in Indian English: ", ))
            print()
            indianNum = num2words(num1, lang='en_IN')
            print("Your number in Indian English is: ", indianNum)

        elif choice2 == '8':
            num1 = int(input("Enter your number in order to find out its place value in Norwegian: ", ))
            print()
            norwegianNum = num2words(num1, lang='no')
            print("Your number in Norwegian is: ", norwegianNum)

        elif choice2 == '9':
            num1 = int(input("Enter your number in order to find out its place value in Polish: ", ))
            print()
            polishNum = num2words(num1, lang='pl')
            print("Your number in Polish is: ", polishNum)

        elif choice2 == '10':
            num1 = int(input("Enter your number in order to find out its place value in Russian: ", ))
            print()
            russianNum = num2words(num1, lang='ru')
            print("Your number in Russian is: ", russianNum)

        elif choice2 == '11':
            num1 = int(input("Enter your number in order to find out its place value in Danish: ", ))
            print()
            danishNum = num2words(num1, lang='dk')
            print("Your number in Danish is: ", danishNum)

        elif choice2 == '12':
            num1 = int(input("Enter your number in order to find out its place value in Brazilian Portuguese: ", ))
            print()
            brazilianNum = num2words(num1, lang='pt_BR')
            print("Your number in Brazilian Portuguese is: ", brazilianNum)

        elif choice2 == '13':
            num1 = int(input("Enter your number in order to find out its place value in Italian: ", ))
            print()
            italianNum = num2words(num1, lang='it')
            print("Your number in Italian is: ", italianNum)


    elif choice == '4':
        num1 = int(input("Enter any number between 1 and 3999 in order to find out what it is in Roman Numerals: ", ))
        print()
        words = int_to_Roman(num1)
        print("Your number in Roman numerals is: ", words)

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break