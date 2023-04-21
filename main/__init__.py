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
SESSION = "AQAF8rR1HPec2DaaIRCwXwVXFKq0cqf8_l9qvH2DGoPCRY4154XqXbM1gFn_C2Vvlku7IeziYDBgrbWppYOHyKLXuQblzvF-NVq0hRH6liuGgvtCEj-mm8GFMu2zkrphajZqqmZOL4s36Qr6_ZnMaWughVTkPiDcEIaHZKSXI5gVukZsyCTCr6-EWT3Zz76cpV4yw5avu87l57TXDJn4cDvW3rqMGpP2UoP8C3kPHyW7c9Fvz19doKNyU4meSD4dDiFGQshBZvluUoZ73n7s1A7QrLYa1F3JGLDmy4SxenZh-PiUDQXeq14xyBixCWlnbDpoqncxFqBt447f3zOklYfdVT2negA"
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
