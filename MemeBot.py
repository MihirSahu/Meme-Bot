import discord
from discord.ext import commands
import requests

#client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.name == "MercenaryHarpy6":
        await message.add_reaction("\U0001F921")
#    if message.author.name == "The One":
#        await message.add_reaction("\U0001F921")
#    if message.author.name == "Vsadygv":
#        await message.add_reaction("\U0001F921")
#    await client.process_commands(message)

#@client.event
#async def on_message(message):
#    if "June" in message.content or "june" in message.content:
#        await message.add_reaction('\U0001F63B')
#    if "Simp" in message.content or "simp" in message.content:
#        await message.add_reaction('\U0001F921')
#    if "Hot" in message.content or "hot" in message.content:
#        await message.add_reaction('\U0001F60B')
#    if "Feet" in message.content or "feet" in message.content:
#        await message.add_reaction('\U0001F4A6')
#    if "LMAO" in message.content or "lmao" in message.content:
#        await message.add_reaction('\U0001F602')
#    if "LMFAO" in message.content or "lmfao" in message.content:
#        await message.add_reaction('\U0001F923')
#    if "no homo" in message.content:
#        await message.add_reaction('\U0001F46C')
#    if "thiCC" in message.content or "thick" in message.content or "thicc" in message.content:
#        await message.add_reaction('\U0001F351')
#    if "I-" in message.content or "lolol" in message.content:
#        await message.add_reaction('\U0001F1FE')
#        await message.add_reaction('\U0001F1EA')
#        await message.add_reaction('\U0001F1F9')
#        await message.add_reaction('\U0001F1EE')
#    if "sp00k" in message.content or "spook" in message.content:
#        await message.add_reaction('\U0001F631')
#    if "thonk" in message.content:
#        await message.add_reaction('\U0001F914')
#    if "each other" in message.content:
#        await message.add_reaction('\U0001F440')
#    if "Bye" in message.content or "bye" in message.content:
#        await message.add_reaction('\U0001F44B')
#    if "gn" in message.content or "Gn" in message.content:
#        await message.add_reaction('\U0001F319')
#    if "shit" in message.content:
#        await message.add_reaction('\U0001F4A9')
#    if "rip" in message.content or "Rip" in message.content:
#        await message.add_reaction('\U0001F622')
#    if "oof" in message.content:
#        await message.add_reaction('\U0001F921')
#    await client.process_commands(message)

@client.command()
async def yomomma(ctx):
    response = requests.get('https://api.yomomma.info/')
    joke = response.json()
    await ctx.send(joke['joke'])

client.run('NzU2MDEwMDIzMTYyNzQwODE3.X2LnMw.mCfOlNorWmLEYEdNhuvUhgNK_Xw')
