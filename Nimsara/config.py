import re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

APPID = "24008761"
APIHASH = "6312103562:AAHS1e2EN_rmaqQSpldluqmHKydranKT3OQ"
BOTTOKEN = "6578576818:AAHZul8aG55O6AOozuNHuFTB3POMMtGjjSQ"

MONGO_URI = "mongodb+srv://klgeethika:<klgeethika>@cluster0.u3oatsp.mongodb.net/?retryWrites=true&w=majority"
BOT_USERNAME = "Nimsaraxbot"

id_pattern = re.compile(r'^.\d+$')
REQ_ARIA= int(-1001693331508)
CHAT = [int(ch) if id_pattern.search(ch) else ch for ch in '-1001879497983 -1001396114028 -1001375013540'.split()]
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in '1361226141 1746346543 6363073939'.split()]

START_TEXT = "Hey {} I'm ALive"
START_BUTTON = InlineKeyboardMarkup(
                            [[
                                    InlineKeyboardButton('BUTTON1' , url="https://t.me/Nimsaraxbot"),
                                    InlineKeyboardButton('BUTTON2' , url="https://t.me/infinityx_lk")
                            ]]
                            )
