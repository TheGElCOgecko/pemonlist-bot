from discord.ext import tasks
from tasks.roles import update_all_roles

def setup(bot):
    tasks.loop(hours=12)(update_all_roles).start()