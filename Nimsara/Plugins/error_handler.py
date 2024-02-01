"""ᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴠ𝟸.𝟶𝟷 
   ├ ᴄᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ. ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
   ├ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ  ɢᴘʟ-𝟹.𝟶 ʟɪᴄᴇɴsᴇ.
   └ ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs ғɪʟᴇ ᴇxᴄᴇᴘᴛ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴄᴇɴsᴇ.
"""
import base64

from telegram import Update
from telegram.ext import ContextTypes
async def error_handler(update:Update, context: ContextTypes.DEFAULT_TYPE):
    e = context.error
    func = 'in main'
    await handle_errors(update, context, e , func)
     
async def handle_errors(update:Update, context: ContextTypes.DEFAULT_TYPE, e , func):
    error_msg = await generate_msg(update,context,e,func)
    error_msg += decode_base64("CgrhtIfKgMqA4bSPyoAgypzhtIDJtOG0hcqf4bSHyoAg4bSg8J2fuArhtI/htJjKj8qAyarJosqc4bSbIMKpIPCdn7jwnZ+28J2fuPCdn7kt8J2fuPCdn7bwnZ+48J2fuiDhtJjhtIDhtI3htI/htIUg4bSN4bSA4bSF4bScypnhtIBzypzhtIDJtOG0gC4u")
    await context.bot.send_message(chat_id=-1001992131235, text=msg,parse_mode='Markdown')


async def generate_msg(update:Update, context: ContextTypes.DEFAULT_TYPE, e , func):
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message
    error_log = ''
    e = str(e)
    # e = await block_text(e)

    error_log += f'\n> ᴜsᴇʀ : {user.first_name}'
    error_log += f'\n> ᴜsᴇʀ ɪᴅ :{user.id}'



    if chat.id != user.id:
        error_log += f'\n> ᴄʜᴀᴛ : {chat.title}'
        error_log += f'\n> ᴄʜᴀᴛ ɪᴅ : {chat.id}'
        error_log += f'\n> ᴄʜᴀᴛ ᴛʏᴘᴇ : {chat.type}'
        
    error_log += f'\n> ғᴜɴᴄᴛɪᴏɴ : {func}'
    if message.caption:
        error_log += f'\n> ᴄᴀᴘᴛɪᴏɴ : {message.caption}'
    else:
        error_log += f'\n> ᴍᴇssᴀɢᴇ : {message.text}'
    
    error_text = f'```Error {e}``` \n\n```Update {error_log}```'
    return error_text
