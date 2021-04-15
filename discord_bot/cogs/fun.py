import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
      print('Fun file is ready.')
  

  # responds with a greeting
  @commands.command(aliases=['hello', 'hai', 'sup', 'howdy'])
  async def hi(self, ctx):
      greetings = ['hi', 'hello', 'hola', 'bonjour', 'Octavio says hi']
      await ctx.send(random.choice(greetings))


  # responds with a bye
  @commands.command(aliases=['adios', 'goodbye', 'farewell'])
  async def bye(self, ctx):
      leaves = [
          'bye', 'adios', 'farewell', 'see you later', 'goodbye',
          'Octavio says bye', 'Diego says bye'
      ]
      await ctx.send(random.choice(leaves))


  # sends a dancing message
  @commands.command(aliases=['wiggle'])
  async def dance(self, ctx):
      dance_options = [
          'wiggle wiggle', '〜(￣▽￣〜)(〜￣▽￣)〜',
          '(•\_•)\n <) )╯\n  / \ \n (•\_•) \n \\\( (>\n   / \ \n(•_•)\n <) )╯\n  / \ '
      ]
      await ctx.send(random.choice(dance_options))


  # sends a jojo meme
  @commands.command()
  async def hayato(self, ctx):
      await ctx.send('⣿⠃⠷⣤⡄⠄⠑⢆⠄⠄⠄⠄⠰⣷⡗⠄⣴⠞⠄⠄⠠⣤⡬⢿⣿⣿⣿⣿\n⣿⡀⣼⣿⣿⣷⣄⠄⠄⠄⠄⠄⠄⠙⢁⣼⠋⣠⣾⣿⠷⠬⣾⣛⡿⣿⣿⣿\n⣿⢷⣿⣿⣿⣿⣿⣆⣀⠄⠄⠄⢀⡀⢸⠇⢐⢟⠛⠈⠰⢟⣹⣷⣳⠈⣿⣿\n⣿⠔⢸⡏⠉⠉⠙⠛⠛⠻⠿⢢⣼⣿⣷⣿⡯⢞⡢⠤⠐⠈⣽⣿⣟⡆⢸⣿\n⣿⣦⣿⡷⣵⣿⡟⠏⠠⢤⣬⠉⠋⡹⡻⣿⢦⣄⡀⠄⠄⠄⣿⣿⣿⢰⣷⣿\n⣿⣿⣿⣽⣿⣵⢿⠄⢀⡼⠊⠄⢠⣿⣾⣽⣿⣽⣿⣷⣦⣼⣿⣿⣻⢺⣮⣿\n⣿⣿⡾⡿⣽⣿⣿⣏⠄⠄⠄⠄⠸⣷⣿⣿⡻⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣻⣿⠿⣿⣿⣷⡄⠄⠄⠄⠄⠄⠈⠁⢼⣿⣿⡿⢿⣴⣿⣿⣿⠻⣿\n⣿⣿⣿⣿⣯⣾⣮⣿⣿⣿⣦⠄⠄⣀⣴⣶⠶⣞⣫⣭⣦⣿⣿⣿⣿⢻⠄\n⣿⣿⣿⣿⣽⣿⣿⣿⣿⡻⣷⣷⡈⠫⢶⣤⣼⣷⣯⡷⠟⠁⣿⣿⡟⡄⠄⠄\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⡢⠄⢈⠉⠉⠄⠄⠄⠄⣸⣯⠁⠇⡆⠄ \n⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⡛⣷⣶⣮⣶⣶⢶⣶⣶⡶⠞⠋⠄⠄⠄⠇⠄')
 

def setup(client):
  client.add_cog(Fun(client))
