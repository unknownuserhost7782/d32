import discord
from discord.ext import commands
import os

token = "MTM0NTU1NzY0MTk1NDMyODU4Ng.GAIRpm.5cayAWHa-FGOpieJDj1AUorR1ZVUJelHaWPBVg"

# Setze das Intent-System, um Nachrichten zu empfangen
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Erforderlich für das Lesen von Nachrichten

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hallo {ctx.author.mention}!')

# Starte den Bot
bot.run(token)