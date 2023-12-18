from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import BOT_USERNAME , img_start
from Plugins.help_functions.mention import mention
from Plugins.help_functions.force_sub import force_sub_chanel

async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    in_channel = await force_sub_chanel(update,context)
    if in_channel:
        user = await mention(user_id,context)
        photo = img_start
        caption = f"ʜᴇʏ {user} 🌸 ᴛʜɪꜱ ɪꜱ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜꜱɪᴄ ꜰɪɴᴅᴇʀ ʙᴏᴛ, ᴋᴇʏᴡᴏʀᴅ ꜱᴇᴀʀᴄʜᴇʀꜱ & ᴀʟꜱᴏ ᴠᴏɪᴄᴇ ꜱᴇᴀʀᴄʜᴇʀꜱ ꜱᴜᴘᴘᴏʀᴛᴇᴅ 🌷"
        inline_keyboard = [
            [InlineKeyboardButton('⭕ 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 ⭕', url=f"https://t.me/Musicx_lk"),InlineKeyboardButton('✨️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ✨️', url=f"https://t.me/nimsar_a")],
            [InlineKeyboardButton('🌸 ᴀᴅᴅ ᴍᴇ ʙᴇᴀᴜᴛʏ 🌸', url=f"http://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton('🌼 ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ 🌼', url=f"https://t.me/sinhalafilx")]
                ]
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
        await update.message.reply_photo(caption=caption,photo=photo,reply_markup=reply_markup,parse_mode='Markdown')
