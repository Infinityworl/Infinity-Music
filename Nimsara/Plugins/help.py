from telegram import Update
from telegram.ext import ContextTypes

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text('Try typing anything, and I will do my best to respond.')
