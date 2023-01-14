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
SESSION = "AQBlWb68E8cPQOzEFhXW_feJQwMW0Z9u9ibIDC5gLhp1Pg5Ukyjfq72ei8X-5-5KyZ7UaM4plxbJbq4g1ijTWxMOfmU8Nts9NPPl-5wA4N_kRkrUoKJL9TMrtQ4QQY8RNH-8_QHW6XHtLLZeFFQU-1pWAtlB-o5poDZko52HPHWhr3O316Dvp67KQDziIu8aGi0b3VFLxGNIytrm71_lUo2WQnJrePvz7Sjvt1poi37H53KPV_Z2LprqNbBhL1Eu1RNst2-m4UeI5Sli5Z5OXxSrefVBmVYdswPVohITrwQR-WXAqr_XrvHvySgNh1kzylO4JHyVwyV5k2TiG9PpFJjTAAAAAUZCL70A"
FORCESUB = "FwbDuniaVirtual"
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
