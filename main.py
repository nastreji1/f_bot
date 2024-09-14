import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.intents.all())
server_on()

bot.run(os.getenv('TOKEN'))
