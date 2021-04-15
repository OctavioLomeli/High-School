import discord
from discord.ext import commands

# class
class Utility(commands.Cog):

  def __init__(self, client):
        self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
      print('Utility file is ready.')
  
  # deletes messages, default is 3
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def prune(self, ctx, amount=3):
      if amount <= 0:
          amount = 3
      await ctx.channel.purge(limit=(amount + 1))


  # kicking member
  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send('Kicked {}\nReason: {}'.format(member, reason))

  # banning member
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send('Banned {}\nReason: {}'.format(member, reason))

  # unbanning member
  @commands.command()
  async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("Unbanned {}#{}".format(member_name, member_discriminator))
            return


def setup(client):
  client.add_cog(Utility(client))
