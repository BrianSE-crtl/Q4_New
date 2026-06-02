import os
import threading # necessary for concurrent hopping and UI updates
import time

os.system('cls||clear')

# Function to simulate typing effect
def singleTyping(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# Intro screen
singleTyping("--------------------\n", delay=0.02)
singleTyping("Bunny Hop Gone Wrong\n")
singleTyping("--------------------\n", delay=0.02)
singleTyping("(\_/)\n")
singleTyping("( -_-)\n\n")
singleTyping("1. Play The Game\n")
singleTyping("2. Credits\n")
choice = input("Select an option (1 or 2)\n> ")


# Option 1 for the Menu
if choice == '1':
    os.system('cls||clear')
    singleTyping("Waking up The Bunny...", delay=0.15)
    time.sleep(2)
    os.system('cls||clear')

    print("----------------")
    print("Honey The Bunny")
    print("----------------")
    print("(\_/)")
    print("( •_•)")
    singleTyping("\nI am ready to hop!", delay=0.1)
    time.sleep(1.5)

    # The main points system (keeps track of hops)
    hops = 0.0

    # multiplier upgrade variables
    multiplier = 1.0
    multiplier_level = 0
    multiplier_cost = 10

    # speed upgrade variables
    speed_level = 0
    speed_cost = 20

    # hop generation variables  
    hop_interval = 1.5
    running = True

    # Function for hop generation 
    def hop_gen():
        global hops # makes sure to use the hops that every other block is using.
        while running:
            time.sleep(hop_interval)
            hops += multiplier # hops is the total points / multiplier is what gives the points

    # Threaded function for UI generation (goes on forever until the program is exited)
    def ui_gen():
        while running:
            os.system('cls||clear')
            print("----------------")
            print("Honey The Bunny")
            print("----------------")
            print("(\_/)")
            print("( •_•)\n")
            print(f"Hops: {int(hops)}")
            print(f"Multiplier: x{round(multiplier, 1)}")
            print(f"Hop Interval: {round(hop_interval, 1)}s\n")
            print("----------------")
            print("Bug's Hop Shop")
            print("----------------")
            print(f"1) Multiplier Upgrade - Level {multiplier_level} - Cost: {multiplier_cost} hops")
            print("   +0.5 multiplier each purchase")
            print(f"2) Speed Upgrade - Level {speed_level} - Cost: {speed_cost} hops")
            print("   -0.1s interval each purchase (min 1s)")
            print("\nType 1, 2, or quit (make sure to press Enter after):")
            time.sleep(hop_interval)

    # auto generates the hops display and UI
    threading.Thread(target=hop_gen, daemon=True).start()
    threading.Thread(target=ui_gen, daemon=True).start()

    # outputs for the shop and levels / cost of upgrades
    while running:
        command = input("> ").lower()

        if command == "1":
            if hops >= multiplier_cost:
                hops -= multiplier_cost
                multiplier_level += 1 # adds another level to the current level
                multiplier += 0.5 # adds to the current multiplier
                multiplier_cost = int(multiplier_cost * 1.5)

        elif command == "2":
            if hops >= speed_cost and hop_interval > 1:
                hops -= speed_cost
                speed_level += 1 # adds a level to the current speed level
                hop_interval = max(1, hop_interval - 0.1) # makes sure the user doesn't go past 1 second
                speed_cost = int(speed_cost * 1.5)

        # Exit command
        elif command == "quit":
            running = False
            print("Goodbye!")
            break
        else:
            print("False input!")
# Option 2 (About Me section)
elif choice == '2': 
    os.system('clear||cls')
    singleTyping("Credits", delay=0.1)
    singleTyping("\n---------", delay=0.05)
    singleTyping("\nDeveloper - Brian Le", delay=0.05)
    singleTyping("\nResources - Stack Overflow ", delay=0.05)
    singleTyping("\n~1/11/26", delay=0.05)