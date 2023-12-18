from telegram import Update, InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes
from youtube_search import YoutubeSearch
from pytube import YouTube
import requests
import asyncio
import re
import os
from config import *

async def handle_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    try: 
        if update.message.text == "/song":
            await message.reply_text("Give a song name brother  ⚠️")
            return 
        else:
            m = await message.reply_text("🔎 Searching ...")
            st =await message.reply_sticker(sticker=st_loading)
            name = message.text.split(None, 1)[1]
            results = YoutubeSearch(name, max_results=1).to_dict()
            title = results[0]["title"]
            title = title.replace("[", "\[")
            # title = title.replace("]", "\]")
            
            vid_id = results[0]["id"]
            duration = results[0]["duration"]
            performer = results[0]["channel"]
            views = results[0]["views"]
            views = views.replace(" views", "")
            # views = re.search(r'\d+', views).group()
            # await downloadsong(m,st, message, vid_id, title, duration, performer, views)
            print(vid_id, title, duration, performer, views)

    except Exception as e:
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=f"**Nothing Found** [{message.from_user.first_name}](tg://user?id={message.from_user.id})" , parse_mode='Markdown')
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st.message_id)
    await download_song(m, st, message, vid_id, title, duration, performer, views,context)
    
temp = []
async def download_song(m, st, message, vid_id, title, duration, performer, views,context: ContextTypes.DEFAULT_TYPE):
    text = """
{}
┬────
├ Title : [{}](https://youtube.com/watch?v={})
│ 
├ Duration : {}
│
├ Channel : {}
│
└ Views : {} 
        
    """

    caption_text = """
**{}**

🍁 **ᴅᴜʀᴀᴛɪᴏɴ:** {}
🌸 **ᴄʜᴀɴɴᴇʟ:** [{}](https://youtube.com/watch?v={})
⭕ **ᴠɪᴇᴡꜱ:** `{}` 

🧑‍🎤 **Requester:** {}
🔥 **Uploaded By**: [ɪɴꜰɪɴɪᴛʏ](https://t.me/nimsar_a)**

  **[0.0──ㅇＦｅｅｌ───ㅇ 0.1](https://t.me/sinhalafilx)**
  **[ˡᶦᵏᵉ   ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ    ˢʰᵃʳᵉ](https://t.me/sinhalafilx)**
"""
    await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=text.format("Downloading...",title, vid_id, duration, performer, views), parse_mode='Markdown',disable_web_page_preview=True)
    try:
        
        st2 = await context.bot.send_sticker(chat_id=message.chat_id, sticker=st_downloading)
        temp.append(st2.message_id)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st.message_id)
        # await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text="Downloading..." , parse_mode='Markdown')
        url = f"https://www.youtube.com/watch?v={vid_id}"
        yt = YouTube(url)
        thumbloc = yt.title + "thumb"
        thumb = requests.get(yt.thumbnail_url, allow_redirects=True)
        open(thumbloc, 'wb').write(thumb.content)
        video = yt.streams.filter(only_audio=True).first()
        down = video.download(skip_existing=True)
        first, last = os.path.splitext(down)
        song = first + '.mp3'
        os.rename(down, song)
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=text.format("Download Completed",title, vid_id, duration, performer, views) , parse_mode='Markdown',disable_web_page_preview=True)
        st3 = await context.bot.send_sticker(chat_id=message.chat_id, sticker=st_uploading)
        temp.append(st3.message_id)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st2.message_id)
        temp.remove(st2.message_id)
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=text.format("Uploading...",title, vid_id, duration, performer, views), parse_mode='Markdown',disable_web_page_preview=True)
        user = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        # format(f"Uploaded By ",title, vid_id, duration, performer, views)
        inline_keyboard = [
        [InlineKeyboardButton('✨️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ✨️', url=f"https://t.me/nimsar_a")],
        [InlineKeyboardButton('🌸 Open in Youtube 🌸', url=f"https://youtube.com/watch?v={vid_id}")]
            ]
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
        await context.bot.send_audio(chat_id=message.chat_id, audio=song,thumbnail=thumbloc, caption=caption_text.format(title, duration, performer,vid_id, views,user), reply_to_message_id=message.message_id, parse_mode='Markdown',reply_markup=reply_markup)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=m.message_id)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st3.message_id)
        temp.remove(st3.message_id)
        
        st4 = await context.bot.send_sticker(chat_id=message.chat_id, sticker=st_done, reply_to_message_id=message.message_id)
        await asyncio.sleep(3)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st4.message_id)
        temp.remove(st4.message_id)
        if os.path.exists(song):
            os.remove(song)
        if os.path.exists(thumbloc):
            os.remove(thumbloc)
    except Exception as e:
        print(e)
        for msg in temp:
            await context.bot.delete_message(chat_id=message.chat_id, message_id=msg)
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=f"Something went wrong \n\n  {e}" , parse_mode='Markdown')
