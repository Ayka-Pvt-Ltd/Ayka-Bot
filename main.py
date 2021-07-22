import os, sys
import json
import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("config.json not found")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready')
    print('_____________________________________________________')


if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

bot.run(config["token"])
