from discord.ext.commands import Bot, Cog, command


class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        print("Commands plugin loaded")
        self.bot.log.info("Commands plugin loaded")

def setup(bot):
    bot.add_cog(Commands(bot))