import os
import threading # necessary for concurrent hopping and UI updates
import time
import random 

os.system('cls||clear')

# Function to simulate typing effect
def singleTyping(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Intro screen
singleTyping("-------------------------------------\n", delay=0.02)
singleTyping("Honey the Bunny: Back From the Burrow\n")
singleTyping("-------------------------------------\n", delay=0.02)
singleTyping("(\_/) ᶻᶻᶻ\n")
singleTyping("(-_-)\n")
singleTyping("/ >🥕\n\n")
singleTyping("1. Play The Game\n")
singleTyping("2. Credits\n")

choice = input("Select an option (1 or 2)\n> ")

# Option 1 for the Menu
if choice == '1':
    os.system('cls||clear')

    singleTyping("Waking up The Bunny...", delay=0.15)
    time.sleep(2)

    os.system('cls||clear')

    # rabbit display
    print("----------------")
    print("Honey The Bunny")
    print("----------------")
    print("(\_/)︕︕︕")
    print("(•_•)")
    print("/ >🥕")

    singleTyping("\nI am ready to hop!", delay=0.1)
    time.sleep(1.5)

    # The main points system (keeps track of hops)
    hops = 1

    # multiplier upgrade variables
    multiplier = 1.0
    multiplier_level = 0
    multiplier_cost = 10

    # speed upgrade variables
    speed_level = 0
    speed_cost = 20

    # prestige variables
    prestige_points = 0
    prestige_requirement = 1000

    # hop generation variables
    hop_interval = 2.5
    running = True
    
    # relic variables 
    relic_found = False # SHOULD prevent the relic from being found more than once 
    relic_bonus = 1 # default multiplier, change later to 25 if found

    # Function for hop generation
    def hop_gen():
        global hops 
        global relic_found
        global relic_bonus

        while running:
            time.sleep(hop_interval)

            # permanent prestige bonus (+10% per prestige)
            prestige_bonus = 1 + (prestige_points * 0.1)

            # hops is the total points / multiplier is what gives the points / prestige_bonus is another multiplier / relic_bonus should be 25x as well 
            hops += multiplier * prestige_bonus * relic_bonus

            # a lucky hop event that rewards points that scales with upgrades
            hops_events = random.randint(1, 10)

            if hops_events == 5:
                hops_events = 10 * multiplier
                print(f"\nYou got {int(hops_events)} Bonus Hops! Lucky!")
                hops += hops_events

            # relic event (1 in 250 chance)
            if not relic_found:

                relic_roll = random.randint(1, 250)

                if relic_roll == 100:

                    relic_found = True
                    relic_bonus = 25 # 25x multiplier 

                    print("\n✨ LEGENDARY RELIC FOUND! ✨")
                    print("Ancient Carrot of Hopping obtained!")
                    print("All hop gains are now multiplied by 25 by the relic!")
            

    # Threaded function for UI generation (goes on forever until the program is exited)
    def ui_gen():
        while running:
            os.system('cls||clear')

            print("----------------")
            print("Honey The Bunny")
            print("----------------")
            print("(\_/) ✨!")
            print("(•ᴗ•)")
            print("/ >🥕\n")
            
            if relic_found:
                print("🌟 RELIC ACTIVE 🌟") # displays that the relic is active upon receiving it 
            # displays current player stats
            print(f"Hops: {int(hops)}")
            print(f"Multiplier: x{round(multiplier, 1)}")
            print(f"Hop Interval: {round(hop_interval, 1)}s")

            # displays prestige information
            print(f"Prestige Points: {prestige_points}")
            print(f"Prestige At: {prestige_requirement} hops")

            if relic_found:
                print("Relic: Ancient Carrot 🥕✨ (x25)") # displays the relic name and its multiplier 
            else:
                print("Relic: None")

            print()
            print("----------------")
            print("Bug's Hop Shop")
            print("----------------")
            print("/╲/\\╭(•‿•)╮/\\╱\\")
            print()
            # multiplier upgrade display
            print(f"1) Multiplier Upgrade - Level {multiplier_level} - Cost: {multiplier_cost} hops")
            print("   +0.5 multiplier each purchase")

            # speed upgrade display
            print(f"2) Speed Upgrade - Level {speed_level} - Cost: {speed_cost} hops")
            print("   -0.1s interval each purchase (max 1s)")

            # prestige upgrade display
            print("3) Prestige")
            print("   Reset everything for a permanent +10% bonus")

            print("\nType 1, 2, 3, or quit")

            time.sleep(hop_interval)

    # auto generates the hops display and UI
    threading.Thread(target=hop_gen, daemon=True).start()
    threading.Thread(target=ui_gen, daemon=True).start()

    # outputs for the shop and levels / cost of upgrades
    while running:
        command = input("> ").lower()

        # multiplier upgrade purchase
        if command == "1":
            if hops >= multiplier_cost:
                hops -= multiplier_cost
                multiplier_level += 1 # adds another level to the current level
                multiplier += 0.5 # adds to the current multiplier
                multiplier_cost = int(multiplier_cost * 1.5)

        # speed upgrade purchase
        elif command == "2":
            if hops >= speed_cost and hop_interval > 1:
                hops -= speed_cost
                speed_level += 1 # adds a level to the current speed level
                hop_interval = max(1, hop_interval - 0.1) # makes sure the user doesn't go past 1 second
                speed_cost = int(speed_cost * 1.5)

        # prestige purchase / reset
        elif command == "3":
            if hops >= prestige_requirement:

                # awards prestige point
                prestige_points += 1

                # reset player progress
                hops = 0

                multiplier = 1.0
                multiplier_level = 0
                multiplier_cost = 10

                speed_level = 0
                speed_cost = 20

                hop_interval = 2.5

                # increases the next prestige requirement by double (1000 --> 2000 --> 4000)
                prestige_requirement = int(prestige_requirement * 2)

                print("Prestige successful!")
                time.sleep(2)

            else:
                print(f"You need {prestige_requirement} hops to prestige!") # Data validation to check for the right requirement
                time.sleep(2)

        # Exit command
        elif command == "quit":
            running = False
            print("Honey hops away...!")
            break

        else:
            print("False input!")

# Option 2 (Credits section)
elif choice == '2':
    os.system('cls||clear')
    singleTyping("Credits", delay=0.1)
    singleTyping("\n---------", delay=0.05)
    singleTyping("\nDeveloper - Brian Le", delay=0.05)
    singleTyping("\nProject began in early 2026")
    singleTyping("\nResources - Stack Overflow", delay=0.05)
    singleTyping("\nLast Updated: 6/3/2026")