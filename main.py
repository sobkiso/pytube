import os, wget
from pyrogram import Client, filters, idle
from pytube import Playlist  

app = Client(
  "playlists",
  16596628, "421764a823ee2dff786d413aea09959f",
  bot_token="6613026282:AAGiw-mA8x63HubOXLG2AxtTBH8-lsb0kBY"
  )

@app.on_message(filters.command("start") & filters.private)
async def start_(app, message):
     await message.reply(
       "Hello {}\n• I'm YouTube playlists downloader\n• Just send playlist link".format(message.from_user.mention)
     )
     
     
@app.on_message(filters.command("video") & filters.private)
async def download (app,message):
       link = message.text.split(None, 1)[1]
       pl = Playlist(link)
       msg = await message.reply("Downloading ...")
       for video in pl.videos:
           vid = video.streams.get_highest_resolution().download()
           ph = wget.download(video.thumbnail_url)
           await message.reply_video(vid, caption=video.title, thumb=ph, duration=video.length)
           os.remove(vid)
           os.remove(ph)
       await msg.delete()
       
       
@app.on_message(filters.command("audio") & filters.private)
async def download2 (app,message):
       link = message.text.split(None, 1)[1]
       pl = Playlist(link)
       msg = await message.reply("Downloading ...")
       for video in pl.videos:
           aud = video.streams.get_audio_only().download()
           os.rename(aud, aud.replace('.mp4', '.mp3'))
           ph = wget.download(video.thumbnail_url)
           await message.reply_audio(aud.replace('.mp4', '.mp3'), caption=video.title, thumb=ph, duration=video.length, performer=video.author)
           os.remove(aud.replace('.mp4', '.mp3'))
           os.remove(ph)
       await msg.delete()
    
app.start()
print("♾️")
idle()
