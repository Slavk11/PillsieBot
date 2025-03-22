from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Задать вопрос ❓')],
                                     [KeyboardButton(text='Сообщить о проблеме 👾')],
                                     [KeyboardButton(text='Контакты 📩'),
                                     KeyboardButton(text='О нас 💊')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

questions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вопрос о приложении', callback_data= 'аbout-app')],
    [InlineKeyboardButton(text='Безопасность', callback_data='s')],
    [InlineKeyboardButton(text='Хранение данных', url='https://support.apple.com/ru-ru/guide/security/sec35dd877d0/web')
]
])

about_me_and_ksusha = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(text='Дизайн 🩵🩷🤍🩷🩵 О Ксюше ', url='https://www.behance.net/kertender'),
    InlineKeyboardButton(text='О Разработке 💻', url='https://github.com/Slavk11'),
    ]
])