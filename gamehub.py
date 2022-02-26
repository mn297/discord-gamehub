import asyncio
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
client = discord.Client()


@bot.command(name='rps_rock')
async def rpsrock(ctx):

    com = random.randrange(1, 3)
    if com == 1:
        out = "Tie"
    elif com == 2:
        out = "I choose scissors. You win!"
    elif com == 3:
        out = "I choose paper. I win!"

    await ctx.send(ctx.message.author)


# @bot.command(name='rps')
# async def rps(ctx):
#     user = ctx.message.author

#     m = await ctx.send('Rock, paper, scissors. Take your pick: ')
#     c = await m.add_reaction('🪨')
#     await m.add_reaction('📜')
#     await m.add_reaction('✂️')

#     def check(reaction, user):
#         return user == ctx.author and str(reaction.emoji) in ['🪨']

#     b = await c.users().flatten()
#     ctx.send(b)

@client.event
async def on_message(message):
    if "?" in message.content and message.author != client.user:
        await message.channel.send("Have you tried DeMorgan?")

client.run(TOKEN)
