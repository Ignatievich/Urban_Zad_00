""" Домашняя работа по уроку "Способы вызова функции"
====================================================
Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.
-------------------------------------------------------------------------
ЗАДАЧА: "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются
     от одного и того же пользователя(администрации или службы поддержки).
        Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию senderd_email, которая принимает 2 обычных аргумента: сообщение и получатель
              и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
    Внутри функции реализовать следующую логику:
        Проверка на корректность e-mail отправителя и получателя.
        Проверка на отправку самому себе.
        Проверка на отправителя по умолчанию.

Пункты задачи:
  - Создайте функцию senderd_email, которая принимает 2 обычных аргумента: message(сообщение),
    recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию
                                                    sender = "university.help@gmail.com".
  - Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    то вывести на экран(в консоль) строку:
                        "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
  - Если же sender и recipient совпадают, то вывести - "Нельзя отправить письмо самому себе!"
  - Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
                     "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
  - В противном случае вывести сообщение:
    "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
                    Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
                    За один вызов функции выводится только одно и перечисленных уведомлений!
                                                    Проверки перечислены по мере выполнения.
Пример результата выполнения программы:
Пример выполняемого кода (тесты):
senderd_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
senderd_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
senderd_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
senderd_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
Вывод на консоль:
Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!

Примечания:
    Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
    Именованные аргументы всегда идут после позиционных.

"""
#========== Определения функций: =======================

# Функция для отправки сообщений с проверкой корректности адреса:
def sender_email( message, recipient, *args, sender = 'university.help@gmail.com' ) :
    FlagR = FlagS = FlagU = FlagE = False # Объявляем флаги событий
# Чистим строки от лишних пробелов и переводим в нижний регистр
    rec = recipient.lower()
    rec = rec.replace(' ', '')
    sen = sender.lower()
    sen = sen.replace(' ', '')
# Проверка условий на корректность e-mail-ов отправителя и получателя.
    if sen == 'university.help@gmail.com' :
        FlagU = True    # Адрес отправителя -- адрес университета
    if rec == sen :
        FlagE = True    # Адрес отправителя и получателя совпадают
    if ( '@' in rec ) and ( ('.com' == rec[-4:]) or ('.ru' == rec[-3:]) or ('.net' == rec[-4:]) ) :
        FlagR = True    # Адрес получателя стандартный
    if ( '@' in sen ) and ( ('.com' == sen[-4:]) or ('.ru' == sen[-3:]) or ('.net' == sen[-4:]) ) :
        FlagS = True    # Адрес отправителя стандартный

# Логика действий по результатам проверки корректности:
    if FlagR and FlagU and not FlagE :
       print( 'Письмо успешно отправлено с адреса', sen, 'на адрес', rec )
    elif FlagR and FlagS and not FlagE :
        print( 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sen, 'на адрес', rec )
    elif not ( FlagR and FlagS ) and not FlagE :
        print( 'Невозможно отправить письмо с адреса', sen, 'на адрес', rec )
    elif FlagR and FlagS and FlagE :
        print( 'Нельзя отправить письмо самому себе!' )

#=========== А теперь тестируем функцию - senderd_email() =============
sender_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
sender_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
sender_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
sender_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



