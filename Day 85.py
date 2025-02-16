#Day 85: Text-based RPG game.


#Develop a simple text-based RPG game.

import random

# Character class
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack) - random.randint(1, enemy.defense)
        if damage > 0:
            enemy.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was ineffective against {enemy.name}!")

# Enemy class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = random.randint(1, self.attack) - random.randint(1, player.defense)
        if damage > 0:
            player.take_damage(damage)
            print(f"{self.name} attacks {player.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was ineffective against {player.name}!")

# Game setup
def create_character():
    name = input("Enter your character's name: ")
    return Character(name, health=100, attack=20, defense=10)

def create_enemy():
    enemies = [
        Enemy("Goblin", health=30, attack=10, defense=5),
        Enemy("Orc", health=50, attack=15, defense=10),
        Enemy("Dragon", health=100, attack=25, defense=20)
    ]
    return random.choice(enemies)

# Combat function
def combat(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")
        action = input("Do you want to (a)ttack or (r)un? ")
        if action == "a":
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_player(player)
        elif action == "r":
            print("You ran away!")
            break
        else:
            print("Invalid action. Try again.")

    if player.is_alive():
        print(f"You defeated the {enemy.name}!")
    else:
        print("You have been defeated... Game Over!")

# Main game loop
def main():
    print("Welcome to the Text-Based RPG Game!")
    player = create_character()
    print(f"\nWelcome, {player.name}! Your journey begins now.")

    while player.is_alive():
        enemy = create_enemy()
        combat(player, enemy)

        if player.is_alive():
            continue_playing = input("\nDo you want to continue your adventure? (y/n): ")
            if continue_playing.lower() != "y":
                print("Thank you for playing! Goodbye!")
                break
        else:
            print("Game Over!")

if __name__ == "__main__":
    main()