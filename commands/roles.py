import discord
import variables as v
import modules.fetch as fetch

async def update_roles(interaction: discord.Interaction):
    discord_id = str(interaction.user.id)
    try:
        player_data = fetch.fetch_player(discord_id)
        player_records = player_data.records

        await interaction.response.send_message(f"Hey, {player_data.name} exists on our website!")
    except Exception as e:
        print(e)
        await interaction.response.send(('An error occurred while fetching player data.'
            'Make sure your Discord account is connected with your Pemonlist account by logging into our website with Discord.'))