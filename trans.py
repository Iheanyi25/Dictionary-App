print("Welcome, follow the instructions below for word translations")
while True:
    igboDict = {'come': 'Bia', 
                'welcome':'Nnọọ', 
                'welcome':'Dalụ', 
                'how are you':'Kedụ',
                'where are you from':'Ebee ka i si',
                'stop':'Kwusi',
                'fire':'Ọkụ',
                'leave me alone':'Hafum aka',
                'please':'Biko',
                'congratulations':'Ekele',
                'thank you':'Imeela'}
    engDict = {'dalu': 'Welcome',
                'nnoo': 'Welocme',
                'bia':'Come',
                'kedu':'How are you',
                'ebee ka i si':'Where are you from',
                'kwusi':'Stop',
                'hafum aka':'Leave me alone',
                'biko':'Please',
                'ekele':'Congratulations',
                'imeela':'Thank you'}
    print(f'\tCOMMAND \tTRANSLATION')
    print('\t-------------------------------')
    print(f'\t1 \t\t English to Igbo')
    print(f'\t2 \t\t Other Languages to English')
    print()
    choice = input("Make a choice: ")
    if choice == "1":
        j = input ("Enter an English word or phrase: ")
        word = igboDict.get(j.lower())
        newJ = j[0:1].upper() + j[1:].lower()
        if word:
            print(f'{newJ} in igbo means {word}')
        else:
            print(f'{newJ} cannot be found here')
    elif choice == "2":
        print("Sorry, we have just Igbo language available for now")
        j= input ("Enter an Igbo word or phrase: ")
        word = engDict.get(j.lower())
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
