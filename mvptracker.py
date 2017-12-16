# -*- coding: utf-8 -*-
"""
The main module of the MVP tracking functionality.

@author: RoundPiano
"""

import os
import time
#import MvpTracker.mvp as mvp
import mvp

class MvpTracker():
    
    def __init__(self, mvp_file):
        self.mvp_file = mvp_file #this is the hard storage (backup) file. 
        self.list_of_mvps = []
        with open(self.mvp_file, 'r') as file:
            for line in file:
                self.list_of_mvps.append(mvp.pack_to_class(line))
            
    def update_death(self, monster_name, time_of_death, reset=False):
        """Updates time of death of a monster. reset=True is only used if we
           want to allow the user to set a time stamp.
           Returns a boolean False if the update was complete, else True. This
           can be used to check what response to give to the user."""
        if self.find_monster(monster_name) != None:
            monster = self.find_monster(monster_name)
        else:
            return False
        if monster.update_time_of_death(time_of_death, reset):
            with open('{}.tmp'.format(self.mvp_file), 'w') as temp_file:
                for boss in self.list_of_mvps:
                    temp_file.write('{}\n'.format(boss.unpack()))
            if os.path.exists('old_{}'.format(self.mvp_file)):
                os.remove('old_{}'.format(self.mvp_file))
            os.rename(self.mvp_file, 'old_{}'.format(self.mvp_file))
            os.rename('{}.tmp'.format(self.mvp_file), self.mvp_file)
            return True
        return False
            
    def from_input_to_seconds(self, input_time, before=True):
        """Takes a 24 hours 'HH:MM' string and returns an int seconds since epoch"""
        #note: I didn't do extensive testing on this. It might return wrong results in edge cases.
        hour = int(input_time.split(':')[0])
        minute = int(input_time.split(':')[1][:2])
                
        current_instant = self.current_time()
        current_time = self.display_time(current_instant)
        current_hour = int(current_time.split(':')[0])
        current_minute = int(current_time.split(':')[1][:2])
        
        target_time = current_instant 
        #find most recent past time that fits the input
        target_time -= (current_hour - hour) * 60 * 60
        target_time -= (current_minute - minute) * 60
        return target_time
   
    def relevant_deaths(self):
        """Returns a list of monsters who respawned recently or will respawn in the future."""
        monsters_to_show = []
        now_time = self.current_time()
        for monster in self.list_of_mvps:
            if monster.next_respawn_max > now_time - 30*60: #30 minutes ago or sooner
                monsters_to_show.append([monster.display_name,
                                        self.display_time(monster.next_respawn_min),
                                        self.display_time(monster.next_respawn_max)])
        return monsters_to_show
    
    def reset_list(self):
        """Reinitializes the backup file."""
        mvp.reset_file()
        self.__init__(self.mvp_file)
        
    def display_time(self, secs):
        """Converts time since epoch in seconds to string in HH:MMAM format."""
        secs = int(secs)
        secs += 60 * 60 * - 8 #8 hours before UTC aka server time
        hour = time.gmtime(secs)[3]
        if time.gmtime(secs)[4] < 10:
            #18:1 -> 18:01
            minute = '0' + str(time.gmtime(secs)[4])
        else:
            minute = time.gmtime(secs)[4]
        return '{}:{}'.format(hour, minute)
    
    def find_monster(self, name):
        for monster in self.list_of_mvps:
            if monster.display_name.lower() == name.lower():
                return(monster)
                
    def clear_monster(self, name):
        """Resets a monster to the starting time of death."""
        self.update_death(name, 0, reset=True)
        
    def current_time(self):
        return int(time.time())
