import discord
import os
import requests
import json
import random

client = discord.Client()

sad_list = ['depressed', 'depressing', 'melancholic', 'feeling blue', 'saddened', 'miserable']

encouragement_words = ["Don't mind", "At least I like you.", "You are nice...kinda", "Want a cookie?"]


# random quotes with zenquotes.io
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('{0.user}'.format(client) + 'has entered the chat.')


@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith('$hello'):
        await message.channel.send('Hello')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_list):
        await message.channel.send(random.choice(encouragement_words))


client.run(os.getenv('TOKEN'))
