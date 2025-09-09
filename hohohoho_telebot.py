import telebot
import random, os
import lotoc

bot = telebot.TeleBot(os.environ['token'])


@bot.message_handler(commands = ["comand1"])
def commanda(message):
    bot.send_message(chat_id = message.chat.id , text = 'Я рад вас снова видеть')

@bot.message_handler(commands = ["photo"])
def commanda_photo(message):
    bot.send_photo(chat_id = message.chat.id , photo = open('//FILESRV.kvantorium62.local/ProfilesIT$/i.koshevarov/Desktop/Новая папка/handler.png', 'rb'))
    bot.send_photo(chat_id = message.chat.id , photo = 'https://img2.reactor.cc/pics/post/anon-\%D0\%9A\%D0\%B0\%D1\%80\%D1\%82\%D0\%B8\%D0\%BD\%D0\%BA\%D0\%B0-2191131.jpeg')
    bot.send_photo(chat_id = message.chat.id , photo = 'https://img2.reactor.cc/pics/post/anon-\%D0\%9A\%D0\%B0\%D1\%80\%D1\%82\%D0\%B8\%D0\%BD\%D0\%BA\%D0\%B0-2191131.jpeg')
    
@bot.message_handler(commands = ["animation"])
def commanda_animation(message):
    bot.send_animation(chat_id = message.chat.id , animation = 'AAMCAgADGQEAA0JlDEUshehbd7QzdpyNHSAP8nX02wACSjgAAnSkYUh0Efhar9EOUwEAB20AAzAE')
    bot.send_animation(chat_id = message.chat.id , animation = 'https://99px.ru/sstorage/86/2023/09/mid_42056_960976.jpg')
    bot.send_animation(chat_id = message.chat.id , animation = open('//FILESRV.kvantorium62.local/ProfilesIT$/i.koshevarov/Desktop/Новая папка/image_861609231039315617629.png', 'rb'))


@bot.message_handler(commands = ["video"])
def commanda_video(message):
    bot.send_video(chat_id = message.chat.id , video = 'AAMCAgADGQEAA0hlDEr7xa1CNQYCcJmvNmJqHc3_zQACwzgAAnSkYUhurURqPlHjKwEAB20AAzAE')
    bot.send_video(chat_id = message.chat.id , video = 'https://youtu.be/OYUrzEbhRyw')
    bot.send_video(chat_id = message.chat.id , video = open('//FILESRV.kvantorium62.local/ProfilesIT$/i.koshevarov/Downloads'))

'''list = ["Да","абонемент","амбулатория","анекдот","аплодисменты","аквариум","багаж","безукоризненный","гореть","гигиена","греметь","иллюзия","катастрофа","магистраль","равнина"]
@bot.message_handler(commands = ["poll"])
def commanda_poll(message):
    bot.send_poll(message.chat.id, 'Какая сейчас погода?', ["list"]) 
print(random.sample(range("Да", "равнина"), 1))'''
    

@bot.message_handler(commands = ["sticker"])
def commanda(message):
    bot.send_sticker(chat_id = message.chat.id , sticker = 'CAACAgIAAxkBAANeZRWIo_eatcUH1GWG8ueSrg2j7gsAAmUAA2WiAyy60PaLewaeyjAE')
  
@bot.message_handler(commands = ["Location"])
def commanda_Location(message):
    bot.send_location(chat_id = message.chat.id ,  latitude=54.62762435770551, longitude= 39.715745952665166)


@bot.message_handler(commands = ["voice"])
def commanda_voice(message):
    bot.send_voice(chat_id = message.chat.id , voice = 'AwACAgIAAxkBAAOZZR6_opO5yM7tEV98dva7wQHz79gAAvk6AALXe_lI7LNogGryVIgwBA')
  
@bot.message_handler(commands = ["loto"])
def loto_game(message):
  mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
  text = lotoc.loto()
  bot.send_message(chat_id = message.chat.id, text = f' {mention}, текущий бочонок {text}',reply_to_message_id = message.message_id, parse_mode="HTML")
  
@dp.message(Command("knopki"))
async def cmd_knopki(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

from aiogram import F

@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")




bot.polling(non_stop = True, interval = 0)
