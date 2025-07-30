import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import os

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True  # Necesario para acceder a miembros
bot = commands.Bot(command_prefix='!', intents=intents)

# Tu ID de usuario (el que quieres mutear)
USER_ID = 508063119592128522  # Reemplaza con tu ID de Discord
GUILD_ID = 1385086752901042297  # ID del servidor
CHANNEL_ID = 1385086753479725129  # ID del canal de voz

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    scheduler = AsyncIOScheduler()
    
    # Define la hora en que quieres que te mutee (ej: 23:00 todos los días)
    scheduler.add_job(mute_user, 'cron', hour=7, minute=10)
    scheduler.start()

async def mute_user():
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(USER_ID)
    if member and member.voice:
        await member.edit(mute=True)
        print(f"{member.display_name} ha sido muteado.")

bot.run(os.getenv("DISCORD_TOKEN"))
