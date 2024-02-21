from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Plugins import handle_song , start_command , help_command 
from config import TOKEN
print('Starting up bot...')
def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('song', handle_song))
    app.add_error_handler(error)
    print('Polling...')
    app.run_polling(poll_interval=5)
