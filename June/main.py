import discord
import os
import random
from datetime import date
from datetime import datetime
from discord.ext import commands
from everlasting import everlasting

# google sheets
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import csv
import json
import pandas as pd


images = ['profiles/1.png', 'profiles/2.png', 'profiles/3.png', 'profiles/4.png',  'profiles/5.png',  'profiles/6.png',  'profiles/7.png',  'profiles/8.PNG',  'profiles/9.PNG',  'profiles/10.PNG',  'profiles/404.PNG']

#sheet code start
client = commands.Bot(command_prefix='cs!')

client.remove_command('help')
client.remove_command("portfolio")

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(os.environ['JSON_KEY']), scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1AonI_YS0Gi31TYPIWRcpzfUkEao6P6ZRS5okPRCLtAM'

service = build('sheets', 'v4', credentials=creds)

 #sheet code end

# tells when ready
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game('Use cs!help to see commands'))
    print('Bot is ready.')

# sends a message saying that the command does not exist
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No such command. Enter `cs!help` for a list of commands.")
    else:
        print(error)

# sends a message explaining the commands
@client.command(aliases=['ayuda', 'halp', 'HELP', 'Help'])
async def help(ctx):
    descrip = "\n1) `cs!projects` - show a list of projects\n2) `cs!events` - show a list of planned events, like hackathons or game jams\n3) `cs!month` - show the month's schedule"
    emb = discord.Embed(title="Commands", description=descrip, color=2123412)
    await ctx.channel.send(embed=emb)

# assign a role
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 874797444939014154:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        print(payload.emoji.name)
        if payload.emoji.name == '🧑‍🔬':
            role = discord.utils.get(guild.roles, name='scientist')
        elif payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='gameDevs')
        elif payload.emoji.name == '🌐':
            role = discord.utils.get(guild.roles, name='webDevs')
        elif payload.emoji.name == '📊':
            role = discord.utils.get(guild.roles, name='data science')
        elif payload.emoji.name == '🧑‍💻':
            role = discord.utils.get(guild.roles, name='technician')
        elif payload.emoji.name == '📱':
            role = discord.utils.get(guild.roles, name='mobileDevs')
        elif payload.emoji.name == '📖':
            role = discord.utils.get(guild.roles, name='learners')
        else:
            role = None

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                members_roles = [ i.name for i in member.roles ]
                if 'officers' not in list(members_roles):
                    await member.add_roles(discord.utils.get(guild.roles, name='members'))
                print("Member has been added a role")
            else:
                print("Member not found.")
        else:
            print("No role found")


# remove a role
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 874797444939014154:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '🧑‍🔬':
            role = discord.utils.get(guild.roles, name='scientist')
        elif payload.emoji.name == '🎮':
            role = discord.utils.get(guild.roles, name='gameDevs')
        elif payload.emoji.name == '🌐':
            role = discord.utils.get(guild.roles, name='webDevs')
        elif payload.emoji.name == '📊':
            role = discord.utils.get(guild.roles, name='data science')
        elif payload.emoji.name == '🧑‍💻':
            role = discord.utils.get(guild.roles, name='technician')
        elif payload.emoji.name == '📱':
            role = discord.utils.get(guild.roles, name='mobileDevs')
        elif payload.emoji.name == '📖':
            role = discord.utils.get(guild.roles, name='learners')
        else:
            role = None

        if role is not None:
            member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if role is not None:
              await member.remove_roles(role)
              print("Role removed")
        else:
            print("No role found")

# cs!projects - show a list of current projects (or just project)
@client.command()
async def projects(ctx):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="CurrentProjects!A1:C24").execute()

    with open('CSV/current_projects.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',')
      for row in result['values']:
        csv_writer.writerow(row)

    stat_list = pd.read_csv('CSV/current_projects.csv')
    stat_list = stat_list.fillna(0)
    stat_list = stat_list[['Member', 'Category', 'Project Link']]

    dates = " "
    types = " "
    names = " "

    for x in range(len(stat_list.index)):
        dates += stat_list['Project Link'].iloc[x] + "\n"
        types += stat_list['Category'].iloc[x] + "\n"
        names += stat_list['Member'].iloc[x] + "\n"
    
    if len(stat_list.index) == 0:
      emb = discord.Embed(title="Current Projects", color=15418782, description = "There are no current projects.")
      await ctx.channel.send(embed=emb)
    else:
      emb = discord.Embed(title="Current Projects", color=15418782)
      emb.add_field(name="Member", value=names, inline=True)
      emb.add_field(name="Category", value=types, inline=True)
      emb.add_field(name="Project Link", value=dates, inline=True)

      await ctx.channel.send(embed=emb)


# send 5 events, 1 from the past, 4 from the future
@client.command()
async def events(ctx):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Events!A1:F100").execute()

    with open('CSV/event_days.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',')
      for row in result['values']:
        csv_writer.writerow(row)
    stat_list = pd.read_csv('CSV/event_days.csv', header=0)
    stat_list = stat_list.dropna(0)
    stat_list = stat_list[['Date', 'Day', 'Time', 'Type', 'Name', 'Hidden']]
    stat_list = stat_list[stat_list["Hidden"] == False]
    stat_list["Date"] = pd.to_datetime(stat_list["Date"], format="%m/%d/%Y")
    stat_list.reset_index(drop=True, inplace=True)

    emb = discord.Embed(title="Upcoming Events", color=3066993)

    current_date = datetime.now()
    all_dates = stat_list['Date'].to_list()
    starting_index = 0
    # store the index of the event that is before today’s date
    for i, data in enumerate(all_dates):
      if current_date < data:
        starting_index = i - 1
        if starting_index == -1:
          starting_index = 0
        break
    stat_list = stat_list.iloc[starting_index:]
    dates = ""
    types = ""
    names = ""

    stat_list.reset_index(drop=True, inplace=True)
    for x in range(5):
        dates += str(stat_list['Date'].iloc[x].date().month) +"/"+ str(stat_list['Date'].iloc[x].date().day) + " (" + stat_list['Day'].iloc[x]  + ")\n"
        types += stat_list['Type'].iloc[x] + "\n"
        names += stat_list['Name'].iloc[x] + "\n"

    emb.add_field(name="Date", value=dates, inline=True)
    emb.add_field(name="Type", value=types, inline=True)
    emb.add_field(name="Name", value=names, inline=True)
    await ctx.channel.send(embed=emb)

  
# change pfp
last_time_changed = datetime.now()
previous_pfp = "profiles/2.png"

@client.command()
async def pfp(ctx):
    try:
      members_roles = [ i.name for i in ctx.message.author.roles ]
      if 'officers' not in list(members_roles):
          await ctx.send("You can't use this command.")
      else:
        global last_time_changed
        global previous_pfp
        current_time = datetime.now()
        difference = current_time - last_time_changed
        if difference.total_seconds() / 60 < 15:
            if 15 - difference.total_seconds() / 60 <= 0:
              await ctx.send(f"Try again in {round(difference.total_seconds(), 2)} minutes.")
            else:
              await ctx.send(f"Try again in {int(15 - difference.total_seconds() / 60)} minutes.")
        else:
            decided_pfp = random.choice(images)
            while decided_pfp == previous_pfp:
              decided_pfp = random.choice(images)
            last_time_changed = current_time
            with open(decided_pfp, 'rb') as image:
              await client.user.edit(avatar=image.read())
            previous_pfp = decided_pfp
            await ctx.send("Done, changed to ", file=discord.File(decided_pfp))
        
    except Exception as e:
        print(e)
        await ctx.send("Something has gone wrong. Alert EOjune please.")

# send 5 events from this month
@client.command()
async def month(ctx):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Events!A1:F100").execute()

    with open('CSV/event_days.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',')
      for row in result['values']:
        csv_writer.writerow(row)

    stat_list = pd.read_csv('CSV/event_days.csv')
    stat_list = stat_list.fillna(0)
    stat_list = stat_list[['Date', 'Day','Time', 'Type', 'Name', 'Hidden']]
    stat_list["Date"] = pd.to_datetime(stat_list["Date"], format="%m/%d/%Y")
    stat_list = stat_list[stat_list["Hidden"] == False]

    current_date = date.today()
    # store the index of the event that is before today’s date
    stat_list = stat_list[stat_list["Date"].dt.month == current_date.month ]
    stat_list.reset_index(drop=True, inplace=True)
    dates = ""
    types = ""
    names = ""
    for x in range(len(stat_list)):
        if stat_list['Date'].iloc[x].date() < current_date: 
          dates += "*" + str(stat_list['Date'].iloc[x].date().month) +"/"+ str(stat_list['Date'].iloc[x].date().day) + " (" + stat_list['Day'].iloc[x]  + ")*\n"
          types += "*" + stat_list['Type'].iloc[x] + "*\n"
          names += "*" + stat_list['Name'].iloc[x] + "*\n"
        else:
          dates += str(stat_list['Date'].iloc[x].date().month) +"/"+ str(stat_list['Date'].iloc[x].date().day) + " (" + stat_list['Day'].iloc[x]  + ")\n"
          types += stat_list['Type'].iloc[x] + "\n"
          names += stat_list['Name'].iloc[x] + "\n"

    if len(stat_list) == 0:
      emb = discord.Embed(title="Events for this month", color=11342935, description="There are no events for this month.")
    else:
      emb = discord.Embed(title="Events for this month", color=11342935)
      emb.add_field(name="Date", value=dates, inline=True)
      emb.add_field(name="Type", value=types, inline=True)
      emb.add_field(name="Name", value=names, inline=True)
  
    await ctx.channel.send(embed=emb)



everlasting()
token = os.environ.get("key")
client.run(token)