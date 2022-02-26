import os
import rockpaperscissors
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
rockpaperscissors.rockpaperscissorscomputer()
client = discord.Client()

client.run(TOKEN)