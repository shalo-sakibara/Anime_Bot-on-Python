from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Что нового?'),
        KeyboardButton(text='Рассылка по предпочтениям')
    ]
],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите действие из списка",
    selective=True
)

links_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="KANSAI"),
        KeyboardButton(text="AniLibria"),
        KeyboardButton(text="2x2")],
    [
        KeyboardButton(text="Студийная Банда"),
        KeyboardButton(text="AniDUB"),
        KeyboardButton(text="AniMedia")
    ],
    [KeyboardButton(text="Назад")]
],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите действие из списка",
    selective=True
)
