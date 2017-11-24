print ("Welcome to the RPG combat simulator!")

import random

import time

#Player_HP represents the ammount of health the player (ie, you) has, if it falls to zero, you lose.
Player_HP = 100

#Player_Mana represents the ammount of mana you have, mana is used to cast spells.
Player_Mana = 100

#MonsterHP represents the ammount of health the monster has, if it falls to zero, you win.
Monster_HP = 150

#HP_Potions represents the ammount of health recovery potions you have.
HP_Potions = 3

#Mana_Potions represents the ammount of mana recovery potions you have.
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

        #Typing in "Attack" will deal between 10 to 15 damage to the monster.

    if Player_Action == ("Block"):

        Player_Block = random.uniform(4,8)

        Player_Block = int(Player_Block)

        print ("You brace yourself...")

        #Typing in "Block" will reduce 4 to 8 damage from the monsters next attack.

    if Player_Action == ("Use"):

        #Typing in "Use" will use an item of your choice.

        Player_Item = input("What item wil you use?")

        #

        if Player_Item == ("HP Potion"):

            if HP_Potions > 0:

                print ("You drink a health potion.")

                Potion_Recovery = random.uniform(20,30)

                Potion_Recovery = int(Potion_Recovery)

                Player_HP = Player_HP + Potion_Recovery

                print ("You recover %s health." % Potion_Recovery)

                HP_Potions = HP_Potions - 1

                print ("You have %s health potions left!" % HP_Potions)

                if Player_HP > 100:

                    Player_HP = 100

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

                if Player_Mana > 100:

                    Player_Mana = 100

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

    if Player_Action == ("Star Platinum!!!"):

        print("ORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORA!!!!!!!!!!")

        time.sleep(1.5)

        STAR_PLATINUM = random.uniform(100,150)

        STAR_PLATINUM = int(STAR_PLATINUM)

        Monster_HP = Monster_HP - STAR_PLATINUM

        print("You used Star Platinum to pummel the monster for %s damage!!!" % STAR_PLATINUM)

        print("The monster has %s health left!" % Monster_HP)

    if Player_Action == ("Killer Queen!!!"):

        print("BITEZ ZA DUSTO!!!")

        time.sleep(0.5)

        print("*Click.*")

        time.sleep(0.75)

        print("BOOM!!!")

        BITEZ_ZA_DUSTO = random.uniform(50,75)

        BITEZ_ZA_DUSTO = int(BITEZ_ZA_DUSTO)

        Monster_HP = Monster_HP - BITEZ_ZA_DUSTO

        print("The bomb dealt %s damage to the monster!" % BITEZ_ZA_DUSTO)

        time.sleep(2)

        print("I... I did it! It activated!")

        time.sleep(1)

        Player_HP = Player_HP + BITEZ_ZA_DUSTO

        if Player_HP > 100:

            Player_HP = 100

        print("You rewind a brief period back in time but the damage done the monster is still there, due to this you also heal %s damage from yourself!" % BITEZ_ZA_DUSTO)

        print("You have %s health left." % Player_HP)

        print("The monster has %s health left." % Monster_HP)

    if Player_Action == ("The World!!!"):

        print("ZA WARUDO!!! Stop Time!!!")

        time.sleep(0.5)

        print("Time has stoped.")

        time.sleep(3)

        print("One second has elapsed...")

        time.sleep(2)

        print("Two seconds have elapsed...")

        time.sleep(2)

        print("Three seconds have elapsed.")

        time.sleep(2)

        print("Four seconds have elapsed...")

        time.sleep(2)

        print("Five seconds have elapsed...")

        time.sleep(2)

        print("Six seconds have elapsed...")

        time.sleep(2)

        print("Seven seconds have elapsed...")

        time.sleep(2.5)

        print("...")

        time.sleep(1)

        print("ROAD ROLLER!!!!!!!!!!")

        time.sleep(1.5)

        print("CRASH!!!!!!!")

        time.sleep(1)

        print("MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!! MUDA!!!") 

        print("EIGHT SECONDS HAVE ELAPSED!!!")

        time.sleep(1)

        print("WWRRYYYYYYYYYY!!!!!!")

        time.sleep(1)

        print("I'LL SMASH YOU FLAT!!!")

        time.sleep(1)

        print("*SMASH!!!*")

        ZA_WARUDO = random.uniform(500,1000)

        ZA_WARUDO = int(ZA_WARUDO)

        print('In the end, "The World" had dealt %s damage to the mosnter!' % ZA_WARUDO)

        Monster_HP = Monster_HP - ZA_WARUDO

        print("The monster has %s HP left." % Monster_HP)       
                
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
