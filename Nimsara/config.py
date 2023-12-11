import re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

APPID = "24008761"
APIHASH = "c6bb29db832216220e1234b163233cec"
BOTTOKEN = "6578576818:AAHZul8aG55O6AOozuNHuFTB3POMMtGjjSQ"

MONGO_URI = "mongodb+srv://nimsara:nimsara@cluster0.mgn7qqv.mongodb.net/?retryWrites=true&w=majority"
BOT_USERNAME = "Nimsaraxbot"

id_pattern = re.compile(r'^.\d+$')
REQ_ARIA= int(-1001885188788)
CHAT = [int(ch) if id_pattern.search(ch) else ch for ch in '-1001879497983 -1001396114028 -1001375013540'.split()]
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in '1949037588 1746346543 6363073939'.split()]

START_TEXT = "Hey {} ᴅᴇᴀʀ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍᴜꜱɪᴄ ᴡᴏʀʟᴅ ☘️"
START_BUTTON = InlineKeyboardMarkup(
                            [[
                                    InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ' , url="https://t.me/Nimsar_a"),
                                    InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ' , url="https://t.me/infinityx_lk")
                            ]]
                            )

st_start = 'CAACAgIAAxkBAAEoL9Nldq4aMAUhIoKg2lMSQ6OfZERpCgACAQEAAladvQoivp8OuMLmNDME'
st_loading ='CAACAgUAAxkBAAEoL-dldrFPzxcocixG6zvPqSWGNjhtfAACmgADyJRkFCxl4eFc7yVqMwQ'
st_downloading = 'CAACAgUAAxkBAAEoMAlldrwZJuyZvCYdaqdPIEKgMAvFEwACnQADyJRkFKod8wepbhc6MwQ'
st_uploading = 'CAACAgUAAxkBAAEoMCNldr65MpR0gSM08Dc5UHUJv9Is1gACpQADyJRkFHhDhV4BRbZGMwQ'
st_done= 'CAACAgUAAxkBAAEoL_9ldroNVKslyAv7kU28qs2aF3j7JwACpAADyJRkFIBDD5aPWWn6MwQ'
