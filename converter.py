 
import discord 
import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$') 

money = 100

@bot.command(name='coins')
async def conversion(ctx):
    await ctx.send(money//10)
 
@bot.command(name='money')
async def money(ctx):
    await ctx.send(money)
 
bot.run(token)
