import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

 all_balances = {}

@bot.event
async on_member_join(member):
     x = {f"{member}": 100}
     all_balances.update(x)
     print(f"{member} has joined the server.")
     
@bot.command(name= "Coin-Flip")
async def Coin_Flip(ctx):
    import random
    await ctx.send(random.choice(["HEADS", "TAILS"]))

money = 100
@bot.command(name='coins')
async def conversion(ctx):
    await ctx.send(money//10)
 
@bot.command(name='money')
async def money(ctx):
    await ctx.send(money)
    
@bot.command(name= "Emoji-Slot")
async def emjoi_slot(ctx):
    import random
    options = ["🤡","😷","👽"]
    slot = [random.choice(options),random.choice(options),random.choice(options)]
    await ctx.send(slot)
    outcome = all(x == slot[0] for x in slot)
    if outcome == False:
        await ctx.send(f"New Balance for {client.user.name} is {all_balances[client.user.name] - 10}")
        await ctx.send("Sorry son, this ain't it- ya lost some cash.")
        all_balances[user.name] = all_balances[user.name] - 10
    if outcome == True:
        await ctx.send(f"New Balance for {client.user.name} is {all_balances[client.user.name] + 10}")
        await ctx.send("Look at you! Don't be shy- play some more!")
        all_balances[client.user.name] = all_balances[client.user.name] + 10
        
bot.run(token)
