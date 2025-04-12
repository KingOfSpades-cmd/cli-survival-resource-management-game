
This is a resource management game where the *player* has to manage *resources* 

class construction
Resources: 
- Notes: the resources will have to be connected to the player, so lets make them food, water, energy.
- Attributes: What could be its attributes? its quantity and its value(how much does it replenish)

Player: the player can get hungry, thirsty, sleepy and weak 
- Attributes: name, state(hungry, thirsty, tired,) Alive = true, health out of 100

Actions: the player will have to scavange for food, collect water and sleep


**Classes**
1. Player
    - Attributes
        - Plahd
    - Actions
        - Plahd 
2. Resources
    - Attributes
        - Plahd
    - Actions
        - Plahd


resources need to replenish hunger, thirst and sleep, they also need to replenish it by some amount random amount, they could also be spoiled or poisoned making you lose some health or energy or both 

def scavange_food(self, food):
    food_item = {"burger":20, "banana":5, "beans":10, "candy":1}
    if player selects scavange for food:
        get food item.random

    for value in food_item.items: 
        self.inventory.append(food) # i am unsure if its best to use a dictionary but i think it makes sense in this case how else could i provide the food with the necessary quantity

    also need some code to randomly select if a food is poisonous (very rare) when the player collects it and to take away healthy by 1 to 5 points which i dont know what to do 

def collect_water(self, water):
    water = {water:10} # unsure if its best to use a dictionary in this case, i just want the water item to self.thirst -= 10 this also means we need to find a way to make sure any of the attributes dont go into the negatives
    if user selects water:
        self.thirst += random(range(3, 20)) # if the user selects to collect water, add a random number between 3 and 20 and add it to the thirst

    for key in food_item: 
        self.inventory.append(food)

    also need some code to randomly select if a food is poisonous (very rare) when the player collects it and to take away healthy by 1 to 5 points which i dont know what to do


.# we also need to find a way to update the stats each day since the gameplay loop is new day starts => energy is reduced by some number (by 5 or 2.5) => player is asked if they would like to sleep, scavenge, collect water (if user chooses scavenge or collect water they lose some amount of energy like 20) so the user can do like some number of tasks a day like 1 or 2 and also take from thier inventory if they have any saved resources. The player can also check thier inventory and take from it every time, this wont be counted as a limited action like sleeping or collecting water  

Launch timeline
[] Make sure Git ignores this file
[] Remove the AI generated comments
[] Ask Co-pilot to do the documentation and commenting for the document

Next issues:
1. solve this error you got in the terminal "Traceback (most recent call last):
  File "c:\Users\USER\Documents\Coding stuff\CLI-resource-management-game\script.py", line 60, in <module>
    player.collect_water()
  File "c:\Users\USER\Documents\Coding stuff\CLI-resource-management-game\script.py", line 60, in <module>
    player.collect_water()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "c:\Users\USER\Documents\Coding stuff\CLI-resource-management-game\game_logic_and_backend.py", line 146, in collect_water
    self.inventory.append(found_water)
                          ^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'found_water' where it is not associated with a value
(project-1)"
2. Find a way to get medkits and energy drinks randomly as you search for food and water they need to be rare like you only get them 1/10 the time: if i am correct this is a code block we just need to create once then put in the methods for scavange_food and collect_water