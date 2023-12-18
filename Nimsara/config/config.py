import re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

APPID = "24008761"
APIHASH = "c6bb29db832216220e1234b163233cec"
BOTTOKEN = "6578576818:AAEBfTyvp6u_oCXQ0d_kbslNg0SEFkgQvtA"

MONGO_URI = "mongodb+srv://nimsara:nimsara@cluster0.mgn7qqv.mongodb.net/?retryWrites=true&w=majority"
BOT_USERNAME = "Nimsaraxbot"

id_pattern = re.compile(r'^.\d+$')
REQ_ARIA= int(-1002062161170)
CHAT = [int(ch) if id_pattern.search(ch) else ch for ch in '-1001885188788'.split()]
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in '1949037588'.split()]

START_TEXT = "Hey {} 🌸 ᴛʜɪꜱ ɪꜱ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜꜱɪᴄ ꜰɪɴᴅᴇʀ ʙᴏᴛ, ᴋᴇʏᴡᴏʀᴅ ꜱᴇᴀʀᴄʜᴇʀꜱ & ᴀʟꜱᴏ ᴠᴏɪᴄᴇ ꜱᴇᴀʀᴄʜᴇʀꜱ ꜱᴜᴘᴘᴏʀᴛᴇᴅ 🌷 "
START_BUTTON = InlineKeyboardMarkup(
                [
                 [
                 InlineKeyboardButton("⭕ 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 ⭕", url='https://t.me/Musicx_lk'),
                 InlineKeyboardButton("✨️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ✨️", url='https://t.me/nimsar_a')
                 ],
                 [
                  InlineKeyboardButton("🌸 ᴀᴅᴅ ᴍᴇ ʙᴇᴀᴜᴛʏ 🌸", url='https://t.me/Nimsaraxbot?startgroup=true'),
                 ],
                 [
                  InlineKeyboardButton("🌼 ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ 🌼", url='https://t.me/sinhalafilx'),
                 ],
                ]
)
img_start = "https://i.ibb.co/3zvHYPh/photo-2023-08-30-22-45-44.jpg"
st_start = 'CAACAgIAAxkBAAEoL9Nldq4aMAUhIoKg2lMSQ6OfZERpCgACAQEAAladvQoivp8OuMLmNDME'
st_loading ='CAACAgIAAx0CbhArBwACGAplfcuyOI9ys_e8Tqx9iPyhVD4GCgAC6BYAAv2LEEra9hZZ9LdRQB4E'
st_downloading = 'CAACAgEAAxkBAAEoMFNldsx2wvR-Lfgn--vsCqFpdoCl3QACBAYAAm5PKEe-rP_0rU2xITME'
st_uploading = 'CAACAgUAAxkBAAEoMCNldr65MpR0gSM08Dc5UHUJv9Is1gACpQADyJRkFHhDhV4BRbZGMwQ'
st_done= 'CAACAgUAAxkBAAEoL_9ldroNVKslyAv7kU28qs2aF3j7JwACpAADyJRkFIBDD5aPWWn6MwQ'
