from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Plugins import start_command ,error_handler , song
from config import TOKEN

print('Starting up bot...')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    # app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('song', song))
    app.add_error_handler(error_handler)
    print('Polling...')
    app.run_polling(poll_interval=3)
