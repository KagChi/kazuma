import os
from discord.ext import commands
import B
import discord


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=['k,'], help_command=None, activity=discord.Activity(type=1, name="k,help for info!"))

    async def on_ready(self):
        print(f'Logged in as {self.user.name} | {self.user.id}')
        
        
        

client = Bot()
modules = [f  for f  in os.listdir('./modules') if os.path.isfile(os.path.join('modules', f))]

for(cogs) in modules:
  try:
    cogs_name= cogs.split('.py')[0]
    client.load_extension('modules.{0}'.format(cogs_name))
    print(f'Loaded {cogs}')
  except Exception as e:
     exc = '{}: {}'.format(type(e).__name__, e)
     print('Falied To load cogs {}\n{}'.format(cogs, exc))
B.b()
client.run(os.environ.get("token"))

