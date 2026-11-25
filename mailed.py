# ЗАДАЧА 19. Телефонная книга с командами
# ----------------------------------------------------------------
# Условие:
#     Словарь «имя → телефон». Команды:
#         add <имя> <телефон>   — добавить/обновить запись
#         get <имя>             — получить телефон
#         del <имя>             — удалить
#         list                  — вывести все записи
#     Если имени нет при get/del — вывести "не найдено".
#
# Данные:
#     add Аня +996700111222  -> добавлено
#     add Борис +996700333444 -> добавлено
#     get Аня                -> +996700111222
#     get Петя               -> не найдено
#     del Борис              -> удалено
#     list                   -> Аня: +996700111222
#
phonebook = {}

while True:
    command = input("Введите команду: ")

    parts = command.split()

    if parts[0] == "add":
        name = parts[1]
        phone = parts[2]

        phonebook[name] = phone

        print("добавлено")

    elif parts[0] == "get":
        name = parts[1]

        if name in phonebook:
            print(phonebook[name])
        else:
            print("не найдено")

    elif parts[0] == "del":
        name = parts[1]

        if name in phonebook:
            del phonebook[name]
            print("удалено")
        else:
            print("не найдено")

    elif parts[0] == "list":
        for name, phone in phonebook.items():
            print(name + ":", phone)

    elif parts[0] == "exit":
        break
