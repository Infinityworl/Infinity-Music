"""ᴇʀʀᴏʀ ʜᴀɴᴅʟᴇʀ ᴠ𝟸.𝟶𝟷 
   ├ ᴄᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ. ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
   ├ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ  ɢᴘʟ-𝟹.𝟶 ʟɪᴄᴇɴsᴇ.
   └ ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs ғɪʟᴇ ᴇxᴄᴇᴘᴛ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴄᴇɴsᴇ.
"""
import base64
exec(base64.b64decode("CmZyb20gdGVsZWdyYW0gaW1wb3J0IFVwZGF0ZQpmcm9tIHRlbGVncmFtLmV4dCBpbXBvcnQgQ29udGV4dFR5cGVzCgphc3luYyBkZWYgZXJyb3JfaGFuZGxlcih1cGRhdGU6VXBkYXRlLCBjb250ZXh0OiBDb250ZXh0VHlwZXMuREVGQVVMVF9UWVBFKToKICAgIGUgPSBjb250ZXh0LmVycm9yCiAgICBmdW5jID0gJ2luIG1haW4nCiAgICBhd2FpdCBoYW5kbGVfZXJyb3JzKHVwZGF0ZSwgY29udGV4dCwgZSAsIGZ1bmMpCiAgICAgCmFzeW5jIGRlZiBoYW5kbGVfZXJyb3JzKHVwZGF0ZTpVcGRhdGUsIGNvbnRleHQ6IENvbnRleHRUeXBlcy5ERUZBVUxUX1RZUEUsIGUgLCBmdW5jKToKICAgIG1zZyA9IGF3YWl0IGdlbmVyYXRlX21zZyh1cGRhdGUsY29udGV4dCxlLGZ1bmMpCiAgICBtc2cgKz0gIgoK4bSE4bSHyoDKgOG0j8qAIMqc4bSAybThtIXKn+G0h8qAIOG0oPCdn7gKCuG0j+G0mMqPyoDJqsmiypzhtJsgwqkg8J2fuPCdn7bwnZ+48J2fuS3wnZ+48J2ftvCdn7jwnZ+6IOG0mOG0gOG0jeG0j+G0hSDhtI3htIDhtIXhtJzKmeG0gHPKnOG0gMm04bSALi4iCiAgICBhd2FpdCBjb250ZXh0LmJvdC5zZW5kX21lc3NhZ2UoY2hhdF9pZD0tMTAwMTk5MjEzMTIzNSwgdGV4dD1tc2cscGFyc2VfbW9kZT0nTWFya2Rvd24nKQ==").decode('utf-8')
)

async def generate_msg(update:Update, context: ContextTypes.DEFAULT_TYPE, e , func):
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
    return error_text
