# ih = input("Enter your name: ")

# if ih == "Iheanyi":
#     print("Welcome Iheanyi")

# elif ih == "Ihekweaba":
#     print("Welcome Ihekweaba")

# else:
#     print("Go away")

# from googletrans import Translator
# translator = Translator()
# lang = input("Press 1 for Eng-Igb and 2 for Igb-eng: ")
# print(lang)
# if lang == "1":
#     new = input("Enter english word or sentence here: ")
#     ih = translator.translate(new, dest='ig')
#     print(ih.text)
# elif lang == "2":
#     new2 = input("Enter igbo word or sentence here: ")
#     ih = translator.translate(new2, src= 'ig', dest='en')
#     print(ih.text)
# else: 
#     print("Enter something resonable")
while True:
    igboDict = {'come': 'bia', 
                'welcome':'Nnọọ', 
                'welcome':'Dalụ', 
                'How are you':'Kedụ',
                'where are you from':'Ebee ka i si',
                'stop':'Kwusi',
                'fire':'Ọkụ',
                'leave me alone':'Hafum aka',
                'please':'Biko'}
    engDict = {'dalu': 'Welcome',
                'nnoo': 'Welocme',
                'bia':'come',
                'kedu':'How are you',
                'ebee ka i si':'Where are you from',
                'kwusi':'Stop',
                'hafum aka':'Leave me alone',
                'biko':'Please'}

    choice = input("Press 1 for Eng-Igbo and 2 for Igbo-Eng: ")
    if choice == "1":
        j= input ("Enter a an English word: ")
        word = igboDict.get(j)
        if word:
            print(f'{j} in igbo means {word}')
        else:
            print(f'{j} cannot be found here')
    elif choice == "2":
        j= input ("Enter an Igbo word: ")
        word = engDict.get(j)
        if word:
            print(f'{j} in english means {word}')
        else:
            print(f'{j} cannot be found here')    
    else: 
        print("Your choice is not valid")

    while True:
        answer = input('Do you want to make another translation? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Goodbye')
        break
