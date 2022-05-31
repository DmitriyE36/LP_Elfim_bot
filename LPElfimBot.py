import logging
import structlog
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import Settings

logging.basicConfig(level=logging.INFO)
logger = structlog.getLogger()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    lp_elfim_bot = Updater(Settings.API_KEY, use_context=True)

    dp = lp_elfim_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logger.info("Бот стартовал")
    lp_elfim_bot.start_polling()
    lp_elfim_bot.idle()

if __name__ == "__main__":
    main()