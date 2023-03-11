#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "10802796"
API_HASH = "191107910c6fbc576bff320d6f4e8d12"
BOT_TOKEN = "5885677035:AAFFwI52ayU947kQvCmOBnvuj03AVOy208s"
SESSION = "AQAhIHQABm2P9HPxIg9tN_klVRi_L785ST7ZIKAnESDPaL9HE2kMHrBA0BHAWsyC0gdcVnsaaAEpds7bf2Re2d6twF0Q5kDvWm1glMsN0IWxh0F5HyeXAW1qHf-cXnMvYDjpDdXKxpERKay1cCeeH89PDH1EUKN4JAcwCoNS02RU0yF0aqxRw3t7URHTwmPEDr1XgZw0r5T7IfWNdBJWozHejwmqSAntzI4umwoqp4W45NeLU4jk9QcA_qgrd8BBD_0to-6Mrt046qsSw1K6llYX6zXzxXk0ZtmUQnUAy54TdjV7cPHKLkV5hB1YptdIJz7UX4TQxjfu9I6q7oO3JHjI4AHwAAAAFGQi-9AA"
FORCESUB = "DuniaVirtualMenfess"
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
