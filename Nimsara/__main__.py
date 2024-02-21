from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from pytube.exceptions import AgeRestrictedError, LiveStreamError, VideoPrivate
from youtube_search import YoutubeSearch
from pytube import YouTube
import requests
import asyncio
import re
import os


TOKEN = '6578576818:AAHp0lPAUWNZR4T-onxWFMluFSypBNvxnh0'
BOT_USERNAME = 'Nimsaraxbot'
print('Starting up bot...')

st_loading ='CAACAgUAAxkBAAEoL-dldrFPzxcocixG6zvPqSWGNjhtfAACmgADyJRkFCxl4eFc7yVqMwQ'
st_downloading = 'CAACAgUAAxkBAAEoMAlldrwZJuyZvCYdaqdPIEKgMAvFEwACnQADyJRkFKod8wepbhc6MwQ'
st_uploading = 'CAACAgUAAxkBAAEoMCNldr65MpR0gSM08Dc5UHUJv9Is1gACpQADyJRkFHhDhV4BRbZGMwQ'
st_done= 'CAACAgUAAxkBAAEoL_9ldroNVKslyAv7kU28qs2aF3j7JwACpAADyJRkFIBDD5aPWWn6MwQ'


async def handle_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    try: 
        print(update.message.text)
        if len(update.message.text) < 5:
            await message.reply_text("Give a song name brother  ⚠️")
            return 
        m = await message.reply_text("🔎 Searching ...")
        st =await message.reply_sticker(sticker=st_loading)
        name = message.text.split(None, 1)[1]
        results = YoutubeSearch(name, max_results=1).to_dict()
        title = results[0]["title"]
        vid_id = results[0]["id"]
        duration = results[0]["duration"]
        performer = results[0]["channel"]
        views = results[0]["views"]
        views = re.search(r'\d+', views).group()
        # await downloadsong(m,st, message, vid_id, title, duration, performer, views)
        print(vid_id, title, duration, performer, views)

    except Exception as e:
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=f"**Nothing Found** [{message.from_user.first_name}](tg://user?id={message.from_user.id})" , parse_mode='Markdown')
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
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=text.format("Uploading...",title, vid_id, duration, performer, views), parse_mode='Markdown',disable_web_page_preview=True)

        await context.bot.send_audio(chat_id=message.chat_id, audio=song,thumbnail=thumbloc, caption=text.format(f"Uploaded By [{message.from_user.first_name}](tg://user?id={message.from_user.id})",title, vid_id, duration, performer, views), reply_to_message_id=message.message_id, parse_mode='Markdown')

        await context.bot.delete_message(chat_id=message.chat_id, message_id=m.message_id)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st3.message_id)
        st4 = await context.bot.send_sticker(chat_id=message.chat_id, sticker=st_done, reply_to_message_id=message.message_id)
        await asyncio.sleep(3)
        await context.bot.delete_message(chat_id=message.chat_id, message_id=st4.message_id)
        if os.path.exists(song):
            os.remove(song)
        if os.path.exists(thumbloc):
            os.remove(thumbloc)
    except Exception as e:
        print(e)
        for msg in temp:
            await context.bot.delete_message(chat_id=message.chat_id, message_id=msg)
        await context.bot.edit_message_text(chat_id=message.chat_id, message_id=m.message_id, text=f"Something went wrong \n\n  {e}" , parse_mode='Markdown')


async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')
def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text('Try typing anything, and I will do my best to respond.')



def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('song', handle_song))
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)
