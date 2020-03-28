import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name= "Coin-Flip")
async def Coin_Flip(ctx):
    import random
    await (random.choice(["HEADS", "Tails"]))

@bot.command(name= "Emoji-Slot")
async def emjoi_slot(ctx):
    import random
    options = ["🤡","😷","👽"]
    slot = [random.choice(options),random.choice(options),random.choice(options)]
    await(slot)
    outcome = all(x == slot[0] for x in slot)
    if outcome == False:
        await "Sorry son, this ain't it- ya lost some cash."
    if outcome == True:
        await "Look at you! Don't be shy- play some more!"