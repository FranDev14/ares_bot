import discord
from discord.ext.commands import Bot, when_mentioned_or
from app.modules.logger import DiscordHandler
import logging

logger = logging.getLogger(__name__)
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = Bot(command_prefix=when_mentioned_or("!"), intents=intents)

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger

# Modules loaded
bot.load_extension("app.modules.commands")