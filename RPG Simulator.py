#RPG Simulator, Made by Ethan "RoyalRedBird" Powell, Finalized on November 28, 2017.

import random

import time

print ("Welcome to the RPG combat simulator!")

time.sleep(0.5)

print("You are wandering through the woods when all of a suddden a ravenous monster leaps out of nowhere looking for his next kill!")

time.sleep(0.5)

print("And it appears that there is no other choice but to fight it...")

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

#While the HP of the Player or the Monster remains above zero, everything in the while loop will continue to play until either
#the player or the monster... Bites the dust...

while Player_HP > 0 and Monster_HP > 0:

    Player_Action = input('What will you do? You can either "Attack", "Block", "Use" an item or "Cast" a spell.')

    #Player_Action will ask the player what he/she will do with a text prompt.

    if Player_Action == ("Attack"):

        #Typing in "Attack" will deal between 10 to 15 damage to the monster.

        Player_Damage = random.uniform(10,15)

        Player_Damage = int(Player_Damage)

        print ("You dealt %s damage!" % Player_Damage)

        Monster_HP = Monster_HP - Player_Damage

        print ("The monster has %s health left!" % Monster_HP)


    if Player_Action == ("Block"):

        #Typing in "Block" will reduce 4 to 8 damage from the monsters next attack.

        Player_Block = random.uniform(4,8)

        Player_Block = int(Player_Block)

        print ("You brace yourself...")
        

    if Player_Action == ("Use"):

        #Typing in "Use" will use an item of your choice.

        print("You have %s HP Potions left." % HP_Potions)

        print("You have %s potions left." % Mana_Potions)

        Player_Item = input('What item wil you use? You can use an "HP Potion" or a "Mana Potion".')

        #Player_Item will ask the player what he/she wants to use with a text prompt.

        if Player_Item == ("HP Potion"):

            #Typing in "HP Potion" will consume an HP Potion (provided that you have at least one), regenerating 20 to 30 health.

            if HP_Potions > 0:

                #If you don't have any HP Potions, it will do nothing.

                print ("You drink a health potion.")

                Potion_Recovery = random.uniform(20,30)

                Potion_Recovery = int(Potion_Recovery)

                Player_HP = Player_HP + Potion_Recovery

                print ("You recover %s health." % Potion_Recovery)

                HP_Potions = HP_Potions - 1

                print ("You have %s health potions left!" % HP_Potions)

                if Player_HP > 100:

                    #If the ammount of HP regenerated brings your total HP above 100, it will reset your health to 100.

                    Player_HP = 100

                print ("You now have %s health left." % Player_HP)

            else:

                #The following text is printed if you attenmt to use an HP Potion when you don't have any.

                print ("You are all out of health potions!")

        if Player_Item == ("Mana Potion"):

            #Typing in "Mana Potion" will consume a mana potion (if you have one), regenerating 20 to 30 mana.

            if Mana_Potions > 0:

                #If you have zero mana potions, nothing happens.

                print ("You drink a mana potion.")

                Mana_Recovery = random.uniform(20,30)

                Mana_Recovery = int(Mana_Recovery)

                Player_Mana = Player_Mana + Mana_Recovery

                print ("You recover %s mana." % Mana_Recovery)

                Mana_Potions = Mana_Potions - 1

                print ("You have %s mana potions left!" % Mana_Potions)

                if Player_Mana > 100:

                    #If the ammount of mana regenerated brings your total mana above 100, it will reset the mana value to 100.

                    Player_Mana = 100

                print ("You now have %s mana left in you." % Player_Mana)

            else:

                #The following text is printed if you try to use a mana potion without having any.

                print ("You are all out of mana potions!")
                

    if Player_Action == ("Cast"):

        #Typing in "Cast" will cast a spell of your choice.

        print("You have %s mana left." % Player_Mana)

        Player_Cast = input('What spell will you cast? You can cast a "Fireball" or "Regen".')

        #Player_Cast will ask the player what spell he/she wishes to cast using a text prompt.

        if Player_Cast == ("Fireball"):

            #Typing in "Fireball" will cast a fireball at the monster, dealing between 20 and 35 damage and costing you 20 mana.

            if Player_Mana >= 20:

                #If you have 20 mana or more, the spell will cast.

                print("You cast a fireball!")

                Fireball_Damage = random.uniform(20,35)

                Fireball_Damage = int(Fireball_Damage)

                Monster_HP = Monster_HP - Fireball_Damage

                Player_Mana = Player_Mana - 20

                print("You hit the monster for %s damage!" % Fireball_Damage)

                print("The monster has %s health left!" % Monster_HP)

                print("You have %s mana left in you." % Player_Mana)

            else:

                #The following text is printed if you don't have enough mana to cast a fireball.

                print("You don't have enough mana.")

        if Player_Cast == ("Regen"):

            #Typing in "Regen" (short for "Regenerate") will heal you 30 to 50 health, at the cost of 40 mana.

            if Player_Mana >= 40:

                #If you have 40 mana or more the spell will cast.

                print("You heal yourself using magic.")

                Regen_Ammount = random.uniform(30,50)

                Regen_Ammount = int(Regen_Ammount)

                print("You heal for %s health." % Regen_Ammount)

                Player_HP = Player_HP + Regen_Ammount

                Player_Mana = Player_Mana - 40

                if Player_HP > 100:

                    Player_HP = 100

                print("You now have %s health left" % Player_HP)

                print("You now have %s mana left in you" % Player_Mana)

            else:

                #The following text prints if you don't have enough mana.

                print("You don't have enough mana.")

    #The following Player_Action prompts are easter eggs, meant to be kept out of the spotlight to be found. But for now, I will
    #comment on these easter eggs.

    #All of the easter egg attacks are based off the anime "JoJo's Bizarre Adventure".

    #"A Stand is an entity psychically generated by its proprietor, generally referred to as a Stand User
    #(スタンド使い Sutando Tsukai). It is viewed as a physical manifestation of the User's fighting spirit.
    #A Stand generally presents itself as a figure hovering near the user and possesses abilities beyond that
    #of an ordinary human, which, depending on the Stand User, can be wielded for good or for evil."
    #- JoJo's Bizarre Encyclopedia (Stand)

    if Player_Action == ("Star Platinum!!!"):

        #Stand Name: "Star Platinum" (スタープラチナ)
        #Stand User: Jotaro Kujo (空条 承太郎)

        #Typing in "Star Platinum!!!" will summon the stand known as such, he will proceed to pummel the monster with a punching rate
        #faster than any firearm you can think of, (and certainly faster then you or me could punch) dealing between 100 to 150 damage.

        #For more information on Star Platinum, I will direct you to the following links.
        # https://www.youtube.com/watch?v=OzHE5q1NGa4
        # http://jojo.wikia.com/wiki/Star_Platinum

        print("STAR PLATINUM!!!")

        time.sleep(0.5)

        print("ORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORAORA!!!!!!!!!!")

        time.sleep(1.5)

        STAR_PLATINUM = random.uniform(100,150)

        STAR_PLATINUM = int(STAR_PLATINUM)

        Monster_HP = Monster_HP - STAR_PLATINUM

        print("You used Star Platinum to pummel the monster for %s damage!!!" % STAR_PLATINUM)

        print("The monster has %s health left!" % Monster_HP)

    if Player_Action == ("Killer Queen!!!"):

        #Stand Name: "Killer Queen" (キラークイーン)
        #Stand User: Yoshikage Kira (吉良 吉影)

        #Typing in "Killer Queen!!!" will summon said stand, he will proceed to use the ability "Bites the Dust" to turn the monster into a bomb and proceed to detonate
        #the bomb, dealing 50 to 75 damage. As a result of this, tile will reverse back to a certain point in time, however, the damage is already done and
        #you heal for the same ammount of damage the bomb does.

        #For more information on Killer Queen, I will direct you to the following links.
        # https://www.youtube.com/watch?v=fiwcZ0pg3xM
        # http://jojo.wikia.com/wiki/Killer_Queen

        print("KILLER QUEEN!!! THIRD BOMB!!!")
        
        time.sleep(1.5)

        print("BITEZ ZA DUSTO!!!")

        time.sleep(0.75)

        print("*Click.*")

        time.sleep(0.75)

        print("BOOM!!!")

        BITEZ_ZA_DUSTO = random.uniform(50,75)

        BITEZ_ZA_DUSTO = int(BITEZ_ZA_DUSTO)

        Monster_HP = Monster_HP - BITEZ_ZA_DUSTO

        print("The bomb dealt %s damage to the monster!" % BITEZ_ZA_DUSTO)

        time.sleep(2)

        print("I... I did it! It activated!")

        time.sleep(3)

        Player_HP = Player_HP + BITEZ_ZA_DUSTO

        if Player_HP > 100:

            Player_HP = 100

        print("You rewind a brief period back in time but the damage done the monster is still there, due to this you also heal %s damage from yourself!" % BITEZ_ZA_DUSTO)

        print("You have %s health left." % Player_HP)

        print("The monster has %s health left." % Monster_HP)

    if Player_Action == ("The World!!!"):

        #Stand Name: "The World" (ザ・ワールド)
        #Stand User: Dio Brando (ディオ・ブランドー)

        #Typing in "The World!!!" will summon the mentioned stand, "The World" will proceed to stop time for nine seconds, after seven
        #seconds, "The World" will smash a steamroller onto the monster, and then proced to punch the steam roller with a punch rate
        #similar to Star Platinm. This move will deal 500 to 1000 damage, effectively killing the monster in one blow.

        #Note: The word "Muda" (Japanese: 無駄) means "Useless".

        #For more information on "The World", I will direct you to the following links.
        # https://www.youtube.com/watch?v=-FT23AwNPOM
        # http://jojo.wikia.com/wiki/The_World
        

        print("ZA WARUDO!!! Stop Time!!!")

        time.sleep(0.5)

        print("Time has stoped.")

        time.sleep(3)

        print("One second has elapsed...")

        time.sleep(2)

        print("Two seconds have elapsed...")

        time.sleep(2)

        print("Three seconds have elapsed...")

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

        print("*CRASH!!!!!!!*")

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

        #If the monster has zero HP or less, the loop breaks.

        break

    print ("Get Ready!")

    time.sleep(2)

    #When it is the monsters turn, the monster will deal between 5 and 20 damage to the player.

    Monster_Damage = random.uniform(5,20)

    Monster_Damage = int(Monster_Damage)

    print ("The monster hit you for %s damage!" % Monster_Damage)

    if Player_Action == ("Block"):

        #If the player is blocking, the monsters damage will be reduced by the ammount of the "Block" variable.

        print ("However, you block for %s damage!" % Player_Block)

        Player_HP = Player_HP - Monster_Damage + Player_Block

    else:

        Player_HP = Player_HP - Monster_Damage

    print ("You have %s health left!" % Player_HP)

    if Player_HP <= 0:

        #If the player has zero HP or less, the loop breaks.

        break

    print ("Compose yourself.")

    time.sleep(3)

if Monster_HP <= 0:

    #If the monster has zero HP or less, the monster dies and you have won the day!

    print ("Huzzah! The foul beast is slain!")

if Player_HP <= 0:

    #If the player has zero HP or less, you die a painful, slow and bitter death.

    print ("Your journey has come to a painful, sombre end...")
