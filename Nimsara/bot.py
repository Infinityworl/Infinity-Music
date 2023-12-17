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



# if message.chat.type != "private":
#         st =await message.reply_sticker(sticker=st_start)
#         st_id = st.id
#         await asyncio.sleep(3)
#         await bot.send_message(
#             message.chat.id,
#             text = START_TEXT.format(message.from_user.mention),
#             reply_markup = START_BUTTON)
#         await bot.delete_messages(message.chat.id, [st_id])
#         return await add_served_chat(message.chat.id) 
@bot.on_message(filters.command("start"))
async def start(_, message):
    if message.chat.type != "private":
        st =await message.reply_sticker(sticker=st_start)
        st_id = st.id
        await asyncio.sleep(3)
        try:
            await bot.send_photo(
                message.from_user.id,
                'https://i.ibb.co/Bcx5564/image.png',
                caption = START_TEXT.format(message.from_user.mention),
                reply_markup = START_BUTTON)
        except Exception as e:
            await message.reply_text(f"**⚠️Unexpected Error⚠️**\n\n`{str(e)}`")
        await bot.delete_messages(message.chat.id, [st_id])
        return await add_served_chat(message.chat.id) 
    else:
        await bot.send_photo(
            photo='https://i.ibb.co/Bcx5564/image.png',
            chat_id=message.from_user.id,
            caption = START_TEXT.format(message.from_user.mention),
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
                                    InlineKeyboardButton('Request Channel' , url='https://t.me/+eu7q3udOdA04YjM1'),
                                    InlineKeyboardButton('Pinned Message' , url='https://t.me/c/2062161170/2')
                            ]]
                            ))
    await bot.send_message(REQ_ARIA, text=f"**#New_Request\n\n👤Requester** - {message.from_user.mention}(`{message.from_user.id}`)\n**💬Chat** - {message.chat.title}(`{message.chat.id}`)\n**📨Message** - {req[1]}", reply_markup=REQ_BTNS)
    await message.reply_text(f"**{message.from_user.mention} ඔයාගේ ඉල්ලිම අප වෙත ලැබි ඇත 🗒**\n#Requested :\n`{req[1]}`",
         reply_markup=(InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton('👁‍🗨 ඉල්ලිම බලන්න 👁‍🗨' , url='https://t.me/+eu7q3udOdA04YjM1'),
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

🍁 **ᴅᴜʀᴀᴛɪᴏɴ:** {}
🌸 **ᴄʜᴀɴɴᴇʟ:** [{}]({})
⭕ **ᴠɪᴇᴡꜱ:** `{}` 

🧑‍🎤 **Requester:** {}
🔥 **Uploaded By**: [ɪɴꜰɪɴɪᴛʏ](https://t.me/nimsar_a)**

  **[0.0──ㅇＦｅｅｌ───ㅇ 0.1](https://t.me/sinhalafilx)**
  **[ˡᶦᵏᵉ   ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ    ˢʰᵃʳᵉ](https://t.me/sinhalafilx)**
"""


CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Nimsar_a")]])


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


async def downloadsong(m,st, message, vid_id, title, duration, performer, views):
    try:
        m = await m.edit(text=f"🌼 **𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕚𝕟𝕘 𝕐𝕠𝕦𝕣 𝕄𝕦𝕤𝕚𝕔**",
                         reply_markup=InlineKeyboardMarkup(
                             [[InlineKeyboardButton("🌼 0:00 ──◁ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ▷── 0.00...", callback_data="progress")]]))
        await bot.delete_messages(message.chat.id, [st.id])
        st2 = await message.reply_sticker(sticker=st_downloading)

        link = YouTube(f"https://youtu.be/{vid_id}")
        thumbloc = link.title + "thumb"
        thumb = requests.get(link.thumbnail_url, allow_redirects=True)
        open(thumbloc, 'wb').write(thumb.content)

        # Get the audio stream with 320kbps
        songlink = link.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        down = songlink.download()
        # Download the audio
        first, last = os.path.splitext(down)
        # Rename the file to .mp3
        song = first + '.mp3'
        os.rename(down, song)

        st3 = await message.reply_sticker(sticker=st_uploading)
        await st2.delete()
        m = await m.edit(text="🌸 **𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐒𝐞𝐯𝐞𝐫**",
                         reply_markup=InlineKeyboardMarkup(
                             [[InlineKeyboardButton("🌸 🅄🄿🄻🄾🄰🄳🄸🄽🄶 🅃🄴🄻🄴🄶🅁🄰🄼...", callback_data="progress")]]))

        await message.reply_audio(song,
                                  caption=CAPTION_TEXT.format(title, duration, performer,
                                                              f"https://youtu.be/{vid_id}", views,
                                                              message.from_user.mention if message.from_user else "Anonymous Admin"),
                                  thumb=thumbloc,
                                  reply_markup=CAPTION_BTN)
        
        await m.delete()
        await st3.delete()
        st4 = await message.reply_sticker(sticker=st_done)
        await asyncio.sleep(3)
        await st4.delete()

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
            return await message.reply_text("𝙶𝚒𝚟𝚎 𝚖𝚎 𝚜𝚘𝚗𝚐 𝚗𝚊𝚖𝚎 𝚋𝚛𝚘𝚝𝚑𝚎𝚛  ⚠️")
    st =await message.reply_sticker(sticker=st_loading)
    m = await message.reply_text("⚡ ꜱᴇᴀʀᴄʜɪɴɢ ʏᴏᴜʀ ʀᴇꜱᴜʟᴛꜱ ...")
    name = message.text.split(None, 1)[1]
    results = YoutubeSearch(name, max_results=1).to_dict()
    title = results[0]["title"]
    vid_id = results[0]["id"]
    duration = results[0]["duration"]
    performer = results[0]["channel"]
    views = results[0]["views"]
    await downloadsong(m,st, message, vid_id, title, duration, performer, views)
   except Exception as e:
      await m.edit(f"**Nothing Found** {message.from_user.mention}")





#🏷 **Title:** [{title}]({link})

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
