import os
from rockpaperscissors import rockpaperscissorscomputer
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='$')
client.run(TOKEN)
bot.run(TOKEN)