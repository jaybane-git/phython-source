from classes.game import Person, bcolors
from classes.magic import Spell

# Create Magic Black
fire = Spell("Fire",10,60,'Black')
thunder = Spell("Thunder",10,100,'Black')
blissard = Spell("Blizzard",10,100,'Black')
meteor = Spell("Meteor",20,200,'Black')
quake = Spell("Quake",14,140,'Black')

# Create Magic White
cure = Spell("Cure",12,120,'White')
cura = Spell("Cura",18,200,'White')

'''
magic = [{"name": "Fire", "cost": 10,"dmg": 60},
         {"name": "Thunder", "cost": 12,"dmg": 80},
         {"name": "Blizzard", "cost": 10,"dmg": 60}]
'''

player = Person(460, 65, 60, 34, [fire,thunder,blissard,meteor,cure,cura])

enemy  = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks" + bcolors.ENDC)

while running :
    print("==================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice)-1

    if index ==0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, "points of damage. Enemy HP", enemy.get_hp())
    elif index == 1:
        print("==================")
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) -1
        print("You choose " + magic[magic_choice]["name"])

        magic_dmg = player.generate_spell_damage(magic_choice)
        cost = player.get_spell_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + magic[magic_choice]["name"] + "deals", str(magic_dmg),"points of damage" + bcolors.ENDC )




    enemy_choice =1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for ", enemy_dmg, "points of damage. Player HP", player.get_hp())
    print("--------------------------------")
    print("Enemy HP are "+ bcolors.FAIL + str(enemy.hp) + "/" +str(enemy.get_max_hp()) +bcolors.ENDC)

    print("Your HP: "+ bcolors.OKGREEN + str(player.hp) + "/" +str(player.get_max_hp()) +bcolors.ENDC)

    print("Your MP: " + bcolors.OKBLUE + str(player.mp) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() ==0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Lost" + bcolors.ENDC)
        running = False

'''
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print("Random Magic spell",player.generate_spell_damage(0))
print("Random Magic spell",player.generate_spell_damage(1))
'''