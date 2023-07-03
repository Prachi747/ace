from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int(os.environ.get("API_ID", '15246273'))
API_HASH = os.environ.get("API_HASH", "6077e7b5f75a689f88c1bc96b1de1d15")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6168917254:AAFGLUd2STdhB33ZzsXqTcHH1Y3XzLhfjvE")
BOT_UN = os.environ.get("BOT_UN", "metacaptionRobot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
