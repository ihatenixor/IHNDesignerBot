from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.dispatcher.filters import Text
 
API_TOKEN = '6115890388:AAGdbk7ff3Aut2Y83qZ3-g-kk4IcPlUBPQQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start') 
async def send_welcome(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Все команды"]
   keyboard.add(*buttons)
   await message.answer("Вас приветствует IHNDesigner Бот.\nЗдесь вы сможете посмотреть наш каталог, а так же заказать одежду!\nЧтобы посмотреть доступные комманды напиши /help или нажмите на кнопку ниже!", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все команды"))
async def send_help(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Контакты", "Заказать", "Каталог"]
   keyboard.add(*buttons)
   await message.answer("Доступные команды:\n/contacts - Наши контакты\n/order - Заказать одежду\n/catalog - Каталог", reply_markup=keyboard)

@dp.message_handler(Text(equals="Вернуться назад"))
async def send_help(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Контакты", "Заказать", "Каталог"]
   keyboard.add(*buttons)
   await message.answer("Доступные команды:\n/contacts - Наши контакты\n/order - Заказать одежду\n/catalog - Каталог", reply_markup=keyboard)

@dp.message_handler(commands=['help']) 
async def send_help(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Контакты", "Заказать", "Каталог"]
   keyboard.add(*buttons)
   await message.answer("Доступные команды:\n/contacts - Наши контакты\n/order - Заказать одежду\n/catalog - Каталог", reply_markup=keyboard)

@dp.message_handler(commands=['contacts']) 
async def send_contacts(message: types.Message):
   await message.answer("Сообщество ВК: https://vk.com/ihndesigns\nКонтактные телефоны: +7(928)320-69-57\nМой Телеграм: @IHNDESIGNER\nТелеграм канал: https://t.me/IHNDESINGS\nEmail: raich.nikolai@yandex.ru")

@dp.message_handler(Text(equals="Контакты"))
async def send_contacts(message: types.Message):
   await message.answer("Сообщество ВК: https://vk.com/ihndesigns\nКонтактные телефоны: +7(928)320-69-57\nМой Телеграм: @IHNDESIGNER\nТелеграм канал: https://t.me/IHNDESINGS\nEmail: raich.nikolai@yandex.ru")

@dp.message_handler(Text(equals="Каталог"))
async def catalog_show(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Майки", "Худи", "Шопперы", "Вернуться назад"]
    keyboard.add(*buttons)
    await message.answer("Наш каталог:\nМайки (8)\nХуди (2)\nШопперы (2)", reply_markup=keyboard)

@dp.message_handler(Text(equals="Назад"))
async def catalog_show(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Майки", "Худи", "Шопперы", "Вернуться назад"]
    keyboard.add(*buttons)
    await message.answer("Наш каталог:\nМайки (8)\nХуди (2)\nШопперы (2)", reply_markup=keyboard)

@dp.message_handler(Text(equals="Майки")) 
async def send_tshirts(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["№1", "№2", "№3", "№4", "№5", "№6", "№7", "№8", "Назад"]
   keyboard.add(*buttons)
   await message.answer("Каталог маек:\n№1. Майка ЖОПА\n№2. Майка Гром среди ясного неба\n№3. Майка Стизус\n№4. Майка Капибара\n№5. Майка Джет\n№6. Майка Family Affair\n№7. Майка Токсик\n№8. Майка Рейна", reply_markup=keyboard)

@dp.message_handler(Text(equals="Худи")) 
async def send_tshirts(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["№1", "№2", "Назад"]
   keyboard.add(*buttons)
   await message.answer("Каталог худи:\n№1. Худи Стизус\n№2. Худи Капибара", reply_markup=keyboard)

@dp.message_handler(Text(equals="Шопперы")) 
async def send_tshirts(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["№1", "№2", "Назад"]
   keyboard.add(*buttons)
   await message.answer("Каталог шопперов:\n№1. Шоппер Стизус\n№2. Шоппер Капибара", reply_markup=keyboard)

@dp.message_handler()
async def unknown(message: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Все команды"]
   keyboard.add(*buttons)
   await message.answer('Простите, но я не понимаю вас! Чтобы узнать список доступных комманд, напишите /help. или посмотрите список команд!', reply_markup=keyboard)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)