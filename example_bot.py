# -*- coding: utf-8 -*-
"""
Just an example of how to implement the MvpTracker class.

@author: RoundPiano
"""
import discord
import mvptracker
import time

client = discord.Client()
tracker_backup_file = '' #txt file name here
tracker = mvptracker.MvpTracker(tracker_backup_file)
token = '' #insert token here

@client.event
async def on_message(message):

    if message.content.startswith('!mvp '):
        #change the value of the death time
        mvp = ' '.join(message.content.split(' ')[1:-1])
        input_tod = message.content.split(' ')[-1]
        time_of_death = tracker.from_input_to_seconds(input_tod)
        if tracker.update_death(mvp, time_of_death): #try to update it
            to_say = "Last known time of death for {} has been updated to: {}".format(
                    mvp, input_tod)
            await client.send_message(message.channel, to_say)
        else: #if it can't update it, it falls here
            to_say = 'Sorry, I could not undestand your request. Try using !mvphelp.'
            await client.send_message(message.channel, to_say)
            
    elif message.content == '!mvplist':
        #show mvp list
        to_say = ''
        for monster in tracker.relevant_deaths():
            to_say += '{}: {}~{}\n'.format(monster[0], monster[1], monster[2])
        if len(to_say) == 0:
            to_say = 'The MVP list is currently empty.'
        else:
            to_say = 'Current Server Time: {}\n\n'.format(tracker.display_time(time.time())) + to_say
        await client.send_message(message.channel, to_say)
        
    elif message.content.startswith('!mvpclear '):
        #This is a special code used to clear the mvp list and file from within Discord.
        #Not intended to be used by the general public.
        if message.content.split(' ')[-1] == 'ALL123':
            tracker.reset_list()
            await client.send_message(message.channel, 'The MVP list has been cleared.')
        else:
            mvp = mvp = ' '.join(message.content.split(' ')[1:])
            if tracker.update_death(mvp, time_of_death, reset=True):
                await client.send_message(message.channel, 'The MVP has been reset.')
            else:
                await client.send_message(message.channel, 'Sorry,' +
                                          'I could not undestand your request. ' + 
                                          'Try using !mvphelp.')
            
    elif message.content in ['!mvphelp', '!mvp']:
        to_say = '--!mvp -> updates the time of death of an MVP'
        to_say += '\nSyntax: !mvp mvpname timeofdeath; e.g. !mvp Stormy Knight 03:57PM)'
        to_say += '\nFor bosses with multiple spawn locations, use !mvp mvpname '
        to_say += '(location) timeofdeath; e.g. !mvp Atroce (ve_fild02) 02:03AM'
        to_say += '\n--!mvplist -> displays the MVPs that respawned recently or that will respawn in the future.'
        to_say += '\nAll time stamps should be in server time and in HH:MMAM or HH:MMPM format.'
        to_say += '\nThis is a work in progress, currently being developed by @RoundPiano#0630.'
        await client.send_message(message.channel, to_say)
        
client.run(token)
