#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9774346
API_HASH = "a92aed7d74654a563af4b07efbcd88e9"
BOT_TOKEN = "5885677035:AAFFwI52ayU947kQvCmOBnvuj03AVOy208s"
SESSION = "BQBo5zeXtdzT9knAGi_fcTs1a0NpX2DrDc00VgOFNRBcHns7h_lE2J2hXm_vbdVRLTYwBbcvYcAIfGOJo9ptLIq5agCX9tBx4riYSD8nj-R4HjUsbzh0gg0oy4FZNZjyB7pyVIYIC5M1HfoRBfkLMpFVuEMmbYuy2yNqO_awIIFSomsxZN0dE9IJERFacy8PtdvuVgoQvnOQ7BEL4UtyFDMgs6XRW51VqCxNAYVPZm07vtQUsLiDOa4KgE1kOxHUzfU22h5-C62QBEYthWkPMErQ1iHQCwAybJqxQ9G_KmlETAVZw6bQXB0tIQS0U6i0cYFsFVjroIC0sxgyj4R4BSdYNhgG9gA"
FORCESUB = "contentbot13"
AUTH = 907544310

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
