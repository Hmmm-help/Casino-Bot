import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name= "Coin-Flip")
async def Coin_Flip(ctx):
    import random
    await (random.choice(["HEADS", "Tails"]))

bot.run(token)
