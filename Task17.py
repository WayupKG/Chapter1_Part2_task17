def Task17():
    using_dict = '''
        1: 'google_kazakstan.txt',
        2: 'google_paris.txt',
        3: 'google_uar.txt',
        4: 'google_kyrgystan.txt',
        5: 'google_san_francisco.txt',
        6: 'google_germany.txt',
        7: 'google_moscow.txt',
        8: 'google_sweden.txt'
    '''
    word = "Введите слово - Hello "
    print(word)
    word_input = input("Введите слово - ")
    if word_input.lower() == "hello":
        print(using_dict)
        using_input_vybor = int(input("Выберите номер списка - "))
        if using_input_vybor == 1:
            file = open('google_kazakstan.txt', "w")
            print("Создан файл с имененем google_kazakstan.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 2:
            file = open('google_paris.txt', "w")
            print("Создан файл с имененем google_paris.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 3:
            file = open('google_uar.txt', "w")
            print("Создан файл с имененем google_uar.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 4:
            file = open('google_kyrgystan.txt', "w")
            print("Создан файл с имененем google_kyrgystan.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 5:
            file = open('google_san_francisco.txt', "w")
            print("Создан файл с имененем google_san_francisco.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 6:
            file = open('google_germany.txt', "w")
            print("Создан файл с имененем google_germany.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 7:
            file = open('google_moscow.txt', "w")
            print("Создан файл с имененем google_moscow.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        elif using_input_vybor == 8:
            file = open('google_sweden.txt', "w")
            print("Создан файл с имененем google_sweden.txt")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
        else:
            not_file = input('Такого файла нету создайте его Имя_файла: ')
            file = open(not_file, "w")
            file.write(input("Что вы хотите записать в файл - "))
            file.close()
Task17()