import discord
import wavelink
import humanize
import os
import asyncio
from discord.ext import commands
import datetime
class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        songs = asyncio.Queue()
        play_next_song = asyncio.Event()

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)
        self.bot.loop.create_task(self.start_nodes())
        
    async def on_event_hook(event):
       if isinstance(event, (wavelink.TrackEnd, wavelink.TrackException)):
        play_next_song.set()

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        node = await self.bot.wavelink.initiate_node(host=f'{os.environ.get("host")}',
                                              port=8080,
                                              rest_uri=f'http://{os.environ.get("host")}:8080',
                                              password='youshallnotpass',
                                              identifier='Kanna',
                                              region='Indonesia')
        node.set_hook(on_event_hook)

        while True:
            play_next_song.clear()
            song, guild_id = await songs.get()
            player = client.wavelink.get_player(guild_id)
            await player.play(song)
            await play_next_song.wait()


    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**')
        await player.connect(channel.id)

    @commands.command(name='play')
    async def play(self, ctx, *, query: str):
          
          tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

          if not tracks:
            return await ctx.send('Could not find any songs with that query.')

          player = self.bot.wavelink.get_player(ctx.guild.id)
          if not player.is_connected:
            await ctx.invoke(self.connect_)

            await ctx.send(f'Added {str(tracks[0])} to the queue.')
            await player.play(tracks[0])

    @commands.command(name="info")
    async def info(self, ctx):
         """Retrieve various Node/Server/Player information."""
         player = self.bot.wavelink.get_player(ctx.guild.id)
         node = player.node

         used = humanize.naturalsize(node.stats.memory_used)
         total = humanize.naturalsize(node.stats.memory_allocated)
         free = humanize.naturalsize(node.stats.memory_free)
         cpu = node.stats.cpu_cores

         fmt = f'**WaveLink:** `{wavelink.__version__}`\n\n' \
              f'Connected to `{len(self.bot.wavelink.nodes)}` nodes.\n' \
              f'Best available Node `{self.bot.wavelink.get_best_node().__repr__()}`\n' \
              f'`{len(self.bot.wavelink.players)}` players are distributed on nodes.\n' \
              f'`{node.stats.players}` players are distributed on server.\n' \
              f'`{node.stats.playing_players}` players are playing on server.\n\n' \
              f'Server Memory: `{used}/{total}` | `({free} free)`\n' \
              f'Server CPU: `{cpu}`\n\n' \
              f'Server Uptime: `{datetime.timedelta(milliseconds=node.stats.uptime)}`'
         await ctx.send(fmt)
def setup(bot):
    bot.add_cog(Music(bot))
