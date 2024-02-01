"""ᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴠ𝟸.𝟶𝟷 
   ├ ᴄᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ. ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
   ├ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ  ɢᴘʟ-𝟹.𝟶 ʟɪᴄᴇɴsᴇ.
   └ ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs ғɪʟᴇ ᴇxᴄᴇᴘᴛ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴄᴇɴsᴇ.
"""
import base64
exec(base64.b64decode("CmZyb20gdGVsZWdyYW0gaW1wb3J0IFVwZGF0ZQpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgQ29udGV4dFR5cGVzCgphc3luYyBkZWYgZXJyb3JfaGFuZGxlcih1cGRhdGU6VXBkYXRlLCBjb250ZXh0OiBDb250ZXh0VHlwZXMuREVGQVVMVF9UWVBFKToKICAgICBlID0gY29udGV4dC5lcnJvcgogICAgIGZ1bmMgPSAnaW4gbWFpbicKICAgICBhd2FpdCBoYW5kbGVfZXJyb3JzKHVwZGF0ZSwgY29udGV4dCwgZSAsIGZ1bmMp").decode('utf-8')
)
async def handle_errors(update:Update, context: ContextTypes.DEFAULT_TYPE, e , func):
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message
    error_log = ''
    e = str(e)
    e = await block_text(e)

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
    await context.bot.send_message(chat_id=-1001992131235, text=error_text,parse_mode='Markdown')
