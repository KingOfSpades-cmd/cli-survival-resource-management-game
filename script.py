from game_logic_and_backend import Player, Resources
import random

# Get the player's name
player_name = input("What is your name, survivor? ").strip().lower().capitalize()

# Create a Player object
player = Player(player_name)

# Introduction to the game
print(f"Hello {player_name}!")
print("Welcome to the Wastelands! It sucks but your goal is to survive as long as possible.")
print("Scavenge for food and water to stay alive, and be wary of wasteland dwellers.")
print("Manage your hunger, thirst, health, and energy carefully. Good luck!")

# Initialize the day counter
days = 0

# Main game loop
while player.is_alive:
    days += 1
    print(f"\nDay {days}:")
    print("You wake up in your shelter.")
    print(player.get_status())  # Display player's current status

    # Daily updates: Increase hunger and thirst, decrease energy
    player.hunger += 5
    player.thirst += 5
    player.energy -= 2.5

    # Check if the player has died
    if player.hunger >= 100 or player.thirst >= 100 or player.health <= 0 or player.energy <= 0:
        player.is_alive = False
        print("You have died. Game over.")
        break

    # Check if the player is too tired to perform actions
    if player.energy < 20:
        print("You are too tired to scavenge or collect water. You need to rest. Would you like to sleep? (y/n)")
        sleep_choice = input().strip().lower()
        if sleep_choice == "y":
            player.sleep()  # Restore energy by sleeping
            print("You slept well and regained 50 energy!")
        else:
            player.health -= 10
            player.energy -= 20
            print("You chose not to sleep. You lost 10 health and 20 energy.")
        continue  # Skip to the next day

    # Display the main menu
    print("\nWhat would you like to do?")
    print("1. Check status")
    print("2. Scavenge for food")
    print("3. Collect water")
    print("4. Sleep")
    print("5. Check inventory")
    print("6. Quit game")

    # Get the player's choice
    choice = input("Enter your choice: ").strip()

    # Process the player's choice
    if choice == "1":
        print(player.get_status())  # Display player's status
    elif choice == "2":
        player.scavenge_food()  # Scavenge for food
    elif choice == "3":
        player.collect_water()  # Collect water
    elif choice == "4":
        player.sleep()  # Sleep to restore energy
        print("You slept well and regained 50 energy!")
    elif choice == "5":
        # Inventory management loop
        while True:
            player.check_inventory()  # Display inventory contents
            print("Enter the number of the item you want to use (or '0' to return): ")
            try:
                item_index = int(input())
                if item_index == 0:
                    break  # Return to main menu
                player.use_item(item_index)  # Use the selected item
            except ValueError:
                print("Invalid input.")
    elif choice == "6":
        print("Thanks for playing!")
        break  # Quit the game
    else:
        print("Invalid choice. Please try again.")

# Game over sequence
if not player.is_alive:
    # Determine the cause of death
    if player.hunger >= 100:
        cause_of_death = "hunger"
    elif player.thirst >= 100:
        cause_of_death = "thirst"
    elif player.health <= 0:
        cause_of_death = "health"
    elif player.energy <= 0:
        cause_of_death = "energy"
    else:
        cause_of_death = "unknown causes"

    print(f"The cause of death was: {cause_of_death}.")
    print("Days survived: ", days)
    print(player.display_stats())  # Display player's statistics
# End of game loop

