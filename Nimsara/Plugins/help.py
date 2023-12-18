from telegram import Update
from telegram.ext import ContextTypes
from Plugins.help_functions.force_sub import force_sub_chanel

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    in_channel = await force_sub_chanel(update,context)
    if in_channel:
        await update.message.reply_text('Try typing anything, and I will do my best to respond.')
