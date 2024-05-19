import discord
from discord.ext import commands
import os
from dotenv import load_dotenv 

load_dotenv() 
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='^', intents=intents)
reactions_added = set()

@bot.event
async def on_ready ():
    print(f'\nReady to be used pookie bear <3')

@bot.command()
async def react(ctx, arg1):
    channel = ctx.channel  # Get channel where command was used
    msg = await channel.fetch_message(ctx.message.reference.message_id)  # Fetch message which command replied to
    word = arg1
    await ctx.message.delete()
    for letter in word:
        if letter.lower() == "a":
            if '\U0001F1E6' not in reactions_added:
                await msg.add_reaction('\U0001F1E6')
                reactions_added.add('\U0001F1E6')
            else:
                await msg.add_reaction('\U0001F170')
                reactions_added.add('\U0001F170')
        elif letter.lower() == "b":
            if '\U0001F1E7' not in reactions_added:
                await msg.add_reaction('\U0001F1E7')
                reactions_added.add('\U0001F1E7')
            else:
                await msg.add_reaction('\U0001F171')
                reactions_added.add('\U0001F171')
        elif letter.lower() == "c":
            await msg.add_reaction('\U0001F1E8')
        elif letter.lower() == "d":
            await msg.add_reaction('\U0001F1E9')
        elif letter.lower() == "e":
            if '\U0001F1EA' not in reactions_added:
                await msg.add_reaction('\U0001F1EA')
                reactions_added.add('\U0001F1EA')
            else:
                await msg.add_reaction('\U0001F4E7')
                reactions_added.add('\U0001F4E7')
        elif letter.lower() == "f":
            await msg.add_reaction('\U0001F1EB')
        elif letter.lower() == "g":
            await msg.add_reaction('\U0001F1EC')
        elif letter.lower() == "h":
            await msg.add_reaction('\U0001F1ED')
        elif letter.lower() == "i":
            if '\U0001F1EE' not in reactions_added:
                await msg.add_reaction('\U0001F1EE')
                reactions_added.add('\U0001F1EE')
            else:
                await msg.add_reaction('\U00002139')
                reactions_added.add('\U00002139')          
        elif letter.lower() == "j":
            await msg.add_reaction('\U0001F1EF')
        elif letter.lower() == "k":
            await msg.add_reaction('\U0001F1F0')
        elif letter.lower() == "l":
            await msg.add_reaction('\U0001F1F1')
        elif letter.lower() == "m":
            await msg.add_reaction('\U0001F1F2')
        elif letter.lower() == "n":
            await msg.add_reaction('\U0001F1F3')
        elif letter.lower() == "o":
            if '\U0001F1F4' not in reactions_added:
                await msg.add_reaction('\U0001F1F4')
                reactions_added.add('\U0001F1F4')
            else:
                await msg.add_reaction('\U0001F17E')
                reactions_added.add('\U0001F17E')
        elif letter.lower() == "p":
            if '\U0001F1F5' not in reactions_added:
                await msg.add_reaction('\U0001F1F5')
                reactions_added.add('\U0001F1F5')
            else:
                await msg.add_reaction('\U0001F17F')
                reactions_added.add('\U0001F17F')        
        elif letter.lower() == "q":
            await msg.add_reaction('\U0001F1F6')
        elif letter.lower() == "r":
            await msg.add_reaction('\U0001F1F7')
        elif letter.lower() == "s":
            await msg.add_reaction('\U0001F1F8')
        elif letter.lower() == "t":
            await msg.add_reaction('\U0001F1F9')
        elif letter.lower() == "u":
            await msg.add_reaction('\U0001F1FA')
        elif letter.lower() == "v":
            await msg.add_reaction('\U0001F1FB')
        elif letter.lower() == "w":
            await msg.add_reaction('\U0001F1FC')
        elif letter.lower() == "x":
            await msg.add_reaction('\U0001F1FD')
        elif letter.lower() == "y":
            await msg.add_reaction('\U0001F1FE')
        elif letter.lower() == "z":
            await msg.add_reaction('\U0001F1FF')
        elif letter.lower() == "!":
            if '\U00002755' not in reactions_added:
                await msg.add_reaction('\U00002755')
                reactions_added.add('\U00002755')
            else:
                await msg.add_reaction('\U00002757')
                reactions_added.add('\U00002757')
        elif letter.lower() == "?":
            if '\U00002754' not in reactions_added:
                await msg.add_reaction('\U00002754')
                reactions_added.add('\U00002754')
            else:
                await msg.add_reaction('\U00002753')
                reactions_added.add('\U00002753')
    
    reactions_added.clear()

bot.run(TOKEN)
