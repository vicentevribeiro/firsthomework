import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
hero_hp = int(input("How much hp does the hero have?\n"))
dragon_hp = int(input("How much hp does the dragon have?\n"))
hero_max_dmg = 20
dragon_max_dmg = 10
health_potion = hero_hp + 10

hero_name = input("What shall the legends call you, brave hero?\n")

print("You venture deep into the caves which legends rumour to be swarmed in monsters, but you've only come for one. The vicious dragon terrorizing your village. Good luck hero")
print("The dragon with", dragon_hp, "hp attacks our hero with", hero_hp, "hp")

# add a While for an infinite block
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    hero_hp = hero_hp - dragon_attack


    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    if dragon_attack == dragon_max_dmg:
        print("CRITICAL HIT")
    # add an if condition to check if the hero was killed by the dragon
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero. RIP sir", hero_name)
    if hero_hp < 10:
        print("Hero! Your health is low! NEAR DEATH BONUS")

        break

    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    dragon_hp = dragon_hp - hero_attack

    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    if hero_attack == hero_max_dmg:
        print("CRITICAL HIT")
    # add an if condition to check if the dragon was killed by the hero
    if dragon_hp <= 0:
        print("Our valiant hero",hero_name, "has slain the dragon!")
        break

    input("Would you like to use your available health potion?")
    if "yes" == hero_hp + 10
        print("You have used your health potion. +10 HEALTH")
    if "no": hero_hp == hero_hp
        print("You have chosen not to use your health potion.")

input("Round over. Press any key")