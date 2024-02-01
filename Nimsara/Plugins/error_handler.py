"""ᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴠ𝟸.𝟶𝟷 
   ├ ᴄᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ. ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
   ├ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ  ɢᴘʟ-𝟹.𝟶 ʟɪᴄᴇɴsᴇ.
   └ ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs ғɪʟᴇ ᴇxᴄᴇᴘᴛ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴄᴇɴsᴇ.
"""
# import base64
# exec(base64.b64decode("CmZyb20gdGVsZWdyYW0gaW1wb3J0IFVwZGF0ZQpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgQ29udGV4dFR5cGVzCgphc3luYyBkZWYgZXJyb3JfaGFuZGxlcih1cGRhdGU6VXBkYXRlLCBjb250ZXh0OiBDb250ZXh0VHlwZXMuREVGQVVMVF9UWVBFKToKICAgIGUgPSBjb250ZXh0LmVycm9yCiAgICBmdW5jID0gJ2luIG1haW4nCiAgICBhd2FpdCBoYW5kbGVfZXJyb3JzKHVwZGF0ZSwgY29udGV4dCwgZSAsIGZ1bmMpCiAgICAgCmFzeW5jIGRlZiBoYW5kbGVfZXJyb3JzKHVwZGF0ZTpVcGRhdGUsIGNvbnRleHQ6IENvbnRleHRUeXBlcy5ERUZBVUxUX1RZUEUsIGUgLCBmdW5jKToKICAgIG1zZyA9IGF3YWl0IGdlbmVyYXRlX21zZyh1cGRhdGUsY29udGV4dCxlLGZ1bmMpCiAgICBtc2cgPSBmJ3ttc2d9CgrhtIThtIfKgMqA4bSPyoAgypzhtIDJtOG0hcqf4bSHyoAg4bSg8J2fuAoK4bSP4bSYyo/KgMmqyaLKnOG0myDCqSDwnZ+48J2ftvCdn7jwnZ+5LfCdn7jwnZ+28J2fuPCdn7og4bSY4bSA4bSN4bSP4bSFIOG0jeG0gOG0heG0nMqZ4bSAc8qc4bSAybThtIAuLicKICAgIGF3YWl0IGNvbnRleHQuYm90LnNlbmRfbWVzc2FnZShjaGF0X2lkPS0xMDAxOTkyMTMxMjM1LCB0ZXh0PW1zZyxwYXJzZV9tb2RlPSdNYXJrZG93bicp").decode('utf-8')
# )
from telegram import Update
from telegram.ext import ContextTypes

async def error_handler(update:Update, context: ContextTypes.DEFAULT_TYPE):
    e = context.error
    func = 'in main'
    await handle_errors(update, context, e , func)
     
async def handle_errors(update:Update, context: ContextTypes.DEFAULT_TYPE, e , func):
    msg = await generate_msg(update,context,e,func)
    msg = f"{msg}\n\nᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴠ𝟸\nᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ.."
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
