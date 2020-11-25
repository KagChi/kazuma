from discord.ext import commands
class Utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'Pong! **{int(self.bot.latency * 1000)}ms** :ping_pong:')


def setup(bot):
    bot.add_cog(Utility(bot))