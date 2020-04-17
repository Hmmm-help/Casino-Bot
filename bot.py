import os
import random
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

wins = 0
losses = 0  
  
bal = list(discord.member.guild.members)
all_bal = {i:100 for i in bal}

@bot.command(name= "Coin-Flip") 
async def Coin_Flip(ctx):
    choice = random.choice(["HEADS", "TAILS"])
    await ctx.send(choice)
    if choice == "HEADS":
        global wins, losses
        wins += 1
    else:
        losses += 1
    
@bot.command(name= "Emoji-Slot")
async def emjoi_slot(ctx):
    import random
    options = ["🤡","😷","👽"]
    slot = [random.choice(options),random.choice(options),random.choice(options)]
    await ctx.send(slot)
    outcome = all(x == slot[0] for x in slot)
    if outcome == False:
        global losses, wins
        losses += 1
        await ctx.send("Sorry son, this ain't it- ya lost some cash.")
        await all_bal
    if outcome == True:
        wins += 1
        await ctx.send("Look at you! Don't be shy- play some more!")

@bot.command(name = "Win:Loss")
async def counter(ctx):
    await ctx.send(f"Your ratio is now {wins}:{losses}.")
    
@bot.command(name = "guessing_game")
async def GuessingGame(ctx,choice):
    (number) = random.randint(1,10)
    if int(choice) == number:
        await ctx.send("Hey goodjob!")
    else:
        await ctx.send(f"Sucks to suck, the number was {number}")

bot.run(token)
