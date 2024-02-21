from telegram import Update, InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes
from youtube_search import YoutubeSearch
from Plugins.help_functions.force_sub import force_sub_chanel
from Plugins.help_functions.mention import mention
from pytube import YouTube
from youtubesearchpython import VideosSearch
from config import *
from .delete_timer import delete_message

import yt_dlp
import requests
import asyncio
import re
import os

async def create_task_for_user(update,context):
    task = asyncio.create_task(get_results(update, context))

async def get_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.edited_message or update.message
    message_id = message.message_id
    user_id = message.from_user.id
    user = await mention(user_id,context)
    in_channel = await force_sub_chanel(update,context)
    if in_channel:
        try: 
            if update.message.text == "/song":
                await message.reply_text("Give a song name brother  ⚠️")
                return 
            else:
                m = await message.reply_text("⚡ ꜱᴇᴀʀᴄʜɪɴɢ ʏᴏᴜʀ ꜱᴏɴɢ ...")
                st =await message.reply_sticker(sticker=st_loading)
                name = message.text.split(None, 1)[1]
                results = YoutubeSearch(name, max_results=10).to_dict()
                info = [{'vid_id': entry['id'], 'title': entry['title']} for entry in results]
                vid_id = [entry['id'] for entry in results]
                keyboard = []
                text = f'{user} , ʜᴇʀᴇ ᴀʀᴇ ᴡʜᴀᴛ ɪ ғᴏᴜɴᴅ'
                b_num = 0
                row = [] 
                for entry in info:
                    b_num = b_num + 1
                    text += f"\n\n{b_num}. {entry['title']}"
                    callback_data = f"{entry['vid_id']} : {user_id}"
                    row.append(InlineKeyboardButton(f'{b_num}', callback_data=callback_data))
                    if b_num % 2 == 0: 
                        keyboard.append(row)
                        row = []
                if row:
                    keyboard.append(row)
                text += "\n\nsᴇʟᴇᴄᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ 👇👇"
                reply_markup = InlineKeyboardMarkup(keyboard)
                await context.bot.delete_message(chat_id=message.chat_id, message_id=st.message_id)
                await context.bot.delete_message(chat_id=message.chat_id, message_id=message_id)
                await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=text ,reply_markup=reply_markup, parse_mode='Markdown')
        except Exception as e:
            try:
                await message.reply_text(text=f"{e}")
                await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=f"**Nothing Found** [{message.from_user.first_name}](tg://user?id={message.from_user.id})" , parse_mode='Markdown')
                await context.bot.delete_message(chat_id=message.chat_id, message_id=st.message_id)
                mid = m.message_id
                task = asyncio.create_task(delete_message(chat_id, mid,10 , context))
            except:
                pass

async def handle_song(update: Update,vid_id,m, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://www.youtube.com/watch?v={vid_id}"
    toDownload = YoutubeSearch(url, max_results=1).to_dict()

    title = toDownload[0]["title"]
    title = title.replace("[", "")
    title = title.replace("]", "")
    duration = toDownload[0]["duration"]
    performer = toDownload[0]["channel"]
    views = toDownload[0]["views"]
    views = views.replace(" views", "")
    
    task = asyncio.create_task(download_song(update,m, vid_id, title, duration, performer, views,context)) 

async def download_song(update, m,vid_id, title, duration, performer, views,context: ContextTypes.DEFAULT_TYPE):
    temp = []
    chat_id = update.effective_chat.id
    message = update.edited_message or update.message
    st =await context.bot.send_sticker(chat_id=chat_id,sticker=st_loading)
    text = """
{}
┬────
├ ● Title : [{}](https://youtube.com/watch?v={})
│ 
├ ● Duration : {}
│
├ ● Channel : {}
│
└ ● Views : {} 
        
    """

    caption_text = """
**{}**

◇───────────────◇

● **ᴅᴜʀᴀᴛɪᴏɴ:** {}
● **ᴄʜᴀɴɴᴇʟ:** [{}](https://youtube.com/watch?v={})
● **ᴠɪᴇᴡꜱ:** `{}` 

◇───────────────◇

◎ **ʀᴇQᴜᴇᴜꜱᴛᴇʀ:** {}
◎ **ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ:** [Moon v2](https://t.me/Nimsaraxbot)**

◇───────────────◇
            **[ʟᴏɢɪᴄ ʟᴀʙ </>](https://t.me/Logic_lab_lk)**
  
  **[ ♡ ㅤ    ❍        ⎙ㅤ   ⌲](https://t.me/sinhalafilx)**
  **[ˡᶦᵏᵉ   ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ    ˢʰᵃʳᵉ](https://t.me/sinhalafilx)**
"""
    downloading = [
        [InlineKeyboardButton('0:00 ──◁ 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕚𝕟𝕘 ▷── 0.00...', callback_data="progress")]
            ]
    download_button=InlineKeyboardMarkup(downloading)
    uploading = [
        [InlineKeyboardButton('0:00 ──◁ 𝕌𝕡𝕝𝕠𝕒𝕕𝕚𝕟𝕘 ▷── 0.00...', callback_data="progress")]
            ]
    upload_button=InlineKeyboardMarkup(uploading)
    
    await context.bot.edit_message_text(chat_id=chat_id, message_id=m, text=text.format("𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕚𝕟𝕘 𝕐𝕠𝕦𝕣 𝕄𝕦𝕤𝕚𝕔",title, vid_id, duration, performer, views), parse_mode='Markdown',reply_markup=download_button,disable_web_page_preview=True)
    try:
        
        st2 = await context.bot.send_sticker(chat_id=chat_id, sticker=st_downloading)
        temp.append(st2.message_id)
        
        await context.bot.delete_message(chat_id=chat_id, message_id=st.message_id)
        # await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text="Downloading..." , parse_mode='Markdown')
        # url = f"https://www.youtube.com/watch?v={vid_id}"
        url = f"https://youtu.be/{vid_id}"
        
        
        words = title.split() 
        file_name = words[0]
        toDownload = YoutubeSearch(url, max_results=1).to_dict()
        suf = toDownload[0]["url_suffix"]
        link = f"https://www.youtube.com{suf}"
        print("URL : ",url)
        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "outtmpl": f"downloads/{title}.mp3",
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
            
        yt = YouTube(link)
        thumbloc = yt.title + "thumb"
        thumb = requests.get(yt.thumbnail_url, allow_redirects=True)
        open(thumbloc, 'wb').write(thumb.content)

        
        st3 = await context.bot.send_sticker(chat_id=chat_id, sticker=st_uploading)
        temp.append(st3.message_id)
        await context.bot.delete_message(chat_id=chat_id, message_id=st2.message_id)
        temp.remove(st2.message_id)
        
        await context.bot.edit_message_text(chat_id=chat_id, message_id=m, text=text.format("𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐒𝐞𝐯𝐞𝐫...",title, vid_id, duration, performer, views), parse_mode='Markdown',reply_markup=upload_button,disable_web_page_preview=True)
        user = f"[{update.effective_user.first_name}](tg://user?id={update.effective_user.id})"
        # format(f"Uploaded By ",title, vid_id, duration, performer, views)
        inline_keyboard = [
        [InlineKeyboardButton('✨️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ✨️', url=f"https://t.me/nimsar_a")],
        [InlineKeyboardButton('🌸 Open in Youtube 🌸', url=f"https://youtube.com/watch?v={vid_id}")]
            ]
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
        # await context.bot.send_video(chat_id=chat_id, video=f"downloads/{file_name}.mp4", caption=caption_text.format(title, duration, performer,vid_id, views,user), parse_mode='Markdown',reply_markup=reply_markup)
        await context.bot.send_audio(chat_id=chat_id, audio=f"downloads/{title}.mp3",thumbnail=thumbloc,performer="ʟᴏɢɪᴄ ʟᴀʙ </>", caption=caption_text.format(title, duration, performer,vid_id, views,user), parse_mode='Markdown',reply_markup=reply_markup)
        await context.bot.delete_message(chat_id=chat_id, message_id=m)
        await context.bot.delete_message(chat_id=chat_id, message_id=st3.message_id)
        temp.remove(st3.message_id)
        
        st4 = await context.bot.send_sticker(chat_id=chat_id, sticker=st_done)
        await asyncio.sleep(3)
        await context.bot.delete_message(chat_id=chat_id, message_id=st4.message_id)
        try:
            os.remove(f"downloads/{title}.mp3")
        except:
            pass
        try:
            os.remove(thumbloc)
        except:
            pass
            

    except Exception as e:
        print(temp)
        await context.bot.edit_message_text(chat_id=chat_id, message_id=m, text=f"Something went wrong \n\n  {e}" , parse_mode='Markdown')
        from __main__ import errors_of_all
        await errors_of_all(update,e,context)
        print(e)
        try:
            for msg in temp:
                await context.bot.delete_message(chat_id=chat_id, message_id=msg)
        except Exception as er:
            print(er)


