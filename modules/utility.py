from discord.ext import commands
import os, sys, discord, platform, psutil, pycrypt
class Utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'Pong! **{int(self.bot.latency * 1000)}ms** :ping_pong:')
    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        """
        Get some useful (or not) information about the bot itself.
        """
        ping = int(self.bot.latency * 1000)
        if (ping < 50):
            pingEmote = ":green_circle:"
        if (ping >= 50):
            pingEmote = ":orange_circle:"
        if (ping >= 100):
            pingEmote = ":red_circle:"
        emb = discord.Embed(title=f"Kazuna", color=0x00FFAA)
        emb.add_field(name="🔹 Me", value=""
        f"• Owners: **KagChi**\n"
        f"• Name: **{self.bot.user.name}**\n"
        f"• Discrim: **{self.bot.user.discriminator}**\n"
        f"• ID: **{self.bot.user.id}**\n"
        f"• Version: **v0.0.1**\n"
        f"• Ping: **{pingEmote} {int(self.bot.latency * 1000)}ms**\n"
        f"• Created: **{'{:02d}'.format(self.bot.user.created_at.day)} {self.bot.user.created_at.strftime('%B')} {self.bot.user.created_at.year}**\n"
        "", inline=False)

        emb.add_field(name="🔹 System", value=""
        f"• OS: **{platform.system()}**\n"
        f"• OS Version: **{platform.release()}**\n"
        f"• CPU Cores: **{os.cpu_count()}**\n"
        f"• CPU Usage: **{int(psutil.cpu_percent())}%**\n"
        f"• RAM Usage: **{int(psutil.virtual_memory()[2])}%**\n"
        f"• Disk Usage: **{int(psutil.disk_usage('/')[3])}%**\n"
        "", inline=False)

        emb.add_field(name="🔹 Statistics", value=""
        f"• Commands: **{len(self.bot.commands)}**\n"
        f"• Servers: **{len(self.bot.guilds)}**\n"
        f"• Members: **{'{:,}'.format(len(set(self.bot.get_all_members())))}**\n"
        "", inline=False)

        emb.add_field(name="🔹 Process Information", value=""
        f"• Python: **{platform.python_version()}**\n"
        f"• discord.py: **{discord.__version__}**\n"
        "", inline=False)

        
        await ctx.send(embed=emb)

       
def setup(bot):
    bot.add_cog(Utility(bot))