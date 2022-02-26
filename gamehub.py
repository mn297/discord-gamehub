import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')
@bot.command(name='rps_rock')
async def rpsrock(ctx):

    com = random.randrange(1,3)
    if com == 1:
        out = "Tie"
    elif com == 2:
        out = "I choose scissors. You win!"
    elif com == 3:
        out = "I choose paper. I win!"
        
    await ctx.send(out)
    
    

bot.run(TOKEN)