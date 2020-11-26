import discord
from discord.ext import commands
class Help(commands.Cog, name="Help"):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.group(name='help')
    async def help(self, ctx):
      if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Welcome to the help page!", description=""
        "To get help please use `help [CategoryName]`.\nAvailable categories are: `fun`, `music` \n\n",
        color=0x00FFAA)
        await ctx.send(embed=embed)
    
    @help.command(name="fun")
    async def help_fun(self, ctx):
      embed = discord.Embed(title="Fun Commands", description=""
      "** Name | Info**\n"
      "- `baka` | Send Random Bakka Images.\n"
      "- `wikihow` | Send Random WIkihow Images.\n",
      color=0x00FFAA)
      author = ctx.message.author
      pfp = author.avatar_url
      embed.set_author(name=f'{self.bot.user.name}',icon_url=f'{self.bot.user.avatar_url}')
      embed.set_thumbnail(url=pfp)
      await ctx.send(embed=embed)

      



def setup(bot):
    bot.add_cog(Help(bot))


