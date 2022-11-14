from dowloader import *
from aiogram import *
from config import *
from pytube import YouTube

bot = Bot('5554069469:AAFbLV81retIaVNoweQKVTN9a40rmFy1KOk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Привет! Я бот для загрузки видео с YouTube.\n""Просто пришлите мне ссылку на видео")


@dp.message_handler()
async def get_link(message: types.Message):
    chat_id = message.chat.id
    link = message.text
    if link.__contains__('youtube.com') or link.__contains__('youtu.be'):
        video = YouTube(link)
        await bot.send_message(chat_id, f'Запуск загрузки видео [{video.title}] из канала [{video.author}]')
        await download(link, message, bot)
    else:
        await bot.send_message(chat_id, "Не могу распознать ваш URL, пожалуйста, пришлите мне ссылку с Youtube")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)