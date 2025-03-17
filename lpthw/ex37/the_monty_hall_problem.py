# There are three doors 
# You choose a door at random
# After you make the choice the host will open one of the two doors left
# The door that the host opens always contains a goat 
# Should you change your choice or not 
import random
from random import choice

repetitions = 100000 # variable represent value of repetion of number time is the quiz repeat
number_of_successful_events_with_no_change = 0 # the name define the mean of the variable
number_of_successful_events_with_the_change = 0 # the name define the mean of the variable

for i in range(1,repetitions):#this big part of all thing  make them repeat 99999
    doors = {}# dictionary empty it will be add the 2goat and car 
    prizes = ["goat", "car","goat"]# that the variable by will add  the door
    
    for i in range(1,4):#  *i* is number will represent in future the index and will and because we have 3 variable in prizes
        prize_for_door_i= prizes.pop(random.randrange(len(prizes))) # is *pop* make the variable *prize_for_door_i* get the value of *prizes* by len or the index of variable in len 
        doors[i] = prize_for_door_i# that when the index of door  by the order of i and after get the random prizes

    players_choice = random.randint(1,3)# the choice of the playey between 1 to 3 because this the index in dictionary can be car or goat *
    hosts_removed_door = choice([i for i in range(1,4) if i is not players_choice and doors[i] == "goat"])# is just choose the door who open by random way but                                                         #
                                                                        #it should be not the choose of player and equal goat
    
    door_left = choice([i for i in range (1,4) if i is not players_choice and i is not hosts_removed_door])


    if doors[players_choice] == "car":
        number_of_successful_events_with_no_change += 1 

    if doors[door_left] == "car":
        number_of_successful_events_with_the_change += 1 

print("Win percentage with change:", number_of_successful_events_with_the_change/repetitions)
print("Win percentage with no change:", number_of_successful_events_with_no_change/repetitions)