import random

class Player:
    def __init__(self, name):
        # Initialize player attributes
        self.name = name
        self.hunger = 0
        self.thirst = 0
        self.health = 100
        self.energy = 100
        self.is_alive = True
        self.inventory = []  # List to store items
        self.inventory_capacity = 3  # Maximum number of items the player can carry

        # Initialize player stats
        self.scavenge_count = 0
        self.collect_water_count = 0
        self.attack_count = 0
        self.items_count = 0

    def __repr__(self):
        # String representation of the Player object for debugging purposes
        return f"Player(name={self.name}, hunger={self.hunger}, thirst={self.thirst}, health={self.health}, energy={self.energy}, is_alive={self.is_alive})"

    def get_status(self):
        # Print the player's current status and inventory
        print(repr(self))  # Calls the __repr__ method and prints the status of the player
        print(f"Inventory: {self.inventory}")  # Print the inventory of the player

    def display_stats(self):
        # Display the player's statistics
        print(f"Times scavenged: {self.scavenge_count}")
        print(f"Times collected water: {self.collect_water_count}")
        print(f"Times attacked: {self.attack_count}")
        print(f"Times items found: {self.items_count}")
        print("inventory")
        if self.inventory:
            print("Your inventory contained:")
            for i, item in enumerate(self.inventory):
                print(f"{i + 1}. {item.name} (Quantity: {item.quantity}, Replenishes: {item.get_replenishment_value()})")

    def check_inventory(self):
        # Check and display the contents of the player's inventory
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for i, item in enumerate(self.inventory):
                print(f"{i + 1}. {item.name} (Quantity: {item.quantity}, Replenishes: {item.get_replenishment_value()})")

    def use_item(self, item_index):
        # Use an item from the player's inventory
        if 0 < item_index <= len(self.inventory):
            item_to_use = self.inventory.pop(item_index - 1) # Remove the item from the inventory
            print(f"You used {item_to_use.name}.")
            if item_to_use.name == "Water":
                self.thirst -= item_to_use.get_replenishment_value() # Decrease thirst by the item's replenishment value
                self.thirst = max(0, self.thirst)  # Ensure thirst does not go below 0
            elif item_to_use.name in ["burger", "banana", "beans", "candy"]:
                self.hunger -= item_to_use.get_replenishment_value()  # Decrease hunger by the item's replenishment value
                self.hunger = max(0, self.hunger)  # Ensure hunger does not go below 0
            elif item_to_use.name == "medkit":
                self.health += item_to_use.get_replenishment_value()  # Increase health by the item's replenishment value
                self.health = min(self.health, 100)  # Ensure health does not exceed 100
            elif item_to_use.name == "energy drink":
                self.energy += item_to_use.get_replenishment_value()  # Increase energy by the item's replenishment value
                self.energy = min(self.energy, 100)  # Ensure energy does not exceed 100
            else:
                print("You can't use this item.")

    def scavenge_food(self):
        # Scavenge for food in the wasteland
        self.energy -= 5  # Reduce energy
        self.scavenge_count += 1  # Increment scavenge count
        print("You venture out to scavenge for food...(-20 energy)")
        found_food = None
        if random.random() < 0.7:  # 70% chance of finding food
            self.items_count += 1  # Increment items found count
            possible_foods = {"burger": 20, "banana": 5, "beans": 10, "candy": 1}
            if random.random() < 0.1: # 10% chance of finding a medkit or energy drink
                possible_foods['medkit'] = 50
                possible_foods['energy drink'] = 30
                chosen_food_name = random.choice(list(possible_foods.keys()))
                found_food = Resources(chosen_food_name, 1)
            chosen_food_name = random.choice(list(possible_foods.keys()))
            found_food = Resources(chosen_food_name, 1)
            found_food.replenishment_value = found_food.get_replenishment_value()

            print(f"You found a {found_food.name} (Replenishes: {found_food.replenishment_value} hunger)!")
            if len(self.inventory) < self.inventory_capacity:
                self.inventory.append(found_food)
                print(f"Added {found_food.name} to your inventory.")
            else:
                print("Your inventory is full.")
                replace = input("Would you like to replace an item? (y/n): ").strip().lower()
                if replace == 'y':
                    self.check_inventory()
                    try:
                        replace_index = int(input("Enter the number of the item to replace: ")) - 1
                        if 0 <= replace_index < len(self.inventory):
                            self.inventory[replace_index] = found_food
                            print(f"Replaced {self.inventory[replace_index].name} with {found_food.name}.")
                        else:
                            print("Invalid item number.")
                    except ValueError:
                        print("Invalid input.")
                else:
                    print("You had to leave it behind.")
        else:
            print("You didn't find any food today.")

        if random.random() < 0.075:  # Reduced attack frequency by half
            self.attack_count += 1
            health_loss = random.randint(1, 10)
            self.health -= health_loss
            print(f"You were attacked by wasteland dwellers and lost {health_loss} health.")
            if self.health <= 0:
                self.is_alive = False
                print("You have died.")

    def collect_water(self):
        # Collect water in the wasteland
        self.energy -= 5  # Reduce energy
        self.collect_water_count += 1  # Increment collect water count
        print("You venture out to collect water...(-15 energy)")
        found_water = None
        if random.random() < 0.875:  # Increased base random number of water
            found_water = Resources("Water", 1)
            found_water.replenishment_value = found_water.get_replenishment_value()

            print(f"You found some {found_water.name} (Replenishes: {found_water.replenishment_value} thirst)!")
            if random.random() < 0.1:  # 10% chance of finding a medkit or energy drink
                possible_items = ["medkit", "energy drink"]
                chosen_item = random.choice(possible_items)
                found_item = Resources(chosen_item, 1)
                if len(self.inventory) < self.inventory_capacity:
                    self.inventory.append(found_item)
                    print(f"You found a {found_item.name}!")
                else:
                    print(f"You found a {found_item.name}, but your inventory is full.")
            if found_water:
                if len(self.inventory) < self.inventory_capacity:
                    self.inventory.append(found_water)
                    print(f"Added {found_water.name} to your inventory.")
                else:
                    print("Your inventory is full.")
                    replace = input("Would you like to replace an item? (y/n): ").strip().lower()
                    if replace == 'y':
                        self.check_inventory()
                        try:
                            replace_index = int(input("Enter the number of the item to replace: ")) - 1
                            if 0 <= replace_index < len(self.inventory):
                                self.inventory[replace_index] = found_water
                                print(f"Replaced {self.inventory[replace_index].name} with {found_water.name}.")
                            else:
                                print("Invalid item number.")
                        except ValueError:
                            print("Invalid input.")
                    else:
                        print("You had to leave it behind.")
        else:
            print("You didn't find any water today.")

        if random.random() < 0.075:  # Reduced attack frequency by half
            health_loss = random.randint(1, 5)
            self.health -= health_loss
            print(f"You were attacked by wasteland dwellers and lost {health_loss} health.")
            if self.health <= 0:
                self.is_alive = False
                print("You have died.")

    def sleep(self):
        # Restore player's energy
        print("You find a safe place to sleep...(+50 energy)")
        self.energy += 50
        self.energy = min(self.energy, 100)


class Resources:
    def __init__(self, name, quantity):
        # Initialize resource attributes
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        # String representation of the Resources object for debugging purposes
        details = f"{self.name} (Quantity: {self.quantity})"
        return details

    def get_details(self):
        # Print the resource's details
        print(repr(self))

    def get_replenishment_value(self):
        # Get the replenishment value of the resource
        possible_foods = {"burger": 30, "banana": 10, "beans": 20, "candy": 5}
        possible_drinks = {"Water": random.randint(15, 50)}
        item_medkits = {"medkit": 50}
        item_energy_drink = {"energy drink": 30}
        if self.name in possible_foods:
            return possible_foods[self.name]
        elif self.name in possible_drinks:
            return possible_drinks[self.name]
        elif self.name in item_medkits:
            return item_medkits[self.name]
        elif self.name in item_energy_drink:
            return item_energy_drink[self.name]
        else:
            return 0  # Return 0 if the item is not found

