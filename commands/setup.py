from discord import app_commands
from commands.roles import update_roles
from commands.pemon import pemon

def setup(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="updateroles",
            description="Change your Pemonlist roles (WIP)",
            callback=update_roles,
        )
    )
    bot.tree.add_command(
        app_commands.Command(
            name="pemon",
            description="Talks about pemons",
            callback=pemon,
        )
    )