from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables


Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
