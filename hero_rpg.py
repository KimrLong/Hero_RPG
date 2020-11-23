#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character():
    def __init__(self, health, power, gold):
        super().__init__(self, health, power, gold)
        self.health = health
        self.power = power
        self.gold = gold

    def alive(self):
        if self.health > 0 :
            return True
        else:
            return False

    def attack(self, enemy):
        if(enemy.character_name != "zombie"):
            enemy.health -= self.power

        elif(self.character_name == "hero"):
            print(f'Hero does {self.power} damage to the {enemy.character_name}.')
        else:
            print(f"The {self.character_name} does {self.power} damage to the hero.") 
#write elif for individual actions
    def receive_damage(self, points):
        self.health -= points
        print(f"{self.character_name} received {self.points} damage.")


    def print_status(self):
        if(self.character_name == "hero"):
            print(f"You have {self.health} health and {self.power} power.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")

            
class Hero(Character):
    def __init__(self, health, power, gold):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power, gold)
    def restore(self, health):
        self.health = 10
        print("Hero is back in action! Health is retored to {self.health}!")
    def purchase(self, item):
        self.gold -= item.cost
        item.apply(hero)
    
class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power) 

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power)

class Alchemist(Character):
    def __init__(self, health, power):
        self.character_name = "alchemist"
        super(Alchemist, self).__init__(health, power)

class Necromancer(Character):
    def __init__(self, health, power):
        self.character_name = "necromancer"
        super(Necromancer, self). __init__(health, power)
    # def attack(self, enemy):
    #        swap_power = random.random() > 0.5
    #    if swap_power:
    #        print("{} swaps power with {} during attack".format(self.name, enemy.name))
    #        self.power, enemy.power = enemy.power, self.power
    #    super(Wizard, self).attack(enemy)

hero = Hero(10, 5, 100)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)
alchemist = Alchemist(9, 2)
necromancer = Necromancer(11, 4)

class Potion(object):
    def__init__(self, gold, name):
        self.gold = 3
        self.name = tonic
    def apply(self, hero):
        hero.health += 2
        print("{hero.tonic}'s health is up to {hero.health}")
class Weapon(object):
    def__init__(self, gold, name):
        self.gold = 6
        self.name = dagger
    def apply(self, hero):
        hero.power += 3
        print("{hero.dagger}'s power increased to {hero.power}!")
class Store(object):
    def__init__(self, items):
        Store.items => [Potion, Weapon]
    self.items = [Potion, Weapon]
    def shopping(self, hero):
        # while True:
        #     print("Welcome, you have {hero.gold}.")
        #     print("What would you like to do?")
        #     for i in range(len(Store.items)):
        #         item = Store.items[i]
        #         print("{i+1}. buy {item.name}({item.cost})")
        #     print("7. leave store")
        #     input = int(input(">"))
        #     if input == 10:
        #         break
        #     else:
        #         Purchase = Store.items[input - 1]
        #         item = Purchase()
        #         hero.item

    

        
        

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

main(enemy)

# #!/usr/bin/env python

# # In this simple RPG game, the hero fights the goblin. He has the options to:

# # 1. fight goblin
# # 2. do nothing - in which case the goblin will attack him anyway
# # 3. flee

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()