import aiogram
№import keyboard
#keyboard
button1 = aiogram.keyboard_button.KeyboardButton('help')
button2 = aiogram.keyboard_button.KeyboardButton('loto')
button3 = aiogram.keyboard_button.KeyboardButton('animation')
button4 = aiogram.keyboard_button.KeyboardButton('btn')



markup1 = aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add (button2).add(button3)
markup2 = aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2, button3,button4)

inline_btn_1 = aiogram.types.reply_keyboard_Button.InlineKeyboardButton('Кнпк')

