#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, health, power, coins):
        super().__init__(self, health, power, coins)
        self.health = health
        self.power = power
        self.coins = coins

    def alive(self):
        if self.health > 0 :
            return True
        else:
            return False

    def attack(self, enemy):

        if(enemy.character_name != "zombie"):
            enemy.health -= self.power

        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        else:
            print(f"The {self.character_name} does {self.power} damage to you.") 
#write elif for individual actions

    def print_status(self):
        if(self.character_name == "hero"):
            print(f"You have {self.health} health and {self.power} power.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")

            
class Hero(Character):
    def __init__(self, health, power, coins):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power, coins)
    
class Goblin(Character):
    def __init__(self, health, power, coins):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power, coins) 

class Zombie(Character):
    def __init__(self, health, power, coins):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power, coins)

class Alchemist(Character):
    def __init__(self, health, power, coins):
        self.character_name = "alchemist"
        super(Alchemist, self).__init__(health, power, coins)

class Necromancer(Character):
    def __init__(self, health, power, coins):
        self.character_name = "necromancer"
        super(Necromancer, self). __init__(health, power, coins)


hero = Hero(10, 5, 100)
goblin = Goblin(6, 2, 0)
zombie = Zombie(10, 1, 0)
alchemist = Alchemist(9, 2, 0)
necromancer = Necromancer(11, 4, 0)

def main(enemy):
    

    while enemy.alive() > 0 and hero.alive() :
    
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # # Hero attacks enemy
            hero.attack(enemy)
            # print("You do {} damage to the enemy.".format(hero.power))
            if not enemy.alive():
                print("The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():

            enemy.attack(hero)

            # print("The enemy does {} damage to you.".format(enemy.power))

            if not hero.alive():
                print("You are dead.")

main(zombie)
