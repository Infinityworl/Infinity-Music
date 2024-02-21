from telegram import Update
from telegram.ext import ContextTypes	from telegram.ext import ContextTypes


def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):	async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text('Try typing anything, and I will do my best to respond.')	    await update.message.reply_text('Try typing anything, and I will do my best to respond.')
0 comments on commit 4576c21
@Infinityworl
Comment
 
