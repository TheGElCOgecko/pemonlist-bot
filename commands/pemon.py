import discord
import random

async def pemon(interaction: discord.Interaction):
    responses = [
        (
            'Pimu is a game where you play as a little blue square and you have to jump over spikes and stuff. '
            'It\'s a really fun game and I love it. I play it all the time. I can\'t stop playing it. '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Geometry Dash',
        'glungus',
        'pemonpemonpemonpemonpemonpemonPEMON'
    ]

    response = random.choice(responses)
    await interaction.response.send_message(response)