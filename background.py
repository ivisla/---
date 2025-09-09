from aiogram import F, html
from flask import Flask
from flask import request
from threading import Thread
import time, os
import requests
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
import aiogram, asyncio
from aiogram import Bot, Dispatcher, Router, types
#from aiogram.enums import ParseModee
from aiogram.filters import Command
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram import F
from aiogram.types import InputFile
#from PIL import Image, ImageFont, ImageDraw
from random import *
from aiogram.utils.markdown import hlink

dp = Dispatcher()
@dp.message(Command('produsestore'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Магнит"),
           types.KeyboardButton(text="Пятёрочка")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "Магнит")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://magnit.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Пятёрочка")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://5ka.ru",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(Command('clothingstore'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="ЦУМ"),
           types.KeyboardButton(text="Lamoda")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "ЦУМ")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.tsum.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Lamoda")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.lamoda.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )
@dp.message(Command('markets'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Ozon"),
           types.KeyboardButton(text="Яндекс Маркет")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "Ozon")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.ozon.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Яндекс Маркет")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://market.yandex.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )
@dp.message(Command('hardwarestore'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="DNS"),
           types.KeyboardButton(text="М.Видео")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "DNS")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.dns-shop.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "М.Видео")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.mvideo.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(Command('communicationstore'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="МегаФон"),
           types.KeyboardButton(text="МТС")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "МегаФон")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.megafon.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "МТС")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.mts.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(Command('bank'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Сбербанк России"),
           types.KeyboardButton(text="Тинькофф")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "Сбербанк России")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "http://www.sberbank.ru/ru/person",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Тинькофф")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.tinkoff.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )


@dp.message(Command('gamestore'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Steam"),
           types.KeyboardButton(text="Epic Games")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите магазин", reply_markup=keyboard)

@dp.message(F.text == "Steam")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://store.steampowered.com/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Epic Games")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://store.epicgames.com/ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\

@dp.message(Command('streamingservice'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Яндекс Музыка"),
           types.KeyboardButton(text="Spotify")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "Яндекс Музыка")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://music.yandex.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Spotify")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://open.spotify.com/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )


@dp.message(Command('onlinecinema'))
async def cmd_knopka(message: types.Message):
  kb = [
         [
           types.KeyboardButton(text="Кинопоиск"),
           types.KeyboardButton(text="Netflix")
         ],
     ]
  keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder= "Это сервис."
        )
  await message.answer("Пожалуйста, выберите сервис", reply_markup=keyboard)

@dp.message(F.text == "Кинопоиск")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://www.kinopoisk.ru/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )

@dp.message(F.text == "Netflix")
async def extract_data(message: types.Message):
    data = {
        "Ссылка": "https://hetflix.online/",
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Я нашёл сервис, который вы выйбрали.\n"
        f"Ссылка: {html.quote(data['Ссылка'])}\n"
    )
async def main():
  bot = Bot('6683459873:AAFJXIa46nnDFDZZVCCGkH8EJZaXOEjvbQE')
  await dp.start_polling(bot)

if __name__ == '__main__':
  asyncio.run(main())