from enemy import Enemy
from myplayer import MyPlayer
import sys

my_player = MyPlayer()

enemy = Enemy()

toggle = 0


while my_player.life > 0 or enemy.life > 0:

    choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choice == "1" and toggle == 1:
        my_player.life -= enemy.damage()
        if my_player.life < 0:
            print("Tu as perdu")
            sys.exit()
        toggle = 0
        print(f"enemy pv {enemy.life}, my player pv {my_player.life}")


    elif choice == "1":
        enemy.life -= my_player.damage()
        my_player.life -= enemy.damage()


        if int(my_player.life) < 0:
            print("Tu as perdu")
            sys.exit()

        
        elif int(enemy.life) < 0:
            print("ennemi a perdu")
            sys.exit()

        else:

            print(f"enemy pv {enemy.life}, my player pv {my_player.life}")


    elif choice == "2" and my_player.potion > 0:
        my_player.recover_life()
        my_player.potion -= 1
        my_player.life -= enemy.damage()
        toggle = 1
        print(f"enemy pv {enemy.life}, my player pv {my_player.life}")


    elif choice == "2" and my_player.potion == 0:
        print("vous n'avez plus de potions")

