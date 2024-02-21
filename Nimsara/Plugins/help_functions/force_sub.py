@@ -1,21 +0,0 @@
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton	
from telegram.ext import ContextTypes	

async def force_sub_chanel(update: Update, context: ContextTypes.DEFAULT_TYPE):	
    message = update.edited_message or update.message	
    user = message.from_user	
    user_id = user.id	
    first_name = user.first_name	
    user_profile_link = f'[{first_name}](tg://user?id={user_id})'	
    channel_username = '@sinhalafilx'	
    member = await context.bot.get_chat_member(channel_username, user_id)	
    member = member.status	

    if member in ('kicked' , 'left' , 'restricted'):	
        photo="https://i.ibb.co/3zvHYPh/photo-2023-08-30-22-45-44.jpg"	
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ɪɴꜰɪɴɪᴛʏ ᴍᴏᴠɪᴇꜱ", url="https://t.me/sinhalafilx")]])	
        text =f"{user_profile_link}, \n\n🚫  ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ"	
        await update.message.reply_photo(caption=text, reply_markup=reply_markup,photo=photo,parse_mode='Markdown')	
        return False 	
    else:	
        return True
