# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    joe_pasta = "Who is Joe? This is a question which has boggled the minds of many scientists across many " \
                "generations. However after many sessions of independent research and personal experiments " \
                "I believe I have found an answer. Joe, to put it simply. Does not exist. He is a construct " \
                "of the human mind and when someone is asked or asks the question “who is Joe?” it results " \
                "in the asker getting pranked when the asked says the phrase “Joe mama”"

    if message.content == 'Joe!':
        response = joe_pasta
        await message.channel.send(response)

client.run(TOKEN)
