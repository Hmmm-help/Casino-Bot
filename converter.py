money = 100
coins = money // 10 
 
import discord 
import os
 
@bot.command(name='coins')
async def conversion(ctx):
    await ctx.send(money//10)
 
@bot.command(name='money')
async def money(ctx):
    await ctx.send(money)
