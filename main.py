import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user}'.format(client) + 'has entered the chat.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')


client.run(os.getenv('TOKEN'))

