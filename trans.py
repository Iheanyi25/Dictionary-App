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
                'thank you':'Imeela',
                'mother':'Nne',
                'father':'Nna',
                'children':'Umuaka',
                'child':'Nwa',
                'school':'Uloakwukwo',
                'land':"Ala",
                'water':'Mmiri',
                'house':'Ulo',
                'telephone':'Ekwenti',
                'spirit':'Mmuo',
                'masquerade':'Ekpo',
                'drink':'Mmanya',
                'food':'Nri',
                'grandfather':'Papa ukwu',
                'grandmother':'Mama ukwu',
                'eye':'Anya',
                'hand':'Aka',
                'mouth':'Onu',
                'head':'Isi',
                'chair':'Oche',
                'hair':'Ntutu',
                'leg':'Ukwu',
                'shoe':'Agba',
                'transformer':'Igwe oku',
                'light':'Oku',
                'money':'Ego',
                'university':'Mahadum',
                'principal':'Onye isi uloakwukwo'}
    engDict = {'dalu': 'Well done',
                'nnoo': 'Welocme',
                'bia':'Come',
                'kedu':'How are you',
                'ebee ka i si':'Where are you from',
                'kwusi':'Stop',
                'hafum aka':'Leave me alone',
                'biko':'Please',
                'ekele':'Greetings',
                'imeela':'Thank you',
                'nne':'Mother',
                'nna':'Father',
                'umuaka':'Children',
                'nwa':'Child',
                'uloakwukwo':'School',
                'ala':'Land',
                'mmiri':'Water',
                'ulo':'House',
                'ekwenti':'Telephone',
                'mmuo':'Spirit',
                'ekpo':'Masquerade',
                'mmanya':'Drink',
                'nri': 'Food',
                'papa ukwu': 'Grandfather',
                'mama ukwu': 'Grandmother',
                'anya': 'Eye',
                'aka': 'Hand',
                'onu': 'Mouth',
                'isi': 'Head',
                'oche': 'Chair',
                'ntutu': 'Hair',
                'ukwu': 'Leg',
                'agba': 'Leg',
                'igwe oku': 'Transformer',
                'oku': 'Light',
                'ego': 'Money',
                'mahadum': 'University',
                'onye isi uloakwukwo': 'Principal'}
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