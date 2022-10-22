def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Закончить работу")
    while 1:
        try:
            choice = int(input('Введите цифру: '))
            if choice not in [1, 2, 3, 4, 5]:
                print('Некорректный ввод!')
            break
        except:
            print('Некорректный ввод!')
    return choice


def read_file(filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def show_file(filename):
    for row in read_file(filename):
        print(*row.values())


def show_by_surname(filename):
    surname = input('Введите фамилию: ')
    for row in read_file(filename):
        if surname == row['Фамилия']:
            return row.values()
    return 'Нет данных',


def show_by_phone(filename):
    phone = input('Введите номер телефона: ')
    for row in read_file(filename):
        if phone == row['Телефон']:
            return row.values()
    return 'Нет данных',


def write_file(filename):
    with open(filename, 'a', encoding='utf-8') as out:
        record = input('Введите через * фимилию, имя, телефон, описание:\n').split('*')
        out.write(','.join(record) + '\n')
    return


while 1:
    try:
        format_file = int(input("\n1. Справочник с расширением '.txt'\n"
                                "2. Справочник с расширением '.csv'\n"
                                "Введите цифру: "))
        if format_file == 1:
            file_name = 'phonebook.txt'
            break
        elif format_file == 2:
            file_name = 'phonebook.csv'
            break
        else:
            print('Некорректный ввод!')
    except:
        print('Некорректный ввод!')


while 1:
    menu = show_menu()
    if menu == 1:
        print()
        show_file(file_name)
        menu = show_menu()

    elif menu == 2:
        print()
        print(*show_by_surname(file_name))
        menu = show_menu()

    elif menu == 3:
        print()
        print(*show_by_phone(file_name))
        menu = show_menu()

    elif menu == 4:
        print()
        print(write_file(file_name))
        menu = show_menu()

    elif menu == 5:
        break