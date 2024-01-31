from telegram import  Update ,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

import asyncio

from help_functions import mention
from Database import add_served_user , add_served_chat
from config import img_start as LOGO


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    command = context.args[0] if context.args else ''
    if command:
        print(command)
    else:
        asyncio.create_task(start_cmd(update,context))
        if update.effective_chat.type == 'private':
            asyncio.create_task(add_served_user(update.effective_user.id))
        else:
            asyncio.create_task(add_served_chat(update.effective_chat.id))

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = await context.bot.get_me()
    BOT_NAME = bot.username
    user_id = update.effective_user.id
    user  = await mention(user_id,context)
    caption = f'ʜᴇʏ {user} !'
    
    inline_keyboard = [
        [InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕', url=f"http://t.me/{BOT_NAME}?startgroup=true")],
        [InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url=f"https://t.me/pc_games_4_u"),InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url=f"https://t.me/game_zone_pc")],
        [InlineKeyboardButton('ғᴇᴀᴛᴜʀᴇs' , callback_data=f'help : {user_id}')]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    try:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=LOGO, caption=caption,reply_markup=reply_markup,parse_mode='Markdown')
    except Exception as e:
        print(e)
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
    

