from discord.ext import commands
import requests
import discord
class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='repeat', description='I\'ll repeat what did you said!', aliases=['say'])
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def repeat(self, ctx, *, text: str = None):
        if text is None:
            return await ctx.send('Please input a text')
        if ctx.me.guild_permissions.manage_messages:
            await ctx.message.delete()
        await ctx.send(text)
        pass

    @commands.command(name='wikihow', description='random wikihow image', aliases=["wiki"])
    async def wiki(self, ctx):
        payload={}
        response = requests.request("GET", "https://api.nezukochan.xyz/wikihow", data=payload)
        embed = discord.Embed(title=response.json()["title"])
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)

    @commands.command(name='baka', description='random bakka image')
    async def baka(self, ctx):
        payload={}
        response = requests.request("GET", "https://nekos.life/api/v2/img/baka", data=payload)
        embed = discord.Embed(title="BAKKAAAA!!!")
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))