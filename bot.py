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
    if choice == "HEADS":
        global wins
        wins += 1
    else:
        global losses
        losses += 1
    await ctx.send(choice)

@bot.command(name="counter")
async def counter(ctx):
    global wins, losses
    await ctx.send(f"Your win:loss ratio is {wins}:{losses}.")
    
bot.run(token)
