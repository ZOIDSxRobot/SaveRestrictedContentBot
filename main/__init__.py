#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "21556392"
API_HASH = "48469320efa1b110f1fda0f2d767521c"
BOT_TOKEN = "6948559234:AAEz9BvD7gi1BGRlwN9Ifmz3N4aly0pdTDY"
SESSION = "AQB8TiZ97cc37-EvgMNmLRiEJVO9gc8GO8J0eLtJtfeMFh53cpsb4nSumAAkk9zyK4Ay3SjYSKoPVORZVH2vw_eAPxArstwrx-GgFITuvAXW_Ydod65VgJbhywE3GIv9uRneASzhmjKttC9h4Xiiuc-6Cb_JvDMmX7Emo5EuLRfYJqitvvBwfXO0rlVVpDWVHL5ZdblfYPdyEgODl_n5eNafXHl8zj8PCG-bQMlRd3ghLqoE79-K1B8sxXT1WWiwkm6VdAX7WZHVOwe5ZsBA-d7EV6HrNVwTz-3pjB0NSSzgfwmCEr29sJwpvJhdc1OAX4XdQBZ3i9BgKi8CtoRwEB4IAAAAAYPwZokA"
FORCESUB = "Zoids_Robot"
AUTH = 6508537481

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
