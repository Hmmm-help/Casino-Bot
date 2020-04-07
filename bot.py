import os
import json
import random
from discord.ext import commands

os.chdir(r"/project/Hmmm-help-Casino-Bot")
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

wins = 0
losses = 0  

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["balance"] = 100

@bot.event
async def on_member_join(member):
    with open("users.json", "r") as f:
        users = json.load(f)

    await update_data(users, member)

    with open("users.json", "w") as f:
        json.dump(users, f)

@bot.event
async def on_message(message):
     with open("users.json", "r") as f:
        users = json.load(f)

    await update_data(users, message.author)

    with open("users.json", "w") as f:
        json.dump(users, f)

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
async def GG(ctx):
    import random
    number = random.randint(1,10)
    if choice == number:
        print(number)
        return "Hey goodjob!"
    elif choice != number:
        print(number)
        return "Sucks to suck"

    
@bot.command(name = "guessing_game")
async def GuessingGame(ctx,choice):
    (number) = random.randint(1,10)
    if int(choice) == number:
        await ctx.send("Hey goodjob!")
    else:
        await ctx.send(f"Sucks to suck, the number was {number}")

bot.run(token)
