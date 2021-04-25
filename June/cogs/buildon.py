import discord
import pandas as pd
from discord.ext import commands
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import csv
import json
import os


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(os.environ['JSON_KEY']), scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '177URmZo7VJQ7WerHDWWs0wYemcoeNRd5czk63NZC63o'

service = build('sheets', 'v4', credentials=creds)


# class
class BuildOn(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
      print('BuildOn file is ready.')

  # sends link to hours tracker
  @commands.command()
  async def hours(self, ctx):
      await ctx.send(
          'Hours Tracker:  https://docs.google.com/spreadsheets/d/177URmZo7VJQ7WerHDWWs0wYemcoeNRd5czk63NZC63o/edit#gid=392807749'
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
    # Call the Sheets API
      sheet = service.spreadsheets()
      result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range="2020-2021 Hours!B2:AQ96").execute()

      with open('service_hours.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in result['values']:
          csv_writer.writerow(row)

      stat_list = pd.read_csv('service_hours.csv')

      stat_list = stat_list.fillna(0)
      stat_list.set_index('Member Name', inplace=True)
      stat_list = stat_list[['Grade', 'Hours Gained', 'Goal', 'Hours Needed']].iloc[:71]
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

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="2020-2021 Hours!B2:AQ96").execute()

    with open('service_hours.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',')
      for row in result['values']:
        csv_writer.writerow(row)

    stat_list = pd.read_csv('service_hours.csv')
    stat_list = stat_list.fillna(0)
    stat_list = stat_list[['Member Name', 'Grade', 'Hours Gained']].iloc[:3]

    await ctx.send(
        "Formatted bad on phone, sorry\n```      Hours           Grade    Name\n\n1.    {}            {}      {}\n2.    {}            {}      {}\n3.    {}            {}      {}```"
        .format(stat_list.iloc[0]['Hours Gained'], stat_list.iloc[0]['Grade'],
                stat_list.iloc[0]['Member Name'], stat_list.iloc[1]['Hours Gained'],
                stat_list.iloc[1]['Grade'], stat_list.iloc[1]['Member Name'],
                stat_list.iloc[2]['Hours Gained'], stat_list.iloc[2]['Grade'],
                stat_list.iloc[2]['Member Name']))


  # sends the number of services a member attended
  @commands.command(aliases=['sa', 'num'])
  async def service_attended(self, ctx, *,member='Octavio Castro'):

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="2020-2021 Hours!B2:AQ96").execute()

    with open('service_hours.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',')
      for row in result['values']:
        csv_writer.writerow(row)

    num_list = pd.read_csv('service_hours.csv')
    num_list = num_list.fillna(0)
    num_list = num_list.loc[:, (num_list != 0).any(axis=0)]
    num_list.set_index('Member Name', inplace=True)
    dropping = ['Grade', 'Hours Gained', 'Goal', 'Hours Needed']
    num_list = num_list.drop(dropping, axis = 1)

    try:
      count = 0
      for column_num in range(len(num_list.columns)):
          if not(num_list.loc[member][column_num] in [0, '0', '', ' ', None]) :
              count += 1
      await ctx.send("{} has attended {} services.".format(member, count))
    except:
      await ctx.send('```No member with that name exists. Check your spelling and capitalization.\nIf error, DM eojune#3500```')

def setup(client):
    client.add_cog(BuildOn(client))
