print ("Welcome to the RPG combat simulator!")

import random

import time

Player_HP = 100

Monster_HP = 75

HP_Potions = 3

Vigor_Potions = 3

while Player_HP > 0 and Monster_HP > 0:

    Player_Action = input("What will you do?")

    if Player_Action == ("Attack"):

        Player_Damage = random.uniform(10,15)

        Player_Damage = int(Player_Damage)

        print ("You dealt %s damage!" % Player_Damage)

        Monster_HP = Monster_HP - Player_Damage

        print ("The monster has %s health left!" % Monster_HP)

    if Player_Action == ("Block"):

        Player_Block = random.uniform(4,8)

        Player_Block = int(Player_Block)

        print ("You brace yourself...")

    if Player_Action == ("Use"):

        Player_Item = input("What item wil you use?")

        if Player_Item == ("HP Potion"):

            if HP_Potions > 0:

                print ("You drink a health potion.")

                Potion_Recovery = random.uniform (20,30)

                Potion_Recovery = int(Potion_Recovery)

                Player_HP = Player_HP + Potion_Recovery

                print ("You recover %s health." % Potion_Recovery)

                Potions = Potions - 1

                print ("You have %s potions left!" % Potions)

                print ("You now have %s health left." % Player_HP)

            else:

                print ("You are all out of potions!")

        if Player_Item == ("Vigor Potion"):

            if Vigor_Potions > 0:

                print ("You drink a vigor potion.")

                
        
    if Monster_HP <= 0:

        break

    print ("Get Ready!")

    time.sleep(2)

    Monster_Damage = random.uniform(5,20)

    Monster_Damage = int(Monster_Damage)

    print ("The monster hit you for %s damage!" % Monster_Damage)

    if Player_Action == ("Block"):

        print ("However, you block for %s damage!" % Player_Block)

        Player_HP = Player_HP - Monster_Damage + Player_Block

    else:

        Player_HP = Player_HP - Monster_Damage

    print ("You have %s health left!" % Player_HP)

    if Player_HP <= 0:

        break

    print ("Compose yourself.")

    time.sleep(3)

if Monster_HP <= 0:

    print ("Huzzah! The foul beast is slain!")

if Player_HP <= 0:

    print ("Your journey has come to a painful, sombre end...")
