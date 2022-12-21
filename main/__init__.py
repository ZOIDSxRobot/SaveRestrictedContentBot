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
SESSION = "AQCU_vG3sJtMH_EcakQ3x8Xc8c5ciC9wn-9HNZJpq_LezV_y13fpHVMY6oTjNVNxnsRs2JqIfpCG06RVQQw1eLQ-gueof7rFaVhyYet9R2zesRAKKyoKRqdN-dAFEgq_TWuDjrOiu2_DyPQt8QtyJfUT8UzRGioBBxZGIzgKdpuJrNS-5-GzZuryF97J5ooVix8JblryDaBDvJteSvTm3d5nLvH19AKa0CweiupR1XBJT7hNAzwIRR9hrDWKhIOo7Q9BENOMef6DRCg7gahhDO8k2r4yG48bCEkuDwdcs5NluFfLMbbLA2XNPHzHwW9-UsAaib_1DMICe2YcsBa3lu1AAAAAAUZCL70A"
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
