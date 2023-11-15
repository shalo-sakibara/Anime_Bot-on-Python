# Импортируем фрейворк aiogramm
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import asyncio
# Импорт вспомогательных библиотек
import pars_animeGo
import data_bot
import keybords
import data_base_service
import datetime

"""Переменные"""
old_arr_anime = str()
"""Инициализация бота"""
bot = Bot(token=data_bot.Token)
dp = Dispatcher(bot=bot)


"""Команда start"""


@dp.message(Command("start"))
async def start(message: Message):
    await message.reply(f"Привет, {message.from_user.first_name}! \nЯ Аниме Бот. Я буду уведомлять тебя о выходе новых серий аниме", reply_markup=keybords.main_keyboard)

"""Функция получения списка аниме с сайта"""


def spisok_anime(mass):
    if mass != "arr":
        text = str()
        for name_anime in pars_animeGo.new_anime_from_AnimeGo():
            if mass in name_anime.split(" "):
                text += f"{' '.join(name_anime.split(' '))}\n"
            if mass == None:
                text += f"{' '.join(name_anime.split(' '))}\n"
        return text
    else:
        return pars_animeGo.new_anime_from_AnimeGo()


@dp.message(F.text.lower() == "что нового?")
async def new(message: Message):
    global old_arr_anime
    new_spisok_anime = spisok_anime(mass=None)
    if old_arr_anime != new_spisok_anime:
        try:
            await message.reply(f"Появились новые серии аниме", reply_markup=keybords.links_kb)
            await message.answer(new_spisok_anime.replace(old_arr_anime, ""))
            old_arr_anime = new_spisok_anime
        except:
            await message.answer(f"Ошибка на строне сервера, слишком длинный список аниме.\nА пока посмотрите в нужных озвучках (Выбор в меню снизу).")

    else:
        await message.reply(f"Новые серии не появились", reply_markup=keybords.links_kb)


async def search_message(all_anime, id_user: int):
    all_anime = "\n".join(all_anime).replace(old_arr_anime, "")
    if len(all_anime) > 0:
        users = data_base_service.admin_read_json()
        mail = str()
        user_arr = users[str(id_user)]
        for anime_from_all in all_anime:
            if anime_from_all.split(" ")[0] in user_arr:
                mail += f"{anime_from_all}\n"
        if len(mail) > 0:
            await bot.send_message(chat_id=id_user, text=f'Вышли новые серии ваших любимых аниме: \n  {mail}')


async def scheduled_messages(user: int):
    while True:
        current_datetime = datetime.datetime.now()
        current_hour = current_datetime.hour
        current_minute = current_datetime.minute
        if (current_hour == 12 and current_minute == 0) or (current_hour == 18 and current_minute == 0) or (current_hour == 6 and current_minute == 0):
            await search_message(id_user=user, all_anime=spisok_anime(mass="arr"))
        await asyncio.sleep(60)


@dp.message(Command("mailing"))
async def maill(message: Message, command: CommandObject):
    try:
        user_anime = command.args
        user_anime = command.args.split("\ ")
        user_id = str(message.from_user.id)
        await message.answer(text=data_base_service.add_key_value_to_json(key=user_id, value=user_anime))
        await scheduled_messages(user=message.from_user.id)
    except:
        await message.answer('Напишите сообщение правильно. Пример сообщения:\n/mailing Берсерк\ Клинок, рассекающий демонов: Квартал красных фонарей\ Миги и Дали')


@dp.message()
async def echo(message: Message):
    mess = message.text
    if mess == "Рассылка по предпочтениям":
        try:
            await message.answer('На пишите /mailing и точные названия аниме через "\ " (одним сообщением). Не более трёх разных аниме')
        except:
            await message.answer("Что-то не так :(")
    if mess == "AniLibria":
        try:
            await message.answer("Все в озвучке AniLibria.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет.")
    if mess == "2x2":
        try:
            await message.answer("Все в озвучке 2x2.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет.")
    if mess == "KANSAI":
        try:
            await message.answer("Все в озвучке KANSAI.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет.")
    if mess == "Студийная Банда":
        try:
            await message.answer("Все в озвучке Студийная Банда.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет")
    if mess == "AniDUB":
        try:
            await message.answer("Все в озвучке AniDUB.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет.")
    if mess == "AniMedia":
        try:
            await message.answer("Все в озвучке AniMedia.")
            await message.answer(spisok_anime(mass=mess))
        except:
            await message.answer("Такой озвучки сегодня нет.")
    if mess == "Назад":
        await message.answer("Вы вернулись назад", reply_markup=keybords.main_keyboard)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
