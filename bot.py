import random
from discord.ext import commands
import json
import os

os.chdir(r"/project/Hmmm-help-Casino-Bot")
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

wins = 0
losses = 0  

@bot.event
async def on_member_join(member):
    with open('users.json', 'r+') as f:
        data = json.load(f)
        if not member in data.keys():
            data[member] = 100
            f.seek(0)
            json.dump(data, f)

@bot.event
async def on_message(message):
    with open('users.json', 'r+') as f:
        data = json.load(f)
        if message.author.name in data.keys():
            data[message.author.name] += 1
        else:
            data[message.author.name] = 100
            f.seek(0)
            json.dump(data, f)

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
    if outcome == True:
        wins += 1
        await ctx.send("Look at you! Don't be shy- play some more!")

@bot.command(name = "Win:Loss")
async def counter(ctx):
    await ctx.send(f"Your ratio is now {wins}:{losses}.")
    
@bot.command(name = "guessing_game")
async def guessinggame(ctx,choice):
    number = random.randint(1,10)
    if int(choice) == number:
        global losses, wins
        wins += 1
        await ctx.send("Hey goodjob!")
    if int(choice) != number: 
        losses += 1
        await ctx.send(f"Sucks to suck, the number was {number}")

bot.run(token)
