# Monty Hall problem
Description:This program is designed to verify Monty Hall problem in computer.

### About Monty Hall problem:
<img height="250" src=".\three_door.png" width="500"/>
In the problem, you are on a game show, being asked to choose between three 
doors. Behind each door, there is either a car or a goat. You choose a door.
The host, Monty Hall, picks one of the other doors, which he knows has a goat
behind it, and opens it, showing you the goat. (You know, by the rules of the
  game, that Monty will always reveal a goat.) Monty then asks whether you
  would like to switch your choice of door to the other remaining door. 
Assuming you prefer having a car more than having a goat, do you choose to 
switch or not to switch?

The program should take three parameters:

    * round(int, default=1000) -r： define the times that are run to get a statistic result.  
    * doors_number(int, default=3) -d: the number of doors are created
    * door_you_choose(int, default=1) -c: choose a door index which should less then doors number

This program can be used by:
    
    python main.py -r 1000 -d 10 -c 1

The program should return several result:


### Table

    * times that you won/lost a car when you don't change your mind
    * times that you won/lost a car when you change your mind

### Possibility

    * possibility that you won a car when you change your mind




Structure:  
1. Each instance represents a door. User can define to create how many 
doors are created, the default is three. 
2. the attribute of class need to have: 
   * is_chosen(True and False): to define if the instance has been chosen at the first time, only one instance is True
   * car_goat(True and False):  to define if the instance has car or goat(randomly assigned to instance, only one instance can be True)



