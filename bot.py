import os
import random

from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

wins = 0
losses = 0

@bot.command(name= "Coin-Flip")
async def Coin_Flip(ctx):
    choice = random.choice(["HEADS", "TAILS"])
    await ctx.send(choice)
    if choice == "HEADS":
        wins += 1
    else:
        losses +- 1

@bot.command(name="counter")
async def counter(ctx):
    await ctx.send(f"Your score is now {wins}:{losses}.")
bot.run(token)
