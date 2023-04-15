#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "27547356"
API_HASH = "9a5fa029f05c61096bf9fe89cc0f8862"
BOT_TOKEN = "5885677035:AAG9k37bonLS95Mv5suqT7joH9H-MRhMMmo"
SESSION = "AQDEBE3iIoEG0bvnzFIPPqcWWCF_FItDiyDgvk0bnoHv4IAM7zna-F56vgbq2bYUgdCnpS6UUMvcJDO75XrzXpOqNYDW0IrJlyZYprAfC8nrRCSSp5cCEQG6kvfF7TgdoYYmg9TRjZTU06mlEnra-WyDN_km3ZAUwVLefu7p_JTkKTz4mqjxsPzM4oDHYjuypIEXksHT5BmvrwZLILEugQxyvxvf9J2flpgdD_c6rkt4Qd9WcuAS9RTZhhqgH7C9cGdOQXxwCfrsu61cnzxG97t_KYovjP73c9kyM-sKGJfzKiB5W3PZvxUBCT9nrI692JQVtlys5r53CS_G_XxU_GpAVT2negA"
FORCESUB = "DuniaVirtualMenfess"
AUTH = 1430103930

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
