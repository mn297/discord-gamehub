import random
import discord
import os
from discord.ext import commands

async def rockpaperscissorscomputer(userin):
    client = discord.Client()
    bot = commands.Bot(command_prefix='$')

    @bot.command(name='rps rock')
    async def rpsrock(ctx):

        com = random.randrange(1,3)
        if com == 1:
            print("Tie!")
        elif com == 2:
            print("I choose scissors. You win!")
        elif com == 3:
            print("I choose paper. I win!")
        
        await ctx.send(com)

   