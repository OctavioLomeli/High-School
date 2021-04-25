import discord
import os
from discord.ext import commands
from everlasting import everlasting

client = commands.Bot(command_prefix='j!')

client.remove_command('help')

# tells when ready
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game('Use j!help to see commands'))
    print('Bot is ready.')


# sends a message saying that the command does not exist
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('No such command.')
    else:
        print(error)

# for cogs
@client.command()
async def load(ctx, extension):
  client.load_extension('cogs.{}'.format(extension))

# for cogs
@client.command()
async def unload(ctx, extension):
  client.unload_extension('cogs.{}'.format(extension))


# sends a message explaining the commands
@client.command(aliases=['ayuda', 'halp', 'HELP', 'Help'])
async def help(ctx):
    await ctx.send(
        "Formatted bad on phone, sorry ``` 'Fun' Commands     Description\n\n j!hi               Sends a greeting message back\n j!bye              Sends a goodbye message back\n j!dance            Sends a random dancing message\n\n Covid Commands     Description\n\n j!covid            Sends num of cases of a state (Usage ex: j!covid Virginia)\n j!ccm              Sends the states > inputted num of cases (Usage ex.j!ccm 500000)\n j!cdm              Sends the states > inputted num of deaths (Usage ex. j!cdm 17000)\n\n BuildOn Commands   Description\n\n j!zoom             Sends zoom link\n j!social           Sends social media links\n j!hours            Sends link to hours tracker\n j!new_member       Sends forms for membership\n j!stats, j!rank    Sends the stats of member (Usage ex: j!stats First Last)\n j!top              Sends the stats of top 3 members with highest hours\n j!num              Sends the number of services a member attended. (Usage ex: j!num First Last)\n\n Utility Commands   Description\n\n j!prune            Deletes messages inputted. Default is 3 (Usage ex: j!prune 5)\n j!kick             Kicks a member. Reason is optional. (Usage ex: j!kick @eojune Reason)\n j!ban              Bans a member. Reason is optional. (Usage ex: j!ban @eojune Reason)\n j!unban            Unbans a member. (Usage ex: j!unban @eojune) ```"
    )


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


everlasting()
token = os.environ['KEY']
client.run(token)
