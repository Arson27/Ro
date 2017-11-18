# -*- coding: utf-8 -*-
"""
Contains the class Mvp, which contains the MVP properties and a few methods.

@author: RoundPiano
"""

import os
import time
from mvp_properties import *

class Mvp():
    
    def __init__(self, id_number, display_name,
                 respawn_min, respawn_max, time_of_death, locations=None, names=None):
        self.line_number = int(id_number)
        self.display_name = display_name
        if names == None:
            self.names = [self.display_name] #currently unused
        self.respawn_min = int(float(respawn_min))
        self.respawn_max = int(float(respawn_max))
        self.locations = locations #currently unused
        if int(time_of_death) > self.current_time():
            print('Something wrong happened. ERROR_CODE_13')
            self.time_of_death = 0
        elif int(time_of_death) + self.respawn_max < self.current_time() + 60*60:
            self.time_of_death = 0
        else:
            self.time_of_death = int(time_of_death)
        self.next_respawn_min = self.time_of_death + self.respawn_min
        self.next_respawn_max = self.time_of_death + self.respawn_max
    
    def unpack(self):
        return '{},{},{},{},{}'.format(self.line_number, self.display_name,
                                       self.respawn_min, self.respawn_max,
                                       self.time_of_death)
    
    def update_time_of_death(self, new_time_of_death, reset=False):
        if new_time_of_death > self.current_time():
            return False
        elif new_time_of_death < self.time_of_death and not reset:
            return False
        else:
            self.time_of_death = int(new_time_of_death)
            self.next_respawn_min = self.time_of_death + self.respawn_min
            self.next_respawn_max = self.time_of_death + self.respawn_max
            return True
        
    def current_time(self):
        return int(time.time())
    


default_time = 0

#Debugging only.
#mvp_list = [Mvp(i, mvp_names[i], mvp_respawn_min[i], mvp_respawn_max[i],
#                default_time, mvp_location[i]) for i in range(len(mvp_names))]

def reset_file():
    """Makes the backup file or restores it to the starting settings."""
    with open('mvp_list_file.txt', 'w') as file:
        for mvp in mvp_list:
            file.write('{},{},{},{},{}\n'.format(mvp.line_number, mvp.display_name,
                                                 mvp.respawn_min, mvp.respawn_max,
                                                 default_time))
            
def pack_to_class(line):
    info = line.split(',')
    return Mvp(info[0], info[1], info[2], info[3], info[4])

def start_file_and_list():
    """Initializes the backup file and list mvp_list if they don't exist yet."""
    if not os.path.exists('mvp_list_file.txt'):
        mvp_list = [Mvp(i, mvp_names[i], mvp_respawn_min[i], mvp_respawn_max[i],
                        default_time, mvp_location[i]) for i in range(len(mvp_names))]
        reset_file()
    else:
        mvp_list = []
        with open('mvp_list_file.txt', 'r') as file:
            for line in file:
                mvp_list.append(pack_to_class(line))
                
start_file_and_list()