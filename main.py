from util import *

print('Вас приветствует банкомат банка "Рога & Копыта"!')
data_lines = []
while True:
    print("  1. Восстановить данные.")
    print("  2. Создать аккаунт.")
    print("  3. Выход из приложения.")
    operation = input("Введите номер операции: ")
    if operation == '1':
        try:
            with open("data.txt") as file_in:
                for lines in file_in.readlines():  # .read().splitlines():
                    data_lines.append(lines.strip())
        except FileNotFoundError:
            print('Восстановить данные невозможно. Файл данных отсутствует.')
            exit()

        user_name = data_lines[0]
        user_year = int(data_lines[1])
        user_password = data_lines[2]
        tmp_password = input("Введите пароль: ")
        if not tmp_password == user_password:
            print("Введен неверный пароль!")
            print()
            print("Для продолжения введите номер операции.")
        else:
            print()
            print(f'Вы вошли в аккаунт: {user_name} ({2024 - user_year} лет)')
            print("Для продолжения введите номер операции.")
        break

    elif operation == '2':
        user_name = input("Введите ФИО: ")
        type_check = False
        while type_check == False:
            try:
                user_year = int(input("Введите год рожнения: "))
                type_check = True
            except ValueError:
                print('Необходимо указать числовое значение.')
                print()

        print("Создан аккаунт: " + user_name + " (" + str(2024 - user_year) + " лет)")
        user_password = input("Создайте пароль для аккаунта: ")
        user_account, user_limit = 0, 0
        data_lines = [
            user_name, user_year, user_password, user_account, user_limit
        ]
        file_save(data_lines)
        print("Аккаунт успешно зарегистрирован!")
        print()
        print("Для продолжения введите номер операции.")
        break

    elif operation == '3':
        print()
        print("Спасибо за пользование нашей программой. До свидания!")
        exit()
    else:
        print()
        print("Указан несуществующий номер операции. Повторите попытку.")

while True:
    print("  1. Положить деньги на счет.")
    print("  2. Снять деньги.")
    print("  3. Вывести баланс на экран.")
    print("  4. Установка лимита на счет.")
    print("  5. Запись ожидаемой транзакции.")
    print("  6. Выполнить транзакции.")
    print("  7. Статистика по ожидаемым транзакциям.")
    print("  8. Фильтр по ожидаемым транзакциям.")
    print("  9. Выход из приложения.")
    operation = input("Введите номер операции: ")

    if operation == '1':
        type_check = False
        while type_check == False:
            try:
                user_cash = int(input("Введите сумму пополнения (для отмены операции введите 0): "))
                type_check = True
            except ValueError:
                print('При вводе суммы пополнения, необходимо указать числовое значение.')
                print()

        if user_cash > 0:
            data_lines[3] = int(data_lines[3]) + user_cash
            file_save(data_lines)
            print(f'Счёт успешно пополнен на сумму: {user_cash} руб.')

        print()
        print("Для продолжения введите номер операции.")

    elif operation == '2':
        tmp_password = input("Введите пароль: ")
        user_password = data_lines[2]
        if not tmp_password == user_password:
            print("Введен неверный пароль!")
            print()
            print("Для продолжения введите номер операции.")
        else:
            user_account = int(data_lines[3])
            type_check = False
            while type_check == False:
                try:
                    print(f'Ваш текущий баланс: {user_account} руб.')
                    user_pick = int(input("Введите сумму для снятия: "))
                    type_check = True
                except ValueError:
                    print('При вводе суммы снятия, необходимо указать числовое значение.')
                    print()

            if user_pick > 0:
                if user_account - user_pick < 0:
                    print(f'Выполнение операции невозможно! Ваш текущий баланс: {user_account} руб.')
                else:
                    user_account -= user_pick
                    data_lines[3] = user_account
                    file_save(data_lines)
                    print(f'Снятие успешно завершено! Ваш баланс: {user_account} руб.')

            print()
            print("Для продолжения введите номер операции.")

    elif operation == '3':
        tmp_password = input("Введите пароль: ")
        user_password = data_lines[2]
        if not tmp_password == user_password:
            print("Введен неверный пароль!")
        else:
            user_account = int(data_lines[3])
            print(f'Ваш баланс {user_account} руб.')

        print()
        print("Для продолжения введите номер операции.")

    elif operation == '4':
        user_limit = int(data_lines[4])
        type_check = False
        while type_check == False:
            try:
                print(f'На Ваш счет установлен лимит в {user_limit} руб.')
                user_limit = int(input("Изменить лимит на счет: "))
                type_check = True
            except ValueError:
                print('При изменении лимита, необходимо указать числовое значение.')
                print()

        data_lines[4] = user_limit
        file_save(data_lines)
        print(f'Установлен лимит на счет: {user_limit} руб.')
        print()
        print("Для продолжения введите номер операции.")

    elif operation == '5':
        type_check = False
        while type_check == False:
            try:
                trans_summ = int(input("Укажите сумму ожидаемой транзакции: "))
                type_check = True
            except ValueError:
                print('Необходимо указать числовое значение.')
                print()

        trans_note = input("Наименование ожидаемой транзакции: ")
        trans_line = str(trans_summ) + ";" + trans_note + ";0"
        data_lines.append(trans_line)
        with open("data.txt", 'a') as file_add:
            file_add.write(str(trans_line) + '\n')
        print(f'Ожидаемая транзакция "{trans_note}" на сумму {trans_summ} руб. установлена.')

        count = 0
        for i in range(len(data_lines)):
            if i > 4:
                trans_item = data_lines[i].split(";")
                if int(trans_item[2]) == 0:
                    count += 1
        print(f'Количество ожидаемых транзакций: {count}')
        print()
        print("Для продолжения введите номер операции.")

    elif operation == '6':
        s = ''
        user_account = int(data_lines[3])
        user_limit = int(data_lines[4])
        for i in range(len(data_lines)):
            if i > 4:
                trans_item = data_lines[i].split(";")
                trans_summ = int(trans_item[0])
                if int(trans_item[2]) == 0:
                    if user_account - trans_summ >= user_limit:
                        user_account -= trans_summ
                        data_lines[3] = user_account
                        trans_item[-1] = '1'
                        data_lines[i] = trans_item[0] + ";" + trans_item[1] + ";" + trans_item[2]
                        s = s + "\n" + (
                            f'Транзакция "{trans_item[1]}" на сумму {trans_item[0]} руб. успешно применена.')
                    else:
                        s = s + "\n" + (
                            f'Транзакция "{trans_item[1]}" на сумму {trans_item[0]} руб. не может быть применена (превышен лимит).')
        file_save(data_lines)
        print(s)
        print(f'На Ваш счет установлен лимит в {user_limit} руб. Текущий баланс счета {user_account} руб.')
        print()
        print("Для продолжения введите номер операции.")

    elif operation == '7':
        trans_dict = {}
        for i in range(len(data_lines)):
            if i > 4:
                trans_item = data_lines[i].split(";")
                if int(trans_item[2]) == 0:
                    trans_info = []
                    if trans_item[1] not in trans_dict:
                        trans_dict[trans_item[1]] = 1
                    else:
                        trans_dict[trans_item[1]] += 1

        if len(trans_dict) == 0:
            print("Ожидаемых транзакций нет.")
            print()
            print("Для продолжения введите номер операции.")
        else:
            print("Ожидаемые транзакции:")
            for name, count in trans_dict.items():
                print(
                    f'Количество платежей "{name}": {count}, на общую сумму {transaction_amount(data_lines, name)} руб.')
            print()
            print("Для продолжения введите номер операции.")

    elif operation == '8':
        type_check = False
        while type_check == False:
            try:
                user_filter = int(input("Показать ожидаемые транзакции, сумма которых больше: "))
                type_check = True
            except ValueError:
                print('Необходимо указать числовое значение.')
                print()

        count = 0
        for summa, name in transaction_filter(data_lines):
            if summa > user_filter:
                print(f'Транзакция "{name}", на сумму {summa} руб.')
                count += 1

        if count == 0:
            print(f'Ожидаемых транзакции, сумма которых больше {user_filter} руб. нет.')

        print()
        print("Для продолжения введите номер операции.")

    elif operation == '9':
        print()
        print("Спасибо за пользование нашей программой. До свидания!")
        break
    else:
        print()
        print("Указан несуществующий номер операции. Повторите попытку.")
