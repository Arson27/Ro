# mvp-bot
Ragnarok Online MVP bot for Discord  
Written in python 3.6

Files in the module:  
mvptracker.py -> Main module. Contains class MvpTracker, which is used to interact with the bot.  
mvp.py -> Contains class Mvp and lower methods and functions.  
mvp_properties.py -> A bunch of lists containing different properties of MVPs. Used to generate the mvp list and the initial back up file.  

This program generates a back up file, that is restored on start up. The name of that file is defined on the initialization of the MvpTracker object.  

Required modules:  
discord.py  (Discord API)  
string (built-in)  
time (built-in)  
os (built-in)  

/Created by RoundPiano
