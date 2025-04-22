import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD'))
URI = os.getenv('MONGODB_URI')
ERROR_CHANNEL_ID = int(os.getenv('ERROR_CHANNEL'))

GUILD = None
GUILD_OBJ = None
error_channel = None
bot = None