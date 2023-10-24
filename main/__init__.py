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
BOT_TOKEN = "6948559234:AAEz9BvD7gi1BGRlwN9Ifmz3N4aly0pdTDY"
SESSION = "AQC4xtRT2QRyTOnd8FmceESzZao096xquqHoTenXoRCY8Twvc4dGE1dNq7AMvAcx2uHBmL4No5etLl9R9k7YQM2O45rT1fa-D5ti_10IZ6NdIWz63IxAlEz2IcuqrzWP8xOlPf_1MQDvE-sEmCRrebKDIulMsTLzfoz3jMU-DBjkPD7YD2RqunFA9K2kCek0VIHy-o1AR89iC5jvwTwFvCPf4o7uzkZS4jMoSLq8g2pybNuubyF-_IxehG9KhloGhzVuad-RyLGnKV5oBxHMszTEHrRqdKhzYX1WwDpYwqD77MMPwfHrJ2LSIk1xR_IAOh4Tkcd18CsS_JHS2AUXynCkAAAAAYPwZokA"
FORCESUB = "ZoidsRobot"
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
