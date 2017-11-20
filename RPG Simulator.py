print ("Welcome to the RPG combat simulator!")

import random

import time

Player_HP = 100

Monster_HP = 75

while Player_HP > 0 and Monster_HP > 0:

    Player_Action = input("What will you do?")

    if Player_Action == ("Attack"):

        Player_Damage = random.uniform(10,15)

        Player_Damage = int(Player_Damage)

        print ("You dealt %s damage!" % Player_Damage)

        Monster_HP = Monster_HP - Player_Damage

        print ("The monster has %s health left!" % Monster_HP)

    print ("Brace for combat!")

    time.sleep(2)

    Monster_Damage = random.uniform(5,20)

    Monster_Damage = int(Monster_Damage)

    print ("The monster hit you for %s damage!" % Monster_Damage)

    Player_HP = Player_HP - Monster_Damage

    print ("You have %s health left!" % Player_HP)

    print ("Compose yourself.")

    time.sleep(3)

    
