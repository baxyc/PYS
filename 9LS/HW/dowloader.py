import os

from pytube import YouTube


async def download(link, message, bot):
    video = YouTube(link)
    video_props = video.streams.filter(progressive=True, file_extension='mp4')
    video_props.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{video.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{video.title}', 'rb') as file:
        await bot.send_video(message.chat.id, file, caption="это твое видео")
        os.remove(f'{message.chat.id}/{message.chat.id}_{video.title}')