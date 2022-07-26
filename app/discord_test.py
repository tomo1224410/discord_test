import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('Discord Bot test 起動中！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'test':
        await message.channel.send('discord bot テスト中!')

client.run(TOKEN)