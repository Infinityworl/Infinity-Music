import re
import asyncio
from config import *
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from database import (
    add_served_chat,
    add_served_user,
    get_served_chats,
    get_served_users,
    remove_served_chat,
    remove_served_user
)

bot = Client(
    "nimsarabot",
    api_id=APPID,
    api_hash=APIHASH,
    bot_token=BOTTOKEN)

REQ_BTNS = InlineKeyboardMarkup(
                            [[
                                    InlineKeyboardButton('Status' , callback_data='status#Pending...'),
                                    InlineKeyboardButton('Pending 👁‍🗨' , callback_data=f'pending')
                            ]]
                            )

@bot.on_message(filters.command("start"))
async def start(_, message):
    if message.chat.type != "private":
       await bot.send_message(
        message.chat.id,
        text = START_TEXT.format(message.from_user.mention),
        reply_markup = START_BUTTON)
       return await add_served_chat(message.chat.id) 
    else:
        await bot.send_message(
            message.from_user.id,
            text = START_TEXT.format(message.from_user.mention),
            reply_markup = START_BUTTON)
    return await add_served_user(message.from_user.id)

@bot.on_callback_query(filters.regex("pending"))
async def pending(_, query):
        channel_id = query.message.chat.id
        user_id = query.from_user.id
        st = await bot.get_chat_member(channel_id, user_id)
        if (st.status == "administrator") or (user_id in ADMINS):
            return await query.edit_message_reply_markup(InlineKeyboardMarkup(
                                [[
                                    InlineKeyboardButton('Status' , callback_data='status#Done...'),
                                    InlineKeyboardButton('Done✅' , callback_data=f'done#{query.from_user.first_name}')
                                ]]))
        else:
            return await bot.answer_callback_query(query.id, f"This Request is Pending...👁‍🗨", show_alert=False)

@bot.on_callback_query()
async def stats(_, query):
        if query.data.startswith("status"):
            stats = query.data.split("#")
            await bot.answer_callback_query(query.id, f"This Request is {stats[1]}", show_alert=False)
        elif query.data.startswith("done"):
            channel_id = query.message.chat.id
            user_id = query.from_user.id
            done_by = query.data.split("#")
            st = await bot.get_chat_member(channel_id, user_id)
            if (st.status == "administrator") or (user_id in ADMINS):
                return await query.edit_message_reply_markup(InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton('Status' , callback_data='status#Pending...'),
                                    InlineKeyboardButton('Pending 👁‍🗨' , callback_data=f'pending')
                                ], 
                            ]))
            else:
                return await bot.answer_callback_query(query.id, f"This Request Completed By {done_by[1]}✅", show_alert=False)

@bot.on_message(filters.regex("#request") & ~filters.bot & filters.chat(CHAT))
async def request(_, message):
    req = message.text.split("request")
    if len(req[1]) < 2:
            return await message.reply_text("**හරියටම Film Request එකක් දාන්නෙ කොහොමද  දැනගන්න Request channel එකට Join වෙලා pined message එක කියවන්න**",
                                           reply_markup=InlineKeyboardMarkup(
                            [[
                                    InlineKeyboardButton('Request Channel' , url='https://t.me/+_zM-aTIXu-IyMzk1'),
                                    InlineKeyboardButton('Pinned Message' , url='https://t.me/c/1693331508/23')
                            ]]
                            ))
    await bot.send_message(REQ_ARIA, text=f"**#New_Request\n\n👤Requester** - {message.from_user.mention}(`{message.from_user.id}`)\n**💬Chat** - {message.chat.title}(`{message.chat.id}`)\n**📨Message** - {req[1]}", reply_markup=REQ_BTNS)
    await message.reply_text(f"**{message.from_user.mention} Your Request have added To The List 🗒**\n#Requested :\n`{req[1]}`",
         reply_markup=(InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton('👁‍🗨 View Requests 👁‍🗨' , url='https://t.me/+_zM-aTIXu-IyMzk1'),
                                ]
                            ])),
         disable_web_page_preview=True
)


from pytube.exceptions import AgeRestrictedError, LiveStreamError, VideoPrivate
from youtube_search import YoutubeSearch
from pytube import YouTube
import requests
import os

CAPTION_TEXT = """
**{}**

⏳ **Duration:** {}
🔗 **Channel:** [{}]({})
👀 **Views:** `{}` 

👤 **Requester:** {}

**[🤖 Moon v2](https://t.me/Nimsaraxbot)**
||[©️ DEVELOPER](https://t.me/nimsar_a)||
"""

CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("BOT", url="https://t.me/Nimsaraxbot")]])


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


async def downloadsong(m, message, vid_id, title, duration, performer, views):
    try:
        m = await m.edit(text=f"📥 **Upload Started**",
                         reply_markup=InlineKeyboardMarkup(
                             [[InlineKeyboardButton("📥 Downloading...", callback_data="progress")]]))
        link = YouTube(f"https://youtu.be/{vid_id}")
        thumbloc = link.title + "thumb"
        thumb = requests.get(link.thumbnail_url, allow_redirects=True)
        open(thumbloc, 'wb').write(thumb.content)

        # Get the audio stream with 320kbps
        songlink = link.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        # Download the audio
        down = songlink.download()
        # Rename the file to .mp3
        first, last = os.path.splitext(down)
        song = first + '.mp3'
        os.rename(down, song)

        m = await m.edit(text="📥 **Upload Started**",
                         reply_markup=InlineKeyboardMarkup(
                             [[InlineKeyboardButton("📤 Uploading...", callback_data="progress")]]))

        await message.reply_audio(song,
                                  caption=CAPTION_TEXT.format(title, duration, performer,
                                                              f"https://youtu.be/{vid_id}", views,
                                                              message.from_user.mention if message.from_user else "Anonymous Admin"),
                                  thumb=thumbloc,
                                  reply_markup=CAPTION_BTN)
        await m.delete()

        # Clean up the downloaded files
        if os.path.exists(song):
            os.remove(song)
        if os.path.exists(thumbloc):
            os.remove(thumbloc)
    except AgeRestrictedError:
        await m.edit(f"**🍼Hey Baby**,\n`It's Age Restricted\nSo Cannot Download🔞`")
    except LiveStreamError:
        await m.edit(f"**Wait What🧐**\n`I am not a Live streamer👾`")
    except Exception as e:
        await m.edit(f"**⚠️Unexpected Error⚠️**\n\n`{str(e)}`")
        
@bot.on_message(filters.command("song") & ~filters.bot & ~filters.forwarded)
async def songdown(_, message):
   try: 
    if len(message.command) < 2:
            return await message.reply_text("Give a song name ⚠️")
    m = await message.reply_text("🔎 Searching ...")
    name = message.text.split(None, 1)[1]
    results = YoutubeSearch(name, max_results=1).to_dict()
    title = results[0]["title"]
    vid_id = results[0]["id"]
    duration = results[0]["duration"]
    performer = results[0]["channel"]
    views = results[0]["views"]
    await downloadsong(m, message, vid_id, title, duration, performer, views)
   except Exception as e:
      await m.edit(f"**Nothing Found** {message.from_user.mention}")





# """**{title}**

#:---------------------------:
#⏳ **Duration:** `{duration}`
#👀 **Views:** `{views}` 
#🔗 **Watch on** [Youtube]({link})
#:---------------------------:

#🧑‍🎤**Requested By**: {message.from_user.mention()}
#📤 **Uploaded By**: [❦infinity❦](https://t.me/infinityx_lk)**"""

#===============================FOR ADMINS=========================================

@bot.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(_, message: Message):
    m = await message.reply("`processing...")
    name = message.from_user.id
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))

    await m.edit(
        name,
        text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{len(served_users)}`
👥 Groups : `{len(served_chats)}`
🚧 Total users & groups : {int((len(served_chats) + len(served_users)))} """)

async def broadcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@bot.on_message(filters.private & filters.command("bcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users() 
    m = await message.reply_text("Broadcast in progress")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass  
    await m.edit(f"""
Broadcast Completed:.""")
       
print("I'm ALive")
bot.run()
