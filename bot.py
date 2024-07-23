from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Telegram Clicker bot!')

def handle_web_app_data(update: Update, context: CallbackContext) -> None:
    data = update.message.web_app_data.data
    update.message.reply_text(f'Received data: {data}')

def main() -> None:
    updater = Updater("6773275451:AAHBKW8RYToE3dIje9xsBnmkJ6t-VWZapfQ")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_web_app_data))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()