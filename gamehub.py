#from turtle import pos
import pandas as pd
from discord.ext import commands
from dotenv import load_dotenv
import discord
import asyncio
import os
import random
#from turtle import pos

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
#client = discord.Client()


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     elif message.content.startswith('_'):

#         cmd = message.content.split()[0].replace("_", "")
#         if len(message.content.split()) > 1:
#             parameters = message.content.split()[1:]

#     if cmd == 'scan':

#         data = pd.DataFrame(columns=['content', 'time', 'author'])

#         def is_command(msg):  # Checking if the message is a command call
#             if len(msg.content) == 0:
#                 return False
#             elif msg.content.split()[0] == '_scan':
#                 return True
#     else:
#         return False

#   # As an example, I've set the limit to 10000
#     async for msg in message.channel.history(limit=10000):
#         if msg.author != client.user:                        # meaning it'll read 10000 messages instead of
#             # the default amount of 100
#             if not is_command(msg):
#                 data = data.append({'content': msg.content,
#                                     'time': msg.created_at,
#                                     'author': msg.author.name}, ignore_index=True)
#         if len(data) == limit:
#             break

#         file_location = "data.csv"  # Set the string to where you want the file to be saved to
#         data.to_csv(file_location)

# @bot.command(name='rps_rock')
# async def rpsrock(ctx):

#     com = random.randrange(1, 3)
#     if com == 1:
#         out = "Tie"
#     elif com == 2:
#         out = "I choose scissors. You win!"
#     elif com == 3:
#         out = "I choose paper. I win!"

#     await ctx.send(ctx.message.author)


# # @bot.command(name='rps')
# # async def rps(ctx):
# #     user = ctx.message.author

# #     m = await ctx.send('Rock, paper, scissors. Take your pick: ')
# #     c = await m.add_reaction('🪨')
# #     await m.add_reaction('📜')
# #     await m.add_reaction('✂️')

# #     def check(reaction, user):
# #         return user == ctx.author and str(reaction.emoji) in ['🪨']

# #     b = await c.users().flatten()
# #     ctx.send(b)

# @client.event
# async def on_message(message):
#     if "?" in message.content and message.author != client.user:
#         await message.channel.send("Have you tried DeMorgan?")


# # @client.command()
# # async def history(ctx, member: discord.Member):
# #     counter = 0
# #     for channel in ctx.guild.channels:
# #         async for message in channel.history(limit=100):
# #             if message.author == member:
# #                 counter += 1

# #     await ctx.send(f'{member.mention} has sent **{counter}** messages in this server.')

global currentMemberCopying
global possibleSayings


@bot.command(name='getHistoryOf')
async def history(ctx, user):
    user_id = int(user[3:-1])
    h = await ctx.channel.history(limit=9999).flatten()
    global possibleSayings
    global currentMemberCopying

    possibleSayings = [
        message.content for message in h if message.author.id == user_id]
    currentMemberCopying = user

    await ctx.send(f"Scraped the messages of {user}.")


@bot.command(name='talk')
async def talk(ctx):
    await ctx.send(random.choice(possibleSayings))

# client.run(TOKEN)
bot.run(TOKEN)
