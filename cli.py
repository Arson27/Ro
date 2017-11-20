import sys
import mvptracker
import time

tracker_backup_file = 'mvptracker'  # txt file name here
tracker = mvptracker.MvpTracker(tracker_backup_file)

def main():
    command = sys.argv[1]
    if command == "mvp":
        mvpCommand(sys.argv)
    elif command == "mvplist":
        mvpListCommand()
    else:
        mvpHelpCommand()

def mvpCommand(input):
    mvp = input[2]
    input_tod = input[3]
    time_of_death = tracker.from_input_to_seconds(input_tod)
    if tracker.update_death(mvp, time_of_death):  # try to update it
        to_say = "Last known time of death for {} has been updated to: {}".format(mvp, input_tod)
    else:  # if it can't update it, it falls here
        to_say = 'Sorry, I could not understand your request. Try using !mvphelp.'

    print(to_say)

def mvpListCommand():
    to_say = ''
    for monster in tracker.relevant_deaths():
        to_say += '{}: {}~{}\n'.format(monster[0], monster[1], monster[2])
    if len(to_say) == 0:
        to_say = 'The MVP list is currently empty.'
    else:
        to_say = 'Current Server Time: {}\n\n'.format(tracker.display_time(time.time())) + to_say

    print(to_say)

def mvpHelpCommand():
    to_say = '--!mvp -> updates the time of death of an MVP'
    to_say += '\nSyntax: !mvp mvpname timeofdeath; e.g. !mvp Stormy Knight 03:57PM)'
    to_say += '\nFor bosses with multiple spawn locations, use !mvp mvpname '
    to_say += '(location) timeofdeath; e.g. !mvp Atroce (ve_fild02) 02:03AM'
    to_say += '\n--!mvplist -> displays the MVPs that respawned recently or that will respawn in the future.'
    to_say += '\nAll time stamps should be in server time and in HH:MMAM or HH:MMPM format.'
    to_say += '\nThis is a work in progress, currently being developed by @RoundPiano#0630.'

    print(to_say)

main()
