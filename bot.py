import discord
from discord.ext import commands, tasks
from discord.utils import get
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import tasks.roles as roles
from commands.setup import setup as setup_commands
from tasks.setup import setup as setup_tasks
import variables as v

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.id == v.ERROR_CHANNEL_ID:
        return

    await bot.process_commands(message)

@bot.event
async def on_ready():
    v.GUILD = get(bot.guilds, id=v.GUILD_ID)
    v.GUILD_OBJ = discord.Object(id=v.GUILD_ID)

    print(f'{bot.user} has connected to the following guild:\n{v.GUILD.name} (id: {v.GUILD.id})')

    # Create a new client and connect to the server
    client = MongoClient(v.URI, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"MongoDB error: {e}")
    
    v.error_channel = bot.get_channel(v.ERROR_CHANNEL_ID)
    setup_commands(bot)
    await bot.tree.sync(guild=v.GUILD_OBJ)
    print(f"Ready to go!")
    print(f"Initializing tasks...")
    setup_tasks(bot)
    print(f"Tasks initialized!")


bot.run(v.TOKEN)