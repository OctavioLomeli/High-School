import discord
import pandas as pd
from discord.ext import commands

# to save time for the stats command
stat_list = pd.read_csv('service_hours.csv')
stat_list.columns = stat_list.iloc[0]
stat_list = stat_list.drop([0])
stat_list = stat_list.fillna(0)
stat_list.set_index('Member Name', inplace=True)
stat_list = stat_list[['Grade', 'Hours Gained', 'Goal', 'Hours Needed']].iloc[:71]

# to save time for the services_attended command
num_list = pd.read_csv('service_hours.csv')
num_list.columns = num_list.iloc[0]
num_list = num_list.drop([0])
num_list = num_list.fillna(0)
num_list = num_list.loc[:, (num_list != 0).any(axis=0)]
num_list.set_index('Member Name', inplace=True)
dropping = ['Grade', 'Hours Gained', 'Goal', 'Hours Needed']
num_list = num_list.drop(dropping, axis = 1)

# class
class BuildOn(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
      print('BuildOn file is ready.')

  # sends all links
  @commands.command()
  async def links(self, ctx):
      await ctx.send(
          'Service Guide: https://docs.google.com/document/d/1N_L-_7ERpMLt8LvxIGYBvxkykoaVj69JK-67lJLuvLk/edit\nHours Tracker: https://docs.google.com/spreadsheets/d/177URmZo7VJQ7WerHDWWs0wYemcoeNRd5czk63NZC63o/edit#gid=392807749\nMembership Form: https://www.tfaforms.com/4849169\nParent Consent Form + Release Form: https://www.tfaforms.com/4849471'
      )


  # sends link to hours tracker
  @commands.command()
  async def hours(self, ctx):
      await ctx.send(
          'Hours Tracker:  https://docs.google.com/spreadsheets/d/177URmZo7VJQ7WerHDWWs0wYemcoeNRd5czk63NZC63o/edit#gid=392807749'
      )


  # sends link to service guide
  @commands.command()
  async def guide(self, ctx):
      await ctx.send(
          'Service Guide: https://docs.google.com/document/d/1cSigGR_o4l3Zbzuvb1y0MUO0PHNhVVpasBSlwxzCqSQ/edit'
      )


  # sends forms to sign up
  @commands.command()
  async def new_member(self, ctx):
      await ctx.send(
          'Welcome to BuildOn\nParent Consent Form + Release Form: https://www.tfaforms.com/4849471\nMembership Form: https://www.tfaforms.com/4849169'
      )


  # sends social media
  @commands.command()
  async def social(self, ctx):
      await ctx.send(
          'Remind Class Code: @buildon21\nInstagram: https://www.instagram.com/buildonoakland/\nWebsite: https://www.buildon.org/what-we-do/us/oakland/'
      )


  # sends zoom link
  @commands.command()
  async def zoom(self, ctx):
      await ctx.send('https://buildon.zoom.us/j/92025277055')


  # sends hours message
  @commands.command(aliases=['rank'])
  async def stats(self, ctx, *, name='Octavio Castro'):
      try:
          await ctx.send(
              "```Grade           {}\nHours Gained    {}\nGoal            {}\nHours Needed    {}\nName: {} ```"
              .format(stat_list.loc[name]['Grade'], stat_list.loc[name]['Hours Gained'],
                      stat_list.loc[name]['Goal'], stat_list.loc[name]['Hours Needed'], name))
      except:
          await ctx.send(
              '```No member with that name exists. Check your spelling and capitalization.\nIf error, DM eojune#3500```'
          )


  # sends top 3 people with hours
  @commands.command()
  async def top(self, ctx):
      df = pd.read_csv('service_hours.csv')
      df.columns = df.iloc[0]
      df = df.drop([0])
      df = df.fillna(0)
      df = df[['Member Name', 'Grade', 'Hours Gained']].iloc[:3]
      await ctx.send(
          "Formatted bad on phone, sorry\n```      Hours           Grade    Name\n\n1.    {}            {}      {}\n2.    {}            {}      {}\n3.    {}            {}      {}```"
          .format(df.iloc[0]['Hours Gained'], df.iloc[0]['Grade'],
                  df.iloc[0]['Member Name'], df.iloc[1]['Hours Gained'],
                  df.iloc[1]['Grade'], df.iloc[1]['Member Name'],
                  df.iloc[2]['Hours Gained'], df.iloc[2]['Grade'],
                  df.iloc[2]['Member Name']))


  # sends latest instagram post
  @commands.command()
  async def insta(self, ctx):
      await ctx.send(file=discord.File('posts/insta_post.jpg'))


  # sends the number of services a member attended
  @commands.command(aliases=['sa', 'num'])
  async def service_attended(self, ctx, *,member='Octavio Castro'):
      try:
        count = 0
        for column_num in range(len(num_list.columns)):
            if num_list.loc[member][column_num] !='0':
                count += 1
        await ctx.send("{} has attended {} services.".format(member, count))
      except:
        await ctx.send('```No member with that name exists. Check your spelling and capitalization.\nIf error, DM eojune#3500```')


  # sends list of services for the month
  @commands.command()
  async def service(self, ctx):
    data = {'Service Theme': ['Teacher Appreciation', 'Food Justice', 'Paper Ornament + Social', "God’s Eye/Ojos de Dios "],
    'Sign Up': ['https://www.tfaforms.com/forms/view/4851569?tfa_15=a0X4T000000Z6Kd&tfa_6=12%2F5%2F2020&tfa_8=Saturday+Event&tfa_10=Teacher+Appreciation+Jibjabs&tfa_17=3&tfa_19=a0V4T000000J10X', 'https://www.tfaforms.com/forms/view/4851569?tfa_15=a0X4T000000Z6Ll&tfa_6=12%2F12%2F2020&tfa_8=Saturday+Event&tfa_10=Food+Justice+Recipe+Booklets&tfa_17=3&tfa_19=a0V4T000000J10X', 'https://www.tfaforms.com/forms/view/4851569?tfa_15=a0X4T000000Z6Lq&tfa_6=12%2F19%2F2020&tfa_8=Saturday+Event&tfa_10=Holiday+Party+Social+%2B+Superlatives&tfa_17=3&tfa_19=a0V4T000000J10X', 'https://www.tfaforms.com/forms/view/4851569?tfa_15=a0X4T000000ZC4N&tfa_6=12%2F23%2F2020&tfa_8=Afterschool&tfa_10=Holiday+Crafts+Over+Break&tfa_17=3&tfa_19=a0V4T000000J10X']
    }
    df = pd.DataFrame(data, columns = list(data.keys()))
    for index in range(len(df['Service Theme'])):
      await ctx.send('{}:     {}'.format(df['Service Theme'][index], df['Sign Up'][index]))

def setup(client):
    client.add_cog(BuildOn(client))
