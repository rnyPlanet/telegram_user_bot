from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.2)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.2)

        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while (perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")


@app.on_message(filters.command("pidor", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    orig_text = msg.text.split(".pidor ", maxsplit=1)[1]
    text = orig_text

    while (perc < 100):
        try:
            text = "Обнаружение пидораса... " + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(5, 10)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit(f"🟢 Пидорас обнаружен! {orig_text}")
    sleep(3)




REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)


@app.on_message(filters.command("un", prefixes="."))
def unread_chat(app, message):
    message.delete()
    app.send(
        functions.messages.MarkDialogUnread(
            peer=app.resolve_peer(message.chat.id), unread=True
        )
    )

app.run()