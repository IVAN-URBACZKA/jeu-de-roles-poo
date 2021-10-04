from enemy import Enemy
from myplayer import MyPlayer
import sys

my_player = MyPlayer()

enemy = Enemy()

toggle = 0


while my_player.get_life() > 0 or enemy.get_life() > 0:

    choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choice == "1" and toggle == 1:
        my_player.set_life(my_player.get_life() - enemy.damage())
        if my_player.get_life() < 0:
            print("Tu as perdu")
            sys.exit()
        toggle = 0
        print(f"enemy pv {enemy.get_life()}, my player pv {my_player.get_life()}")


    elif choice == "1":
        enemy.set_life(enemy.get_life() - my_player.damage())
        my_player.set_life(my_player.get_life() - enemy.damage())

        if int(my_player.get_life()) < 0:
            print("Tu as perdu")
            sys.exit()

        
        elif int(enemy.get_life()) < 0:
            print("ennemi a perdu")
            sys.exit()

        else:

            print(f"enemy pv {enemy.get_life()}, my player pv {my_player.get_life()}")


    elif choice == "2" and my_player.get_potion() > 0:
        my_player.recover_life()
        my_player.set_potion(my_player.get_potion() - 1) 
        my_player.set_life(my_player.get_life() - enemy.damage())

        toggle = 1
        print(f"enemy pv {enemy.get_life()}, my player pv {my_player.get_life()}")


    elif choice == "2" and my_player.get_potion == 0:
        print("vous n'avez plus de potions")
