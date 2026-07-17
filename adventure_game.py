import random
import time
import sys

list_of_weapons = ["shotgun", "pistol", "sniper"]
ur_weapon = random.choice(list_of_weapons)
list_of_sec_weapon = ["knife", "katana", "sword"]
ur_secweapon = random.choice(list_of_sec_weapon)
score = 0

def print_pause():
    time.sleep(2)

# the introduction
def intro():
    print("Hello adventurer")
    print_pause()
    print("You find yourself standing in an open jungle, filled with trees and animals.")
    print_pause()
    print("Rumor has it that a huge creature is somewhere around here, and has been terrifying the nearby village.")
    print_pause()
    print("In front of you is an old house.")
    print_pause()
    print("To your right is a dark cave.")
    print_pause()
    # حرف الـ f رجع هنا عشان يطبع الأسلحة صح
    print(f"In your hand you hold a {ur_weapon} and a {ur_secweapon} (but the {ur_secweapon} is not very effective).")
    print_pause()
    print("enter 1 to explore the dark cave.")
    print_pause()
    print("enter 2 to go to the old house.")
    print_pause()
    print("what would you like to do?")

# replay the game 
def try_again():
    print("would you like to play again?")
    print_pause()
    print("enter 1 to accept.")
    print_pause()
    print("enter 2 to refuse.")
    restart = input()
    
    if restart == "1":
        game()
    elif restart == "2":
        print("thanks for playing our game")
        # sys.exit()
    # التعديل الصح للشرط
    elif restart not in ["1", "2"]:
        print("please enter a valid answer or the game will close")
        restart = input()
        if restart == "1":
            game()
        elif restart == "2":
            print("thanks for playing our game")
            # sys.exit()

def cave():
    print("you went to the cave")
    print_pause()
    print("there are a group of wolves attacked you")
    print_pause()
    print("you don't have enough armor")
    print_pause()
    print("you can't defeat the group")
    print_pause()
    print("you have been killed by them")
    print_pause()
    print("you lose")
    print_pause()
    print(f"your score = {score}")
    print_pause()
    try_again()

def house():
    print("you enterd the house")
    print_pause()
    print("there is an old woman")
    print_pause()
    print("the woman offerd to help you and give you the equipment that you need")
    print_pause()
    print("enter 1 to accept.")
    print_pause()
    print("enter 2 to refuse.")
    print_pause()
    print("what would you like to do?")

    woman = input()
    if woman == "1":
        print("the woman gave you the equipment that you need")
        print_pause()
        print("the woman told you the place of the creature")
        print_pause()
        print("the woman told you that the creature is hiding in the village's river")
        print_pause()
        print("now you are going to the river to kill the creature")
        print_pause()
        print("now you aproached the riverbank")
        print("you saw the creature")
        print_pause()
        print("you fought the creature and killed it!")
        print_pause()
        print("we have a champion!")
        print_pause()
        print("your score = 1000")
        print_pause()
        print("you won")
        print_pause()
        try_again()

    elif woman == "2":
        print("the woman refused to tell you the place of the creature and kicked you out of her house")
        print_pause()
        print("you have to go to the dark cave and sleep there")
        cave()

def game():
    intro()
    action = input()
    # cave
    if action == "1":
        cave()
    # house
    elif action == "2":
        house()
    # invalid
    elif action not in ["1", "2"]:
        print("please enter a valid answer or the game will close")
        print_pause()
        action = input()
        if action == "1":
            cave()
        elif action == "2":
            house()

game()
