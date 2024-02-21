from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Plugins import handle_song , start_command , help_command
from config import TOKEN

print('Starting up bot...')
async def bad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Raise an error to trigger the error handler."""
    await context.bot.wrong_method_name()  # type: ignore[attr-defined]

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    # app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('song', handle_song))
    app.add_handler(CommandHandler("error", bad_command))
    app.add_error_handler(error_handler)
    print('Polling...')
    app.run_polling(poll_interval=3)
