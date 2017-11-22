print ("Welcome to the RPG combat simulator!")

import random

import time

Player_HP = 100

Player_Mana = 100

Monster_HP = 150

HP_Potions = 3

Mana_Potions = 3

Player_Item = ("None")

Player_Cast = ("None")

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

                Potion_Recovery = random.uniform(20,30)

                Potion_Recovery = int(Potion_Recovery)

                Player_HP = Player_HP + Potion_Recovery

                print ("You recover %s health." % Potion_Recovery)

                HP_Potions = HP_Potions - 1

                print ("You have %s health potions left!" % HP_Potions)

                print ("You now have %s health left." % Player_HP)

            else:

                print ("You are all out of health potions!")

        if Player_Item == ("Mana Potion"):

            if Mana_Potions > 0:

                print ("You drink a mana potion.")

                Mana_Recovery = random.uniform(20,30)

                Mana_Recovery = int(Mana_Recovery)

                Player_Mana = Player_Mana + Mana_Recovery

                print ("You recover %s mana." % Mana_Recovery)

                Mana_Potions = Mana_Potions - 1

                print ("You have %s mana potions left!" % Mana_Potions)

                print ("You now have %s mana left in you." % Player_Mana)

            else:

                print ("You are all out of mana potions!")

    if Player_Action == ("Cast"):

        Player_Cast = input("What spell will you cast?")

        if Player_Cast == ("Fireball"):

            if Player_Mana >= 20:

                print("You cast a fireball!")

                Fireball_Damage = random.uniform(20,35)

                Fireball_Damage = int(Fireball_Damage)

                Monster_HP = Monster_HP - Fireball_Damage

                Player_Mana = Player_Mana - 20

                print("You hit the monster for %s damage!" % Fireball_Damage)

                print("The monster has %s health left!" % Monster_HP)

                print("You have %s mana left in you." % Player_Mana)

            else:

                print("You don't have enough mana.")

        if Player_Cast == ("Regen"):

            if Player_Mana >= 40:

                print("You heal yourself using magic.")

                Regen_Ammount = random.uniform(30,50)

                Regen_Ammount = int(Regen_Ammount)

                print("You heal for %s health." % Regen_Ammount)

                Player_HP = Player_HP + Regen_Ammount

                Player_Mana = Player_Mana - 40

                print("You now have %s health left" % Player_HP)

                print("You now have %s mana left in you" % Player_Mana)
                
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
