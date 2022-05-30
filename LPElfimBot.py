import logging
import structlog
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import Settings

logging.basicConfig(level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    LP_Elfim_Bot = Updater(Settings.API_KEY, use_context=True)

    dp = LP_Elfim_Bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logger = structlog.getLogger()
    logger.info("Бот стартовал")
    LP_Elfim_Bot.start_polling()
    LP_Elfim_Bot.idle()

if __name__ == "__main__":
    main()