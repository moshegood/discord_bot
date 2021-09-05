import discord
#from discord.abc import GuildChannel
import requests

#from discord.message import Message
capes = {
    'http://textures.minecraft.net/texture/2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933': 'Migrator',
    'http://textures.minecraft.net/texture/953cac8b779fe41383e675ee2b86071a71658f2180f56fbce8aa315ea70e2ed6': 'Minecon 2011',
}

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello, how are you?')

    if message.content.startswith('hi'):
        await message.channel.send('Hello, how are you?')

    if message.content.startswith('how are you'):
        await message.channel.send('Being a bot LOL')

    if message.content.startswith('bye'):
        await message.channel.send('Bye Sir!')

    if message.content.startswith('uwu'):
        await message.channel.send('owo!')

    if message.content.startswith('rainbow'):
        await message.channel.send('Red, Orange, Yellow, Green, Blue, Indigo, Violet')

    if message.content.startswith('!help'):
        await message.channel.send('Commands: hello bye rainbow More commands coming soon to a bot near you')
    
    if message.content.startswith('!ign'):
        m = message.content
        username = m.split(' ')[1]
        await message.channel.send('https://namemc.com/profile/' + username)
        r = requests.get('https://api.mojang.com/users/profiles/minecraft/' + username)
        print(r.text)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

print('Starting...')
client.run(os.environ['DISCORD_TOKEN'])
