from telegram.ext import ContextTypes 
from Plugins.fonts.block_text import *

async def mention(user_id,context: ContextTypes.DEFAULT_TYPE):
    user = await context.bot.get_chat(user_id)
    first_name = await block_text(user.first_name)
    mention = f"[{first_name}](tg://user?id={user_id})"
    return mention
