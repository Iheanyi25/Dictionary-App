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
    igboDict = {'come': 'Bia', 
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
        j = input ("Enter an English word or phrase: ")
        word = igboDict.get(j.lower())
        newJ = j[0:1].upper() + j[1:].lower()
        if word:
            print(f'{newJ} in igbo means {word}')
        else:
            print(f'{newJ} cannot be found here')
    elif choice == "2":
        j= input ("Enter an Igbo word or phrase: ")
        word = engDict.get(j.lower)
        newJ = j[0:1].upper() + j[1:].lower()
        if word:
            print(f'{newJ} in English means {word}')
        else:
            print(f'{newJ} cannot be found in dictionary')    
    else: 
        print("Your choice is not valid")

    while True:
        answer = input('Do you want to translate another word or phrase? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Thank you!')
        break
