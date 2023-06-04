import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime  import datetime
import settings
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text

    print(user_text)
    update.message.reply_text(user_text)

def planets_const(update, context):
    planet_name = str(update.message.text.lower().split()[1])
    today = datetime.now().date().strftime("%Y/%m/%d")
    planet_dict = {'mars': ephem.Mars, 'venus': ephem.Venus, 'saturn': ephem.Saturn, 'Jupiter': ephem.Jupiter,
               'neptune': ephem.Neptune, 'uranus': ephem.Uranus, 'mercury': ephem.Mercury}
    planet_date = planet_dict[planet_name](f"{today}")
    constellation = ephem.constellation(planet_date)[1]
    update.message.reply_text(f"The planet {planet_name.title()} is currently in the {constellation} constellation.")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets_const))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))



    logging.info("Бот стартовал")
    mybot.start_polling() # Обращение за обновлениями на сервер
    mybot.idle() # Что бы работал постоянно

if __name__ == '__main__':
    print("Запущен бот")
    main()
