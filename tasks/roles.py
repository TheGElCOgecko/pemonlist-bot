import discord
from discord.ext import tasks
from discord.utils import get
import modules.fetch as fetch
import variables as v
import datetime
from tzlocal import get_localzone

async def update_all_roles():
    LOCAL_TIMEZONE = get_localzone()
    now = datetime.datetime.now(LOCAL_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S %Z")
    print(f"Updating roles for all members at {now}")

    # Get member role
    member_role = get(v.GUILD.roles, name="Member")
    if member_role is None:
        await v.error_channel.send("⚠️ Member role not found!")
        return

    for member in v.GUILD.members:
        # Skip non-members
        if member_role not in member.roles:
            continue

        discord_id = str(member.id)
        try:
            player_data = fetch.fetch_player(discord_id)  # Fetch player data
            
        except Exception as e:
            continue

    print("Updated roles for all members!")