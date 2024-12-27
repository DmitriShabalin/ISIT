import telebot

bot = telebot.TeleBot('7639290762:AAG44385maraA3TWoxIqfuB5zXRSrb28SAY')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет," + message.chat.first_name + "!")
        keyboardMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_z1 = telebot.types.KeyboardButton(text="Задание 1")
        key_z2 = telebot.types.KeyboardButton(text="Задание 2")
        key_z3 = telebot.types.KeyboardButton(text="Задание 3")
        key_z4 = telebot.types.KeyboardButton(text="Задание 4")
        key_z5 = telebot.types.KeyboardButton(text="Задание 5")

        keyboardMenu.add(key_z1, key_z2, key_z3, key_z4, key_z5)
        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboardMenu)

    if message.text == "Задание 1":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_test = telebot.types.KeyboardButton(text="Тестирование")
        key_web = telebot.types.KeyboardButton(text="Web")
        key_prog = telebot.types.KeyboardButton(text="Программирование")
        key_back = telebot.types.KeyboardButton(text="Назад")

        keyboard.add(key_test, key_web, key_prog)
        keyboard.add(key_back)

        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboard)

    if message.text == "Тестирование":
        bot.send_message(message.from_user.id, "Задание 1")
        bot.send_message(message.from_user.id, "Тестирование")
        bot.send_message(message.from_user.id,
                         "https://habr.com/ru/articles/549054/")
        bot.send_message(message.from_user.id,
                         "https://ru.hexlet.io/blog/posts/vidy-testirovaniya")
        bot.send_message(
            message.from_user.id,
            "https://skillbox.ru/media/code/chto_takoe_testirovanie_programm/")
    if message.text == "Web":
        bot.send_message(
            message.from_user.id,
            "https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/How_the_Web_works"
        )
        bot.send_message(
            message.from_user.id,
            "https://skyeng.ru/magazine/wiki/it-industriya/chto-takoe-veb/")
        bot.send_message(
            message.from_user.id,
            "https://www.ixbt.com/live/crypto/chto-takoe-web-30-maksimalno-prostym-yazykom.html"
        )
        bot.send_message(message.from_user.id, "")
    if message.text == "Программирование":
        bot.send_message(message.from_user.id, "Программирование")
        bot.send_message(
            message.from_user.id,
            "https://ru.hexlet.io/blog/posts/chto-takoe-programmirovanie")
        bot.send_message(
            message.from_user.id,
            "https://academyit.ru/courses/ИБКИИ512/?utm_source=yandex_aa&utm_medium=cpc&utm_campaign=МК_ИБКИИ512_кибер_месяц&utm_content=&utm_term=---autotargeting&yclid=6058826111887605759"
        )
        bot.send_message(
            message.from_user.id,
            "https://blog.skillfactory.ru/glossary/programmirovanie-eto/")
    if message.text == "Назад":
        keyboardMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_z1 = telebot.types.KeyboardButton(text="Задание 1")
        key_z2 = telebot.types.KeyboardButton(text="Задание 2")
        key_z3 = telebot.types.KeyboardButton(text="Задание 3")
        key_z4 = telebot.types.KeyboardButton(text="Задание 4")
        key_z5 = telebot.types.KeyboardButton(text="Задание 5")

        keyboardMenu.add(key_z1, key_z2, key_z3, key_z4, key_z5)
        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboardMenu)

    if message.text == "Задание 2":
        bot.send_message(message.from_user.id, "Задание 2")

        @bot.message_handler(content_types=['voice'])
        def get_voice_messages(message):
            if (message.voice):
                bot.send_message(
                    message.from_user.id,
                    message.chat.first_name + " " + "Вы прислали голосовое")

    if message.text == "Задание 3":
        bot.send_message(message.from_user.id, "Задание 3")
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        usedName = input()
        bot.send_message(message.from_user.id, "Привет," + usedName + "!")
    if message.text == "Задание 4":
        bot.send_message(message.from_user.id, "Задание 4")

    if message.text == "Задание 5":
        bot.send_message(message.from_user.id, "Задание 5")
       
bot.polling(none_stop=True, interval=0)
