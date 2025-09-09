from PIL import Image, ImageFont, ImageDraw
from random import *
import random, os
from aiogram import Bot, Dispatcher, Router, types
#from aiogram.enums import ParseModee
from aiogram.filters import Command
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
import lotoc
from aiogram import F
from aiogram.types import InputFile
filename = 'Cert_Magistr-PHP.jpg'
with Image.open(filename) as img:
    img.load()

hexcode = '0123456789abcdef'
print(img.size)
cropped_img = img.crop((265,290,818,769))
print(cropped_img.size)
low_res_img = img.resize((img.width//4,img.height//4))



font = ImageFont.truetype('Soledago_Regular.ttf', size=50)
color = '#'+choice(hexcode)+choice(hexcode)+choice(hexcode)+choice(hexcode)+choice(hexcode)+choice(hexcode)
im_draw = ImageDraw.Draw(img)
im_draw.text((400,400), 'ЭТО СЕРТИФИКАТ', font=font, fil = color) 
img.save('moi_certificat.jpg')
with Image.open('Cert_Magistr-PHP.jpg') as img2:
    img2.load()
img2.show()

@dp.message_handler(state= Name)
async def get_picture(message: aiogram.types.Message, state: FSMContext):
  async with state.proxy() as proxy:
    Name.name_text = message.text
    await state.finish()
  im = Image.open('Cert_Magistr-PHP.jpg')
  draw = ImageDraw.Draw(im)
  fnt = ImageFont.truetype("Soledago.ttf", 40)
  draw.text((50,50), Name.name_text, font = fnt, align='center')
  im.save('moi_certificat.jpg.png')
  photo = open('moi_certificat.jpg','rb')
  await bot.send_photo(message.chat.id, photo = photo)