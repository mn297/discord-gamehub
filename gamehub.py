import os
import random
import discord
from discord.ext import commands



from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='$')
client = discord.Client()

print(type(token))
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord as a bot!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$talk"):
        await message.channel.send("Bot is talking! my-PC")
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    pass


bot.run(token)
client.run(token)

