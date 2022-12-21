#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 10802796
API_HASH = "a92aed7d74654a563af4b07efbcd88e9"
BOT_TOKEN = "5885677035:AAFFwI52ayU947kQvCmOBnvuj03AVOy208s"
SESSION = "AQC25_mUkrYj2F3Jt4vAE_eYtHA8R12OYXn0nVD4iJJ8OAEcRvZXKxUT0FfDTcG5ZahEcSJpZbEC7Lqyku9gY1y7VAKZUMR1NhXZQ_68K4-XFd_f1kHo_9mgqiTkJ-NFLlkXc-_lI_RuCWKCK43BMwEaX8wpRfHK7IhrUeeeh16_eJvwmGkjq2GvZoktWu9xgUe_p8W_vWs9gC98V2xOeV35ObMgvlWGyRoAWu_Hh6CHtYewBqGe8zO07Buup4kJm6jQIOtVsNou53r4BtAQFPDt2-KqTGc7J2mdjHUKr8gzrvr1LhZhp7JhEmEZJBqPej01J4dZDmnE84eO1XVuOjAAAAAUZCL70A"
FORCESUB = "contentbot13"
AUTH = 5473710013

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
