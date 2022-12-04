import discord
from discord.ext.commands import Bot, when_mentioned_or

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = Bot(command_prefix=when_mentioned_or(">"), intents=intents)

