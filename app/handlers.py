from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as keyboards

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Рады приветствовать в Telegram - bot приложения Pillsie!', reply_markup=keyboards.main)
    await message.reply('Чем мы можем помочь?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нужна помощь?')

@router.message(F.text == 'Задать вопрос ❓')
async def questions(message: Message):
    await message.answer('Пожалуйста выберите категорию вопроса', reply_markup=keyboards.questions)

@router.message(F.text == 'Сообщить о проблеме 👾')
async def answers(message: Message):
    await message.answer('Пожалуйста сообщите с какой проблемой вы столкнулись при использовании нашего приложения.\nМы'
                         ' с удовольствием выслушаем вас и постараемся помочь 😊')

@router.message(F.text == 'Контакты 📩')
async def contacts(message: Message):
    await message.answer('Выбрать специалиста', reply_markup=keyboards.about_me_and_ksusha)

@router.message(F.text == 'О нас 💊')
async def about(message: Message):
    await message.answer('Мы – молодой стартап, рожденный в страсти к инновациям и креативу.'
                         '\nНаша команда, состоящая из разработчика и креативного дизайнера,'
                         ' ежедневно ищет новые решения для улучшения жизни людей.\nРады представить вам наше бесплатное'
                         'приложение Pillsie! ')
