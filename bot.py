import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    # Ici, tu incrémenteras l'XP de l'utilisateur
    print(f"{message.author} a envoyé un message : {message.content}")

    await bot.process_commands(message)

bot.run("TON_TOKEN_ICI")
